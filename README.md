# intelligent-traffic-monitoring-system 
# Repository Structure
traffic2/
│
├── models/         # Pre-trained and fine-tuned model weights (.pt files)
├── my_utils/       # Utility scripts for image processing & video frame handling
├── static/         # CSS, JavaScript, and static web assets
├── templates/      # HTML templates for the web interface
├── videos/         # Sample input/test video files for traffic detection
├── yolov5/         # Core YOLOv5 object detection framework dependencies
│
├── app.py          # Main Flask application / web server entry point
└── detect8.py      # Core detection, tracking, and metric calculation script
```[span_9](start_span)[span_9](end_span)

---

## 🚀 Features
* **Real-Time Object Detection:** Identifies cars, buses, trucks, and motorbikes in live streams or pre-recorded video[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).
* **Traffic Density Analysis:** Measures vehicle density per lane to provide real-time traffic statistics[span_12](start_span)[span_12](end_span).
* **Web Dashboard:** Interactive frontend built with HTML/Flask to display traffic feeds and detection outputs directly in the browser[span_13](start_span)[span_13](end_span).

---

## 🛠️ Tech Stack & Tools
* **Language:** Python[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span)[span_16](start_span)[span_16](end_span)
* **Computer Vision:** OpenCV, PyTorch, YOLOv5[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span)
* **Web Architecture:** Flask (Python), HTML/CSS/JS[span_19](start_span)[span_19](end_span)[span_20](start_span)[span_20](end_span)
* **Data & Analytics:** NumPy, Matplotlib[span_21](start_span)[span_21](end_span)

---

## 🔧 How to Run locally

### 1. Prerequisites
Ensure Python 3.8+ is installed on your system[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span).

### 2. Clone the Repository
```bash
git clone https://github.com/[your-username]/traffic-monitoring-system.git
cd traffic-monitoring-system

#install Dependencies
pip install -r requirements.txt

# Run the Application
python app.py
