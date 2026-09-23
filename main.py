from my_utils.detection import detect_vehicles
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import torch

import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from flask import Flask, render_template, Response
import cv2
import torch
import os
import sys

app = Flask(__name__)

# Load YOLOv5 model
sys.path.insert(0, os.path.join(os.getcwd(), 'yolov5'))
model = torch.hub.load('yolov5', 'custom', path='models/yolov5s.pt', source='local', force_reload=True)
vehicle_classes = ['car', 'motorcycle', 'bus', 'truck']


# ---------------- ROUTES ---------------- #

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/traffic')
def traffic():
    return render_template('traffic.html')

@app.route('/signal')
def signal():
    return render_template('signal.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')


# ------------- VIDEO STREAMING ------------- #
def generate_frames(cam_id):
    cap = cv2.VideoCapture(f'videos/side{cam_id}.mp4')
    while True:
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        frame = cv2.resize(frame, (640, 480))
        _, _ = detect_vehicles(frame)  # Just to simulate detection
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/traffic_feed/<int:cam_id>')
def traffic_feed(cam_id):
    return Response(generate_frames(cam_id), mimetype='multipart/x-mixed-replace; boundary=frame')



# ------------- MAIN ------------- #
if __name__ == '__main__':
    app.run(debug=True)
