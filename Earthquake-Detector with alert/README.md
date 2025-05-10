# Earthquake Detector with Email Alert using Arduino and Python

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
- Computer running python

---

## Working

This Earthquake Detector project is designed to detect seismic activity using the ADXL335 accelerometer and alert the user through visual, audible, and remote notifications.

### Step-by-Step Working:

1. The *Arduino* continuously reads analog data from the *ADXL335 accelerometer* across the X, Y, and Z axes.

2. It calculates the *magnitude of vibration* using the formula:

   magnitude = sqrt(X^2 + Y^2 + Z^2)

3. If the calculated magnitude exceeds a predefined *threshold value* (indicating a potential earthquake or strong vibration):

- The *LED* starts blinking to provide a visual alert.
- The *buzzer* sounds to provide an audible alert.
- A *Serial message* is sent containing the magnitude value.

4. A *Python script*, running on a connected PC, reads the Serial data from the Arduino.

5. When the script detects that the threshold has been crossed, it sends an *email alert* to a predefined email address. The email includes the *detected magnitude* of the vibration.

This multi-level alert system ensures that both local (LED and buzzer) and remote (email notification) alerts are activated in the event of seismic activity.

---

## Setup Instructions

### 1. Install Python & pip

Ensure Python and pip are installed on your system. If not, follow these steps:

- *Windows*: Download and install Python from [python.org](https://www.python.org/downloads/).
- *Linux/Mac*: Use the following command to install pip (if not already installed):
  ```bash
  sudo apt install python3-pip   # For Ubuntu/Linux

### 2. Install Required Libraries

Run the following command to install the necessary Python libraries for sending email alerts:

pip install smtplib

### 3. Circuit Connections

ADXL335 Accelerometer:

VCC → 5V on Arduino

GND → GND on Arduino

X, Y, Z pins → Analog pins A0, A1, A2 on Arduino (for vibration detection)


LED:

Anode (long pin) → Digital pin 13 on Arduino

Cathode (short pin) → 220-ohm Resistor → GND on Arduino


Buzzer:

Positive (longer pin) → Digital pin 12 on Arduino

Negative (shorter pin) → GND on Arduino


You can refer to the circuit diagram for a more detailed illustration of the wiring.

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
