#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '../lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_1in8_LCD import LCD_1in8
from waveshare_1in8_LCD import LCD_Config

from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

def main():
    LCD = LCD_1in8.LCD()

    Lcd_ScanDir = LCD_1in8.SCAN_DIR_DFT
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear(0xffff);
    image = Image.new("RGB", (LCD.LCD_Dis_Column, LCD.LCD_Dis_Page), "WHITE")
    draw = ImageDraw.Draw(image)
    font18 = ImageFont.truetype('../resources/Font.ttc', 18)
    draw = ImageDraw.Draw(image)
    image = Image.open('../resources/qr.bmp').resize((160,128))
    LCD.LCD_ShowImage(image)
    LCD_Config.Driver_Delay_ms(1500)
    draw = ImageDraw.Draw(image)
    draw.text((33, 12), 'Scan here: ', fill = "blue")
    LCD.LCD_ShowImage(image)
    LCD_Config.Driver_Delay_ms(1500)

try:
    if __name__ == '__main__':
        main()
except Exception as e:
   print(e)
