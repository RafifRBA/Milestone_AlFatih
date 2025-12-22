#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

void setup() {
  Serial.begin(115200);
  while (!Serial);

  Wire.begin();

  if (!sensor.init()) {
    Serial.println("Sensor VL53L0X gagal init!");
    while (1);
  }

  sensor.setTimeout(500);
  sensor.startContinuous();

  Serial.println("VL53L0X siap!");
}

void loop() {
  uint16_t distance = sensor.readRangeContinuousMillimeters();

  if (sensor.timeoutOccurred()) {
    Serial.println("Timeout!");
  } else {
    Serial.print("Jarak: ");
    Serial.print(distance/10);
    Serial.println(" cm");
  }

  delay(200);
}