import gradio as gr
from pyzbar.pyzbar import decode
import cv2
import numpy as np
from PIL import Image
import requests
import json
import time
import os
# from cam import cameraIsbn
# from cam import qr_barcode_scanner

def qr_barcode_scanner(image, box_coords=None):
    # Convert PIL image to numpy array
    image_data = np.array(image)

    # Convert RGB to grayscale if needed
    if len(image_data.shape) == 3 and image_data.shape[2] == 3:
        image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2GRAY)

    # Define coordinates for the box
    if box_coords is not None:
        x, y, w, h = box_coords
        roi = image_data[y:y+h, x:x+w]  # Region of interest within the box
        decoded_objects = decode(roi)
    else:
        decoded_objects = decode(image_data)

    if len(decoded_objects) == 0:
        return "No QR code or barcode found."

    results = []
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        # results.append((obj.type, data))
        # print(data)

        return data

    # return "\n".join(results)

def cameraIsbn():
    cap = cv2.VideoCapture(0)
    c=0
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Infinite loop to capture frames
    while c<200:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Define the box coordinates (x, y, width, height)
        box_x, box_y, box_w, box_h = 100, 100, 500, 200  # Adjust these values as needed

        # Draw the box on the frame
        cv2.rectangle(frame, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 0, 0), 2)

        cv2.putText(frame, "Place the barcode inside the box", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
import cv2
from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image
global c
c=0
def qr_barcode_scanner(image, box_coords=None):
    # Convert PIL image to numpy array
    image_data = np.array(image)

    # Convert RGB to grayscale if needed
    if len(image_data.shape) == 3 and image_data.shape[2] == 3:
        image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2GRAY)

    # Define coordinates for the box
    if box_coords is not None:
        x, y, w, h = box_coords
        roi = image_data[y:y+h, x:x+w]  # Region of interest within the box
        decoded_objects = decode(roi)
    else:
        decoded_objects = decode(image_data)

    if len(decoded_objects) == 0:
        return "No QR code or barcode found."

    results = []
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        # results.append((obj.type, data))
        # print(data)

        return data

    # return "\n".join(results)

def cameraIsbn():
    cap = cv2.VideoCapture(0)
    c=0
    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Infinite loop to capture frames
    while c<200:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Define the box coordinates (x, y, width, height)
        box_x, box_y, box_w, box_h = 100, 100, 500, 200  # Adjust these values as needed

        # Draw the box on the frame
        cv2.rectangle(frame, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 0, 0), 2)

        cv2.putText(frame, "Place the barcode inside the box", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        # Display the frame
        cv2.imshow("Camera Feed", frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Perform QR code/barcode scanning only within the defined box
        a = qr_barcode_scanner(frame, box_coords=(box_x, box_y, box_w, box_h))

        # if c==200:
        #     return "abcde"
        if a != "No QR code or barcode found.":
            return a
            break
        else:
            c+=1
            print(a)
    return "abcde"
    # Release the camera and destroy all windows    
    cap.release()
    cv2.destroyAllWindows()
# cameraIsbn()
