import cv2
import os
import time
from datetime import datetime

# =========================
# CAMERA SETTINGS
# =========================

CAMERA_INDEX = 0

CAPTURE_WIDTH = 2304
CAPTURE_HEIGHT = 1296

PROCESS_WIDTH = 512
PROCESS_HEIGHT = 288

ROI = (140, 60, 380, 230)

MIN_CONTOUR_AREA = 250
MOTION_COOLDOWN = 5

BURST_COUNT = 5
BURST_DELAY = 0.4  # seconds between burst images

BASE_SAVE_DIR = "/home/bombus/bombuscam-01/

# =========================

os.makedirs(BASE_SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAPTURE_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_HEIGHT)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

time.sleep(2)

background = None
last_capture_time = 0

print("Starting insect motion detection...")

while True:

    ret, full_frame = cap.read()
    if not ret:
        continue

    # -------------------------
    # Daily folder creation
    # -------------------------
    date_str = datetime.now().strftime("%Y-%m-%d")
    save_dir = os.path.join(BASE_SAVE_DIR, date_str)
    os.makedirs(save_dir, exist_ok=True)

    # -------------------------
    # Motion detection frame
    # -------------------------
    process_frame = cv2.resize(full_frame, (PROCESS_WIDTH, PROCESS_HEIGHT))

    x1, y1, x2, y2 = ROI
    roi = process_frame[y1:y2, x1:x2]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if background is None:
        background = gray
        continue

    delta = cv2.absdiff(background, gray)

    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    motion = False

    for c in contours:
        if cv2.contourArea(c) < MIN_CONTOUR_AREA:
            continue
        motion = True
        break

    # -------------------------
    # BURST CAPTURE
    # -------------------------
    now = time.time()

    if motion and (now - last_capture_time > MOTION_COOLDOWN):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"[MOTION] Burst capture triggered at {timestamp}")

        for i in range(BURST_COUNT):

            ret, frame = cap.read()
            if not ret:
                continue

            filename = os.path.join(
                save_dir,
                f"insect_{timestamp}_b{i:02d}.jpg"
            )

            cv2.imwrite(
                filename,
                frame,
                [cv2.IMWRITE_JPEG_QUALITY, 90]
            )

            print(f"  saved {filename}")

            time.sleep(BURST_DELAY)

        last_capture_time = now

    # -------------------------
    # Update background slowly
    # -------------------------
    background = cv2.addWeighted(background, 0.9, gray, 0.1, 0)
