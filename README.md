# Create Timelapses from TP-Link Tapo C310 Security Camera (Python Script)

**Introduction:**

This Python script automates the creation of timelapses from your TP-Link Tapo C310 security camera. It simplifies the process of capturing frames and stitching them together into an MP4 video.

**Prerequisites:**  Make sure you have Python 3 and OpenCV installed. You can install them using pip:

```bash
pip install opencv-python
```

## Start Timelapse

To capture frames and create a timelapse, run the following command:

```bash
python timelapse.py
```

Frames will be stored in the ./output directory.
### Note
* Make sure to edit the rtsp_url in timelapse.py to include the correct username, password, and IP address of your TP-Link Tapo C310 camera.


## Create MP4 from Captured Frames
Once you have captured the frames, you can generate an MP4 video by running:

```bash
python makeMovie.py
```
This script will search for frames in the ./output directory and compile them into a video file.
