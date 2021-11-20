from machine import Pin, I2C
import framebuf
from SSD1306 import SSD1306_I2C
import utime
import Font

pix_res_x = 128  # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

print("Initializing I2C ...")
i2c_bus = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)  # start I2C on I2C1 (GPIO 2/3) GROVE 2
print(i2c_bus)
print()
devices = i2c_bus.scan()  # scanning devices on bus

print("Devices on bus : ")
for i in devices:
    print("       {0:X}h".format(i))

print()
print("Initializing display ...")
oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_bus)
oled.fill(0)   # clear display
oled.contrast(6)  # set display contrast
oled.show()  # update display


print("Painting HELLO WORLD")
oled.text("HELLO WORLD",15,30)
oled.show()

utime.sleep(1)

print("Clearing display")
oled.hline(0, 0, 128, 1)
oled.show()

for y in range(1, 65):
    oled.hline(0, y - 1, 128, 0) 
    oled.hline(0, y, 128, 1)
    oled.show()

print("Painting font demo")
oled.text("8x8 framebuf", 0, 0, 1)

Font.PrintString(oled, "7x5 from Font", 0, 10, 1, 1)
Font.PrintString(oled, "double", 0, 20, 2, 1)
Font.PrintString(oled, "triple", 0, 38, 3, 1)

oled.show()

