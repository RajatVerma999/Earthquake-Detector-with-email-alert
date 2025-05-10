# Earthquake Detector using Arduino and Python

This project detects seismic activity using an ADXL335 accelerometer connected to an Arduino Uno. If vibration exceeds a threshold, an alarm is triggered and an email alert is sent using a Python script.

---

## Components Used

- Arduino Uno
- ADXL335 Accelerometer
- LED
- Buzzer
- Jumper Wires
- Breadboard
- 220-ohm resistor

---

## Working

The Arduino reads analog data from the ADXL335 sensor and checks for sudden changes in vibration. If a threshold is exceeded, it sends a signal through Serial. A Python script running on a PC reads this data and sends an email alert.

---

## Arduino Code

File: File: [Arduino Code/earthquake_detector.ino](Arduino%20Code/earthquake_detector.ino)

---

## Python Code

File: File: [Python Code/earthquake_alert_public.py](Python%20Code/earthquake_alert_public.py)

> Note: Replace "your_email@example.com" and "your_password" with your actual email credentials if you test it (use app password for Gmail).

---

## Setup Image
![Setup Image](./Setup%20Image/earthquake_detector_setup.jpg)



> Note: Image may not be very clear, but it shows the real project setup.

---

## Circuit Diagram
![Circuit Diagram](./Circuit%20Diagram/earthquake_detector_circuit.jpg)
---

## Future Scope

- Add cloud integration
- Use a GSM module for SMS alerts
- Visual dashboard with real-time graphing

---

## Author

Rajat Verma (2025)
