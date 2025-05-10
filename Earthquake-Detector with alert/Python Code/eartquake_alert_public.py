import serial
import smtplib
import time
from email.mime.text import MIMEText

# Configure your email credentials
sender_email = "youremail@gmail.com"         # Replace with your Gmail
sender_password = "your password"          # App Password (not normal password)
receiver_email = "recieveremail@gmail.com"    # Receiver Email

# Setup serial port
ser = serial.Serial('COM10', 9600)  # Change COM port if needed
time.sleep(2)  # Give Arduino time to reset

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email Sent Successfully!")
    except Exception as e:
        print("Failed to send email:", e)

earthquake_active = False  # True if earthquake is happening
already_alerted = False    # To avoid multiple emails
current_magnitude = 0.0
current_advice = ""

last_alert_time = 0  # Save last time email was sent
alert_interval = 60  # 60 seconds gap between emails if earthquake is still happening

while True:
    if ser.in_waiting:
        data = ser.readline().decode().strip()
        print(data)

        if "Earthquake Detected!" in data:
            try:
                magnitude_text = data.split("Magnitude:")[1].strip()
                current_magnitude = float(magnitude_text)
                earthquake_active = True

            except Exception as e:
                print("Error reading magnitude:", e)

        elif any(keyword in data for keyword in ["Minor Earthquake", "Moderate Earthquake", "Strong Earthquake", "Severe Earthquake"]):
            current_advice = data

            current_time = time.time()

            if not already_alerted or (current_time - last_alert_time) > alert_interval:
                subject = f"Earthquake Alert!"
                body = f"Earthquake Detected!\nMagnitude: {current_magnitude}\nAdvice: {current_advice}\nStay Safe!"
                send_email(subject, body)
                already_alerted = True
                last_alert_time = current_time

        elif "No Earthquake" in data:
            if earthquake_active:
                subject = "Earthquake Ended"
                body = "The earthquake has ended. It is now safe.\nStay alert and take care!"
                send_email(subject, body)

                earthquake_active = False
                already_alerted = False  # Reset so next earthquake can send alerts
                current_magnitude = 0.0
                current_advice = ""