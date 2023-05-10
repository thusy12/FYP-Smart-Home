import cv2
import numpy as np

# Load the pre-trained YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load the class labels
classes = []
with open("C:/Users/HP/Desktop/synchronization/darknet/data/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set up the webcam
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("C:/Users/HP/Desktop/synchronization/1.mp4")


# Set the camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize the first frame of the video stream
first_frame = None

# Create kernel for morphological operation. You can tweak
# the dimensions of the kernel.
# e.g. instead of 20, 20, you can try 30, 30
kernel = np.ones((20,20),np.uint8)

# Centimeter to pixel conversion factor
# I measured 32.0 cm across the width of the field of view of the camera.
CM_TO_PIXEL = 32.0 / 640

# Define the object coordinates dictionary
object_coords = {}

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to a blob
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)

    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    # Close gaps using closing
    gray = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
       
    # Remove salt and pepper noise with a median filter
    gray = cv2.medianBlur(gray,5)

    # If first frame, we need to initialize it.
    if first_frame is None:
         
      first_frame = gray
       
      # Go to top of loop
      continue
       
    # Calculate the absolute difference between the current frame
    # and the first frame
    absolute_difference = cv2.absdiff(first_frame, gray)

    # If a pixel is less than ##, it is considered black (background). 
    # Otherwise, it is white (foreground). 255 is upper limit.
    # Modify the number after absolute_difference as you see fit.
    _, absolute_difference = cv2.threshold(absolute_difference, 50, 255, cv2.THRESH_BINARY)
 
    # Find the contours of the object inside the binary image
    contours, hierarchy = cv2.findContours(absolute_difference,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]
    areas = [cv2.contourArea(c) for c in contours]
  

    # Set the input to the model
    net.setInput(blob)

    # Forward pass through the model
    output_layers = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers)

    # Extract the bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                w = int(detection[2] * frame.shape[1])
                h = int(detection[3] * frame.shape[0])
                x = int(center_x - w/2)
                y = int(center_y - h/2)


                # label = classes[class_id]
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                
                # Store the object coordinates
                # object_coords[label] = (center_x, center_y)

    # Apply non-maximum suppression to remove overlapping bounding boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw the bounding boxes and class labels on the frame
    for i in indices:
        # i = i[0]
        x, y, w, h = boxes[i]
        label = classes[class_ids[i]]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Draw circle in the center of the bounding box
        x2 = x + int(w/2)
        y2 = y + int(h/2)
        cv2.circle(frame,(x2,y2),4,(0,255,0),-1)
        
        # Calculate the center of the bounding box in centimeter coordinates
        # instead of pixel coordinates
        x2_cm = x2 * CM_TO_PIXEL
        y2_cm = y2 * CM_TO_PIXEL

        # text = "x: " + str(x2_cm) + ", y: " + str(y2_cm)
    
        
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # print(label,x2_cm,y2_cm)

        # Add object coordinates to dictionary
        if label not in object_coords:
            object_coords[label] = {"coords": (x2_cm, y2_cm)}
        else:
            object_coords[label]["coords"] = (x2_cm, y2_cm)

    
    # Display the frame
    cv2.imshow("Object Detection", frame)

    # print(boxes)
    # print(confidences)
    # print(class_ids)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()

# print(x2_cm,y2_cm)
# print(object_coords[label]["coords"])


# print(object_coords)


# print(object_coords['person']["coords"])

# Print the value of x2_cm
# print(x2_cm)
# print("x2_cm:", x2_cm)

# print(object_coords['person']["coords"])


# working
# print(object_coords['person']['coords'][0])
# print(object_coords['person']['coords'][1])
# print(object_coords['chair']['coords'][0])
# print(object_coords['chair']['coords'][1])
