import serial
import time

PORT = "/dev/ttyUSB0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

def set_angle(degree):
    str_degree = f"{degree}\n"
    ser.write(str_degree.encode())

try:
    while True:
        degree = input("Masukkan sudut: ")
        set_angle(degree)
        time.sleep(2)

except KeyboardInterrupt:
    print("Keluar ...")
    
finally:
    ser.close()