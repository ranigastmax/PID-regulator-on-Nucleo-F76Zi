import serial
import csv
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.timeout = 1
try:
    ser.open()
    print("Serial port opened successfully.")
except Exception as e:
    print(f"Failed to open serial port: {e}")
    exit()
csv_file = "data.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Temperature (°C)"])
    print("Start reading data...")
    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                try:
                    temperature = float(line)
                    print(f"Temperature: {temperature}")
                    writer.writerow([temperature])
                except ValueError:
                    print(f"Malformed data: {line}")

    except KeyboardInterrupt:
        print("Data logging stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

ser.close()
print("Serial port closed.")
