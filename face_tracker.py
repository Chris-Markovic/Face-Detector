import cv2
import mediapipe as mp


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

mp_hands = mp.solutions.hands 
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode = False,
    max_num_hands = 2,
    min_detection_confidence = 0.6,
    min_tracking_confidence = 0.5,
)




cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError(
        "Could not open webcam."
    )

print("Face tracker initiated. Press 'x' in the video window to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,      # how much the image size is reduced at each scale
        minNeighbors=10,       # higher = fewer false positives
        minSize=(60, 60),     # ignore detections smaller than this (pixels)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(
            frame,
            "Target",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2,
        )

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_results = hands.process(rgb_frame)

    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )


    cv2.imshow("Face Tracker - press q to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()
