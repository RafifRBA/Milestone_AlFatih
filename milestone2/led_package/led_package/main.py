import time
import sys
import serial

PORT = "/dev/ttyUSB0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

def main():
    if len(sys.argv) < 2:
        print("salah bang...")
        return
    
    status = sys.argv[1]
    status = status.lower()

    if status == "on":
        status = "1\n"
        ser.write(status.encode())
        print("LED menyala")
    elif status == "off":
        status = "0\n"
        ser.write(status.encode())
        print("LED mati")

if __name__ == "__main__":
    main()