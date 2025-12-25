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

    if(status == "start"):
        while True:
            masukan = input("Masukkan sudut (0-180): ")
            masukan = f"{masukan}\n"
            ser.write(masukan.encode())
            

if __name__ == "__main__":
    main()