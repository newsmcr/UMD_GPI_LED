# UMD_GPI_LED
Pushbutton with 6 Buttons with LED plus UMD


These files allow you to control your Blackmagig Design Videohub Matrix with pasberry pi
gpio_6x1_RCP is controlling a single Output from Videomatrix by closing GPI contacts

LED_6_LED.py Diplays which Input is active with a LEDs connected at GPIO

UMD works with max7291 and displays Input Video Name on 8 8x8 LED
Board Pin	Name	Remarks	RPi Pin	RPi Function
connect: MAX7219 Matrix 
    1	VCC	+5V Power	    2	5V0
    2	GND	Ground	      6	GND
    3	DIN	Data In	      19	GPIO 10 (MOSI)
    4	CS	Chip Select	  24	GPIO 8 (SPI CE0)
    5	CLK	Clock	        23	GPIO 11 (SPI CLK)
    
    assign your inputs in config file
    
