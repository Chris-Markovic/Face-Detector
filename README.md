Face & Hand Tracker

A real-time computer vision app in Python that uses your webcam to detect faces and track hands.
Faces are detected with OpenCV's Haar cascade classifier and marked with a red box labelled "Target".
Hands are tracked with Google's MediaPipe, which draws 21 landmarks (joints and fingertips) on up to two hands at once.



Features:

-Live face detection from the webcam feed

-Hand tracking for up to two hands, with joints and connections drawn on screen

-Runs locally, no internet connection needed



Tech stack:

Python

OpenCV – video capture, face detection, drawing

MediaPipe – hand landmark detection



Installation:

Requirements: Python 3.10–3.12 (MediaPipe may not support the newest Python versions yet) and a webcam.

Clone the repository and go into the folder:

git clone https://github.com/Chris-Markovic/Face-Detector.git

cd Face-Detector



Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate      # macOS / Linux

venv\Scripts\activate         # Windows



Install the dependencies:

pip install -r requirements.txt



Usage:

Start the program:

python face_tracker.py



A window with your webcam feed opens. Faces get a red "Target" box, and hands are drawn with their landmarks.

To quit: click on the video window and press x.

macOS: the first time you run it, allow your terminal (or VS Code) to access the camera in System Settings -> Privacy & Security -> Camera.



How it works:

Each frame from the webcam is read with OpenCV.

The frame is converted to greyscale, and the Haar cascade scans it for faces at different scales.

The frame is converted to RGB and passed to MediaPipe, which returns the positions of the hand landmarks.

The boxes and landmarks are drawn on the frame, which is shown in the window.



Configuration:

You can adjust the detection in face_tracker.py:

minNeighbors	10	=. Higher = fewer false face detections, but may miss some faces

minSize	(60, 60)	= Ignores faces smaller than this (in pixels)

max_num_hands	2	 = Maximum number of hands tracked

min_detection_confidence	0.6	= How sure MediaPipe must be before detecting a hand



Troubleshooting:

"Could not open webcam." – another app may be using the camera, or the terminal doesn't have camera permission.

Install errors for MediaPipe – check that you're using Python 3.10–3.12.

