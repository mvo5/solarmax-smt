#!/usr/bin/python3

from pyModbusTCP.client import ModbusClient


def int16_list_to_str(int16_list):
    res = ""
    for int16 in int16_list:
        b1 = (int16 >> 8) & 0xFF
        res += chr(b1)
        b2 = int16 & 0xFF
        res += chr(b2)
    return res


# some ideas from https://forum.fhem.de/index.php?topic=122419.0
# real vendor: Senergy
# possible other things to poke at:
# 6912/5 vendor
# 6672/8 software version
# 4125 - status
# 4131 - hours total
if __name__ == "__main__":
    host = "192.168.178.155"
    mc = ModbusClient(host, auto_open=True)
    res = mc.read_holding_registers(6912, 5)
    print("6912/5", res)
    print(int16_list_to_str(res))

    res = mc.read_holding_registers(6672, 8)
    print("6678/8", res)
    print(int16_list_to_str(res))

    res = mc.read_holding_registers(4125, 1)
    print(res)
    res = mc.read_holding_registers(4131, 1)
    print(res)
