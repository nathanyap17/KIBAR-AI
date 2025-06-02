import cv2 
from ultralytics import YOLO
import serial
import time

# Load the YOLOv11 model
model_path = "KIBAR-AI.pt"  # Update with the actual local path to the model
model = YOLO(model_path)  # Load the model

# Define the classes
classes = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  
    'Hello', 'IloveYou', 'No', 'Please', 'Thanks', 'Yes'
]

# Arduino serial connection
arduino_port = "COM9"  # Update this to the correct port
baud_rate = 115200
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)

# Function to send index to Arduino
def send_to_arduino(word):
    """
    Sends a word to the Arduino one character at a time.
    """
    for letter in word:
        arduino.write(letter.encode())  # Send character
        print(f"Sending to Arduino: {letter}")
        time.sleep(0.5)  # Reduced delay for responsiveness
    
# Track the last detected class
last_detected_class = None

# Access the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    # Perform detection
    results = model(frame)

    # Parse detections
    detected_class = None
    for result in results:
        for box in result.boxes:
            confidence = box.conf[0].item()
            class_id = int(box.cls[0].item())

            if confidence > 0.5:  # Confidence threshold
                detected_class = class_id  # Update detected class
                label = f"{classes[class_id]}: {confidence:.2f}"
                x1, y1, x2, y2 = box.xyxy[0].int().tolist()
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                break  # Process only the first detection per frame

    # Send to Arduino if a new detection occurs
    if detected_class is not None and detected_class != last_detected_class:
        print(f"Detected class: {classes[detected_class]}")
        send_to_arduino(classes[detected_class])
        last_detected_class = detected_class

    # Reset the detection state if nothing is detected
    if detected_class is None:
        last_detected_class = None

    # Display the frame with detections
    cv2.imshow("YOLOv11 Real-Time Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Add a small delay
    time.sleep(0.1)

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()
