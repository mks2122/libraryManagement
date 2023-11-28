# RFID Roll Number Writer

This project combines Flask, MQTT, and an RFID reader to enable the writing of roll numbers onto RFID cards using a web interface.

## Description

The project consists of two main components:

1. **Web Interface** (`web_interface/`): A Flask-based web application that provides a simple form for users to input roll numbers. Upon submission, it publishes the roll number via MQTT to a specific topic.

2. **RFID Writer** (`rfid_writer/`): A Python script that subscribes to the MQTT topic where roll numbers are published. Upon receiving a roll number, it writes the data onto an RFID card using an RFID reader.

## Components

### Web Interface

- **Flask App**: Handles user inputs via a simple web form.
- **MQTT Integration**: Publishes roll numbers to an MQTT topic for RFID writing.
- **HTML/CSS**: Provides a user-friendly interface to input roll numbers.

### RFID Writer

- **MQTT Subscriber**: Listens to the MQTT topic for incoming roll numbers.
- **RFID Reader Integration**: Writes received roll numbers onto RFID cards.

## Usage

1. Clone the repository.
2. Install required libraries for both the web interface and RFID writer.
3. Run the Flask application to start the web interface.
4. Execute the RFID writer script to listen for MQTT messages and write roll numbers to RFID cards.

## Installation

Flask Web Interface

  cd web_interface/
  pip install -r requirements.txt
  python app.py
  
RFID Writer

  cd rfid_writer/
  pip install -r requirements.txt
  python rfid_writer.py
Configuration
Ensure MQTT broker details are correctly configured in both components.
Adjust RFID reader settings if necessary.

Contributing
Contributions are welcome! Feel free to submit issues or pull requests for any enhancements or fixes.
