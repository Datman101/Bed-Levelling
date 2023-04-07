import board
import busio
import Adafruit_ADS1x15
import os
import moonrakerpy as moonpy


printer = moonpy.MoonrakerPrinter("http://192.168.1.226")

def stringify(inp):
    string = "\t"
    for i in range(0, len(inp)):
        string+=str(inp[i])+", "
    return string

#i2c = busio.I2C(board.SCL, board.SDA)
#adc = Adafruit_ADS1x15.ADS1115()

found = False
count = 0
find = -1

x_vals = [30, 140, 230]
y_vals = [40, 150, 235]

vals = [[0 for j in range(3)] for i in range(3)]

for i in range(0, 3):
    for j in range(0, 3):
        gcode = "G0 X" + str(x_vals[i]) + " Y" + str(y_vals[j]) + " Z0\n"
        printer.send_gcode(gcode)
#       vals[i][j]  = adc.read_adc(0)
        vals[i][j] = 0.0



print(vals)

with open("/home/pi/printer_data/config/printer.cfg") as cfg:

    lines = cfg.readlines()

    for line in lines:
        if ("points" in line):
            find = line
    
    if(find != -1):

        val = int(lines.index(find))
        newval = lines[0:val+1] 
        newval.append(stringify(vals[0]) + "\n")
        newval.append(stringify(vals[1]) + "\n")
        newval.append(stringify(vals[2]) + "\n")
        newval += lines [val+8:-1]

cfg = open("/home/pi/printer_data/config/printer.cfg", "w")
cfg.writelines(newval)