#define buzzer 12
#define led 13

#define x A0
#define y A1
#define z A2

int xsample = 0;
int ysample = 0;
int zsample = 0;

#define samples 9
#define threshold 3.0 // Minimum magnitude to detect earthquake

void setup() {
  Serial.begin(9600);        
  pinMode(buzzer, OUTPUT);
  pinMode(led, OUTPUT);

  // Calibration
  for (int i = 0; i < samples; i++) {
    xsample += analogRead(x);
    ysample += analogRead(y);
    zsample += analogRead(z);
    delay(10);
  }

  xsample /= samples;
  ysample /= samples;
  zsample /= samples;

  digitalWrite(buzzer, LOW);
  digitalWrite(led, LOW);

  Serial.println("Device Ready...");
}

void loop() {
  int value1 = analogRead(x);
  int value2 = analogRead(y);
  int value3 = analogRead(z);

  int xValue = xsample - value1;
  int yValue = ysample - value2;
  int zValue = zsample - value3;

  // Calculate magnitude
  float magnitude = sqrt((xValue * xValue) + (yValue * yValue) + (zValue * zValue));

  // Check if earthquake detected based on magnitude
  if (magnitude > threshold) {
    digitalWrite(buzzer, HIGH);

    // Fast LED blinking
    digitalWrite(led, HIGH);
    delay(100);
    digitalWrite(led, LOW);
    delay(100);

    Serial.print("Earthquake Detected! Magnitude: ");
    Serial.println(magnitude);

    // Send detailed alert for different magnitude ranges
    if (magnitude < 4.0) {
      Serial.println("Minor Earthquake - Stay alert, no need for evacuation.");
    }
    else if (magnitude >= 4.0 && magnitude < 6.0) {
      Serial.println("Moderate Earthquake - Stay inside, avoid windows and heavy objects.");
    }
    else if (magnitude >= 6.0 && magnitude < 7.5) {
      Serial.println("Strong Earthquake - Take cover under furniture, be ready to evacuate.");
    }
    else {
      Serial.println("Severe Earthquake - Stay indoors, protect your head and neck, follow evacuation orders.");
    }

  } else {
    digitalWrite(buzzer, LOW);
    digitalWrite(led, LOW);
    Serial.println("No Earthquake...");
    delay(500);  // Wait 500 ms before checking again
  }
}