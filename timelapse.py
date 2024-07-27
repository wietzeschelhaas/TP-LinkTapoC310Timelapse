import cv2
import os
import time

# Define the RTSP URL
rtsp_url = 'rtsp://user:password@ip:554/stream1'

save_dir = 'output'
os.makedirs(save_dir, exist_ok=True)

capture_interval = 10  # Capture a frame every 30 seconds

frame_count = 0

while True:
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Error: Could not open video stream")
        time.sleep(2)
    else:
        ret, frame = cap.read()

        if ret:
            currentTime = int(time.time()) 

            image_path = os.path.join(save_dir, f'{currentTime}.jpg')
            cv2.imwrite(image_path, frame)
            print(f"Captured frame {frame_count}")

            frame_count += 1

            time.sleep(capture_interval)
        else:
            print("Error: Could not read frame")

        cap.release()
