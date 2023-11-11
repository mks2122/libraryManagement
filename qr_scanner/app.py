import gradio as gr
import cv2
from pyzbar.pyzbar import decode
import numpy as np
from PIL import Image

def qr_barcode_scanner(image):
    # Convert PIL image to numpy array
    image_data = np.array(image)

    # Convert RGB to grayscale if needed
    if len(image_data.shape) == 3 and image_data.shape[2] == 3:
        image_data = cv2.cvtColor(image_data, cv2.COLOR_RGB2GRAY)

    # Decode QR codes and barcodes
    decoded_objects = decode(image_data)

    if len(decoded_objects) == 0:
        return "No QR code or barcode found."

    results = []
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        results.append(f"Type: {obj.type}, Data: {data}")

    return "\n".join(results)

cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Infinite loop to capture frames
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    a=qr_barcode_scanner(frame)
    # print(qr_barcode_scanner(frame))

    if a!="No QR code or barcode found.":
        print(a)
        break
    else:
        print(a)

# Release the camera and destroy all windows    
cap.release()
cv2.destroyAllWindows()