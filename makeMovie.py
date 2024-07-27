import cv2
import os

frame_dir = 'output'

video_path = 'time_lapse_video.mp4'

frame_rate = 30

frame_files = sorted(
    [f for f in os.listdir(frame_dir) if f.endswith('.jpg')],
    key=lambda x: int(os.path.splitext(x)[0])
)

first_frame = cv2.imread(os.path.join(frame_dir, frame_files[0]))
height, width, layers = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_path, fourcc, frame_rate, (width, height))

for frame_file in frame_files:
    frame_path = os.path.join(frame_dir, frame_file)
    frame = cv2.imread(frame_path)
    video.write(frame)

video.release()
print(f"Time-lapse video saved to {video_path}")
