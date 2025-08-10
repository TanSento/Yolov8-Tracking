# YOLOv8 Object Tracking

A computer vision project using YOLOv8 for real-time object detection and tracking in videos.

## Features

- Real-time object detection using YOLOv8n (nano model)
- Multi-object tracking with persistent IDs
- Video processing with OpenCV
- Bounding box visualization
- Class label display

## Requirements

```bash
pip install ultralytics opencv-python
```

## Usage

1. Place your video file as `test.mp4` in the project directory
2. Run the tracking script:

```bash
python main.py
```

3. Press 'q' to quit the video display

## Model Information

- **Model**: YOLOv8n (nano version)
- **Classes**: 80 COCO dataset classes
- **Tracker**: BoT-SORT (default)

## File Structure

