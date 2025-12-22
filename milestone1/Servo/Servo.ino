#include <ESP32Servo.h>

Servo servo;
const int SERVO_PIN = 18;
const int MIN_ANGLE = 0;
const int MAX_ANGLE = 180;

void setup() {
  Serial.begin(115200);
  while (!Serial);
  
  servo.attach(SERVO_PIN);
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();
    
    while (Serial.available() > 0) {
      Serial.read();
    }
    
    if (angle >= MIN_ANGLE && angle <= MAX_ANGLE) {
      servo.write(angle);
      Serial.print("Servo bergerak ke: ");
      Serial.print(angle);
      Serial.println("°");
    } else {
      Serial.println("Error: Sudut harus 0-180!");
    }
  }
}
