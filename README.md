# BoundBox - Vision ROI & Intrusion Detection System

**BoundBox** is a real-time computer vision system built with Python, OpenCV, and Ultralytics YOLO. It monitors live video feeds (such as IP camera streams or webcams), defines custom Region of Interest (ROI) boundaries / danger zones, detects specific target classes, and triggers instant visual alerts when targets cross or intersect defined boundaries.

---

## Current Features

- **Real-Time Video Ingestion**: Supports HTTP, RTSP, IP webcam streams, and local camera feeds.
- **Region of Interest (ROI) / Danger Zone**: Configurable bounding coordinates for targeted zone monitoring.
- **Target Intersection Math**: Real-time bounding box intersection and overlap calculation.
- **YOLO Deep Learning Detection**: Fast, lightweight object inference powered by YOLO.
- **Visual Alerting**: Dynamic UI state changes (e.g., green for clear, red alert banners when intrusions occur).

---

## Future Roadmap & Ahead Tasks

The following capabilities are planned for upcoming iterations:

### 1. Gesture-Initiated Dynamic Object Tracking
- **Gesture Selection**: Point at or select specific objects using hand gestures within the camera frame to initiate tracking.
- **Persistent Tracking**: The selected object is locked and tracked continuously as long as it remains within the camera's viewing radius and field of view.

### 2. Object Recognition & Database Tagging
- **Viewing Angle Recognition**: Detect and classify objects entering the camera's viewing angle in real time.
- **Database Metadata Mapping**: Cross-reference detected objects with an internal database to display custom names, classifications, and item attributes.

### 3. Facial Recognition & Automatic Person Enrollment
- **New Face Detection**: Automatically detect when a new individual enters the frame.
- **Interactive Enrollment**: Prompt for the person's name and store their facial embeddings and reference snapshots in a dedicated project directory (e.g., `faces/`).
- **Dynamic Recognition**: Recognize returning individuals instantly and keep profile records updated as new people appear in view.

### 4. Target Area Analytics & Object Counting
- **Bounding Area Interception**: Advanced target area definitions supporting multiple custom polygons and bounding zones.
- **Object Counting & Ingress/Egress**: Count the number of objects or persons intersecting or crossing into designated bounding boxes over time.

---

## Project Structure

```text
bound-box/
├── main.py              # Main application loop and YOLO detection logic
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules (weights, virtual environments, data)
└── README.md            # Project documentation and roadmap
```

---

## Getting Started

### 1. Prerequisites
- Python 3.9+ installed
- WSL2 / Linux / Windows / macOS
- An active webcam or IP camera stream (e.g., IP Webcam mobile app)

### 2. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd bound-box
```

### 3. Setup Virtual Environment
```bash
python3 -m venv env
source env/bin/activate   # On Linux / WSL
# On Windows PowerShell: .\env\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note on Model Weights**: Large `.pt` weight files (such as `yolo26n.pt`) are ignored in version control. Ultralytics YOLO will automatically download the required model weights on first execution.

### 5. Configuration & Execution
Edit `CAMERA_URL` and `ROI` coordinates in `main.py` to match your video source and preferred zone:

```python
# main.py
CAMERA_URL = "http://<YOUR_IP>:8080/video"  # Or 0 for local webcam
ROI = [100, 200, 500, 400]                # [x_min, y_min, x_max, y_max]
```

Run the application:
```bash
python3 main.py
```
Press `q` on the video window to stop the stream.

---

## License
MIT License.