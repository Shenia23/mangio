import argparse
from collections import defaultdict
from bluepy.btle import Scanner, Peripheral, DefaultDelegate, ADDR_TYPE_RANDOM, BTLEException
import datetime
from  app.ReverseMiScale.scale import Scale
from  app.ReverseMiScale.constants import AD_TYPES, UNITS

from  app.ReverseMiScale.body_metrics import bodyMetrics

class ScanDelegate(DefaultDelegate):
    def __init__(self,height, mac_addr, callback, send_only_stabilized_weight):
        DefaultDelegate.__init__(self)
        self.height = height
        self.mac_addr = mac_addr
        self.callback = callback
        self.send_only_stabilized_weight = send_only_stabilized_weight
        self.last_rawData = defaultdict(str)


    def handleData(self, scale):
        # MiScale Raw Data Schema
        # +------+------------------------+
        # | byte |        function        |
        # +------+------------------------+
        # | 0    | Bit 0: unknown         |
        # |      | Bit 1: kg              |
        # |      | Bit 2: lbs             |
        # |      | Bit 3: unknown         |
        # |      | Bit 4: jin unit        |
        # |      | Bit 5: stabilized      |
        # |      | Bit 6: unknown         |
        # |      | Bit 7: load removed    |
        # +------+------------------------+
        # | 1-2  | weight (little endian) |
        # +------+------------------------+
        # | 3-7  | unknown                |
        # +------+------------------------+
        # | 8-9  | sequence (big endian)  |
        # +------+------------------------+

        # Check for duplicate packet
        if scale.rawData == self.last_rawData[scale.address]: return
        
        # Update duplication lookup table
        self.last_rawData[scale.address] = scale.rawData

        scale.isStabilized = (scale.rawData[0] & (1<<5)) != 0
        scale.loadRemoved = (scale.rawData[0] & (1<<7)) != 0

        scale.sequence = int.from_bytes(scale.rawData[8:10], byteorder='big')

        # Unit
        if (scale.rawData[0] & (1<<4)) != 0: # Chinese Catty
            scale.unit = UNITS.JIN
        elif (scale.rawData[0] & (1<<2)) != 0: # Imperial pound
            scale.unit = UNITS.LBS
        elif (scale.rawData[0] & (1<<1)) != 0: # MKS kg
            scale.unit = UNITS.KG
        else:
            scale.unit = UNITS.UNKNOWN

        # Callback
        if self.send_only_stabilized_weight:
            if scale.isStabilized:
                self.callback(scale)
        else:
            self.callback(scale)


    def getScaleInfo(self, dev):
        global flag_data
        global scale

        scale = Scale(address=dev.addr)
        
        for (adtype, desc, data) in dev.getScanData():
            if adtype == AD_TYPES.SERVICE_DATA:
                print("VALUE: ",data)

                if data.startswith('1b18'):
                    data2 = bytes.fromhex(data[4:])
                    ctrlByte1 = data2[1]
                    isStabilized = ctrlByte1 & (1 << 5)
                    hasImpedance = ctrlByte1 & (1 << 1)

                    measunit = data[4:6]
                    measured = int((data[28:30] + data[26:28]), 16) * 0.01
                    unit = ''
                    if measunit == "03":
                        unit = 'lbs'
                    if measunit == "02":
                        unit = 'kg'
                        measured = measured / 2
                    miimpedance = str(int((data[24:26] + data[22:24]), 16))

                    print("IMPEDANCIA:", int(miimpedance))

                    lib = bodyMetrics(measured, self.height, 21, "male", int(miimpedance))
                    bodyscale = ['Obese', 'Overweight', 'Thick-set', 'Lack-exerscise', 'Balanced',
                                'Balanced-muscular', 'Skinny', 'Balanced-skinny', 'Skinny-muscular']
                    message=""
                    message += ',"lean_body_mass":' + \
                        "{:.2f}".format(lib.getLBMCoefficient())
                    message += ',"body_fat":' + "{:.2f}".format(lib.getFatPercentage())
                    message += ',"water":' + "{:.2f}".format(lib.getWaterPercentage())
                    message += ',"bone_mass":' + "{:.2f}".format(lib.getBoneMass())
                    message += ',"muscle_mass":' + "{:.2f}".format(lib.getMuscleMass())
                    message += ',"protein":' + \
                        "{:.2f}".format(lib.getProteinPercentage())
                    message += ',"body_type":"' + \
                        str(bodyscale[lib.getBodyType()]) + '"'
                    message += ',"metabolic_age":' + \
                        "{:.0f}".format(lib.getMetabolicAge())
                    message += '}'
                    

                scale.UUID = bytes.fromhex(data[0:4])[::-1].hex()
                scale.rawData = bytes.fromhex(data[4:])
                scale.height = self.height
                scale.body_fat = lib.getFatPercentage()
                scale.water =lib.getWaterPercentage()
                scale.bone_mass = lib.getBoneMass()
                scale.muscle_mass = lib.getMuscleMass()
                scale.proteine = lib.getProteinPercentage()
                scale.body_type = str(bodyscale[lib.getBodyType()])
                scale.metab_age = lib.getMetabolicAge()
                scale.lean_mass = lib.getLBMCoefficient()
                scale.weight = measured
                scale.impedance = int(miimpedance)
                scale.bmi = lib.getBMI()
                scale.metab_basal = lib.getBMR()
                scale.visceral_fat = lib.getVisceralFat()


                if int(scale.impedance) in range(1,1000):
                    print("MESSAGE = ",message)
                    flag_data = True


            elif adtype == AD_TYPES.MANIFACTURER:
                scale.manufacturerData = bytes.fromhex(data)
        return scale


    def handleDiscovery(self, dev, isNewDev, isNewData):
        if self.mac_addr:
            if dev.addr.upper() == self.mac_addr:
                self.handleData(self.getScaleInfo(dev))
        else:
            for (adtype, desc, value) in dev.getScanData():
                if adtype == AD_TYPES.COMPLETE_LOCAL_NAME and value == "MI_SCALE":
                        self.handleData(self.getScaleInfo(dev))

def MiScale(height,mac_addr, callback, send_only_stabilized_weight):
    global scale
    global flag_data 
    flag_data = False
    mac_addr = mac_addr.upper()
    scanner = Scanner().withDelegate(ScanDelegate(height, mac_addr, callback, send_only_stabilized_weight))
    while flag_data == False:
        scanner.start()
        scanner.process(1)
        scanner.stop()
    return scale

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display Xiaomi scale data.')
    parser.add_argument("-a", "--address", help="The specific scale MAC address to retreive data. If not provided, match any Xiaomi scale")
    parser.add_argument("-s", "--stabilized", action="store_true", help="Send only data when the weight is stabilized")
    args = parser.parse_args()

    # When called from console, print directly the scale data
    MiScale(args.address, print, args.stabilized)
