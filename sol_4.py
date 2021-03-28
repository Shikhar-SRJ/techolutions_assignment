import serial

# No need to set baudrate as default baudrate is 9600
# ser1 = serial.Serial('COM1', 9600)

ser1 = serial.Serial('COM1')
ser2 = serial.Serial('COM3')

# Reading data 
d1 = ser1.read()
d2 = ser2.read()


