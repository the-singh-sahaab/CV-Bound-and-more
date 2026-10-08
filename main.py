import cv2
from ultralytics import YOLO

# 1. Configuration
CAMERA_URL = "http://192.168.178.47:8080/video"

# Define your Region of Interest (ROI) / "Danger Zone"
# Format: [x_min, y_min, x_max, y_max]
# You will need to adjust these numbers based on your tablet camera's resolution
ROI = [100, 200, 500, 400] 

# YOLO class ID to look for. 
# 0 = Person, 16 = Dog, 67 = Cell phone, 73 = Book
TARGET_CLASS = 0  

def check_overlap(box_a, box_b):
    """Math: Checks if two bounding boxes intersect."""
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    # If the right edge is past the left edge, and the bottom is below the top, they overlap
    if x_right > x_left and y_bottom > y_top:
        return True
    return False

def main():
    print("Loading YOLO model...")
    # Downloads the lightweight 'nano' model automatically on first run
    model = YOLO("yolo26n.pt") 

    cap = cv2.VideoCapture(CAMERA_URL)
    if not cap.isOpened():
        print("Error: Could not open the video stream.")
        return

    print("Stream connected! Press 'q' to quit.")

    while True:
        success, frame = cap.read()
        if not success:
            break
            
        # Default zone color is Green (Safe)
        zone_color = (0, 255, 0)
        intrusion_detected = False

        # Run YOLO detection on the frame
        # stream=True keeps it fast for real-time video processing
        results = model(frame, stream=True, verbose=False) 

        for result in results:
            # Extract all bounding boxes found in this frame
            boxes = result.boxes
            
            for box in boxes:
                # Get the ID of the object detected
                cls_id = int(box.cls[0])
                
                # Only process if it is our target object
                if cls_id == TARGET_CLASS:
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detected_box = [x1, y1, x2, y2]
                    
                    # Draw the detected object's bounding box in Blue
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, "Target", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                    # Check for overlap with the Danger Zone
                    if check_overlap(detected_box, ROI):
                        intrusion_detected = True

        # Change zone color to Red if an intrusion is detected
        if intrusion_detected:
            zone_color = (0, 0, 255)
            cv2.putText(frame, "ALERT: INTRUSION DETECTED!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # Draw the Danger Zone (ROI) on the screen
        cv2.rectangle(frame, (ROI[0], ROI[1]), (ROI[2], ROI[3]), zone_color, 3)
        cv2.putText(frame, "Danger Zone", (ROI[0], ROI[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, zone_color, 2)

        cv2.imshow("Watchdoggy Simulator", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()