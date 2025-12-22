import serial
import time

PORT = "/dev/ttyUSB2"
# untuk teensy /dev/ttyACM*
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)  # Tunggu koneksi stabil

print("Membaca sensor VL53L0X...")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='replace').strip()
            if line:
                print("Diterima", line)

except KeyboardInterrupt:
    print("\nKeluar...")
finally:
    ser.close()

