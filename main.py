from ultralytics import YOLO
import cv2


# load yolov8 model
model = YOLO("yolov8n.pt") # load a pretrained YOLOv8n model, 8n is the nano(small) model

# load video
video_path = "./test.mp4"
cap = cv2.VideoCapture(video_path)

ret = True # return value
# read frames until the end of the video
while ret:
    ret, frame = cap.read() # read frame by frame
    if not ret:
        break
    
    # detect objects
    

    # track objects
    results = model.track(frame, persist=True) # persist=True means that the model will be saved to the disk
                                               # returns a list of results, each result is a list of detections
                                               # each detection is a dictionary with the following keys:
                                               # 'boxes', 'masks', 'keypoints', 'labels', 'scores'
                                               # 'boxes' is a list of bounding boxes, each bounding box is a list of 4 numbers [x1, y1, x2, y2]
                                               # 'masks' is a list of masks, each mask is a list of 4 numbers [x1, y1, x2, y2]
                                               # 'keypoints' is a list of keypoints, each keypoint is a list of 2 numbers [x, y]
                                               # 'labels' is a list of labels, each label is a string
                                               # 'scores' is a list of scores, each score is a number
    # # plot results
    # frame_ = results[0].plot()

    # another way to plot results using cv2
    for result in results:
        boxes = result.boxes # get the bounding boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # get the bounding box coordinates
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to integers
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2) # draw the bounding box
            cv2.putText(frame, result.names[int(box.cls)], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) # draw the label



    # visualize results
    cv2.imshow("frame", frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):  # wait for 25ms and if q is pressed, break the loop
        break
