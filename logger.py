from time import sleep, strftime, time
import matplotlib.pyplot as plt
import os
import csv

x = []
y = []

def sensor1():
    for i in os.listdir("/sys/bus/w1/devices"):
        if i == "28-01183085f3ff":
            outsidesensor = i
    return outsidesensor

def sensor2():
    for j in os.listdir("/sys/bus/w1/devices"):
        if j == "28-01183087f8ff":
            outsidesensor = j
    return outsidesensor

def read(insidesensor):
    location = "/sys/bus/w1/devices/" + insidesensor + "/w1_slave"
    file = open(location)
    text = file.read()
    file.close()
    temperatureline = text.split("\n")[1]
    temperaturedata = temperatureline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    return celsius

def read(outsidesensor):
    location = "/sys/bus/w1/devices/" + outsidesensor + "/w1_slave"
    file = open(location)
    text = file.read()
    file.close()
    temperatureline = text.split("\n")[1]
    temperaturedata = temperatureline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    return celsius

def outsideTemperature(outsidesensor):
    with open ("outside_temp.csv", "a") as logging:
        temp = read(outsidesensor)
        logging.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str("%0.1f" % temp)))

def insideTemperature(insidesensor):
    with open ("inside_temp.csv", "a") as logging:
        temp = read(insidesensor)
        logging.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str("%0.1f" % temp)))

# Work in progress
def graph():
    with open ("outside_temp.csv", "r") as outcsvfile:
        plots = csv.reader(outcsvfile, delimiter=",")
        for row in plots:
            x.append(str(row[0]))
            y.append(float(row[1]))
    
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.title("")
    plt.legend()
    plt.savefig("temp.png")

if __name__ == '__main__':
    s1 = sensor1()
    s2 = sensor2()
    insideTemperature(s1)
    outsideTemperature(s2)
    graph()
