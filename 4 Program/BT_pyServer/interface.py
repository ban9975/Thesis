import BT

class interface:
    def __init__(self):
        print("")
        print("Arduino Bluetooth Connect Program.")
        print("")
        self.ser = BT.bluetooth()
        # COM adi: 12, ban: 5
        while(not self.ser.do_connect("COM6")):
            self.ser.do_connect("COM6")
        self.write('0')

    def read(self):
        return self.ser.SerialReadInt()

    def end_process(self):
        self.ser.disconnect()

    def write(self, input):
        return self.ser.SerialWrite(input)