import serial
import matplotlib.pyplot as plt
import time

plt.ion()

ax_list = []
az_list = []
ay_list = []
counter = 0

ser = serial.Serial('COM3', 115200, timeout=0.1)

while True:
    cmd = input("[1] start pomiar: ")
    ser.write(cmd.encode())

    if cmd == '1':
        print("Pomiar... (Ctrl+C aby zatrzymać)")

        try:
            while True:
                data = ser.readline().decode().strip()

                if data:
                    print("RAW:", data)
 

                    try:
                        ax, az, ay = map(int, data.split())

                        ax_list.append(ax)
                        az_list.append(az)
                        ay_list.append(ay)

                        if len(ax_list) > 100:
                            ax_list.pop(0)
                            az_list.pop(0)
                            ay_list.pop(0)
                        counter += 1
                        if counter % 5 == 0: 
                            plt.clf()
                            plt.title("mag")
                            plt.plot(ax_list)
                            plt.plot(az_list)
                            plt.plot(ay_list)
                            plt.pause(0.1)

                    except:
                        print("Błąd danych:", data)
                time.sleep(0.02)

        except KeyboardInterrupt:
            print("\nSTOP")


            




