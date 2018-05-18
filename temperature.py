import os

def sensor1():
    for i in os.listdir("/sys/bus/w1/devices"):
        if i == "28-01183085f3ff":
            outsidesensor = i
    return outsidesensor

def sensor2():
    for j in os.listdir("/sys/bus/w1/devices"):
        if j == "28-01183087f8ff":
            insidesensor = j
    return insidesensor

def read(outsidesensor):
    location = "/sys/bus/w1/devices/" + outsidesensor + "/w1_slave"
    file = open(location)
    text = file.read()
    file.close()
    temperatureline = text.split("\n")[1]
    temperaturedata = temperatureline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    #farenheit = (celcius * 1.8) + 32
    return celsius

def read(insidesensor):
    location = "/sys/bus/w1/devices/" + insidesensor + "/w1_slave"
    file = open(location)
    text = file.read()
    file.close()
    temperatureline = text.split("\n")[1]
    temperaturedata = temperatureline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    #farenheit = (celcius * 1.8) + 32
    return celsius

def outsideTemperature(outsidesensor):
    if read(outsidesensor) != None:
        print("Temperature outside: %0.3f c" % read(outsidesensor))

def insideTemperature(insidesensor):
    if read(insidesensor) != None:
        print("Temperature inside: %0.3f c" % read(insidesensor))

def kill():
    quit()

if __name__ == '__main__':
    try:
        s1 = sensor1()
        s2 = sensor2()
        outsideTemperature(s1)
        insideTemperature(s2)
    except KeyboardInterrupt:
        kill()