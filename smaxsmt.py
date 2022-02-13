#!/usr/bin/python3
#
#
from pymodbus.client.sync import ModbusTcpClient


class _Reg:
    def __init__(self, name, reg, postfix="", scale=1.0):
        self.name = name
        self.postfix = postfix
        self.scale = scale
        if "/" not in reg:
            reg += "/1"
        li = reg.split("/", maxsplit=2)
        self.reg = int(li[0])
        self.count = int(li[1])

    def output(self, mc):
        reg = mc.read_holding_registers(self.reg, count=self.count, unit=1)
        if len(reg.registers) == 1:
            val = reg.registers[0]
        elif len(reg.registers) == 2:
            val = reg.registers[0] * 65535 + reg.registers[1]
        else:
            raise Exception("unknown register {}".format(reg))
        return RegValue(val / self.scale, self.name, self.postfix)


class RegValue(float):
    def __new__(cls, value, name, postfix):
        return super().__new__(cls, value)

    def __init__(self, value, name, unit):
        self.value = value
        self.name = name
        self.unit = unit

    def __str__(self):
        return "{}: {:2.2f} {}".format(self.name, self.value, self.unit)


class ModbusConnectionError(Exception):
    pass


class SolarmaxSmt:
    def __init__(self, host):
        self._host = host

    def _get(self, reg):
        mc = ModbusTcpClient(self._host)
        res = mc.connect()
        if not res:
            raise ModbusConnectionError("cannot connect to {}".format(self._host))
        val = reg.output(mc)
        mc.close()
        return val

    @property
    def current_power(self):
        reg = _Reg("Current power", "4151/2", "kW", scale=10000)
        return self._get(reg)

    @property
    def max_power_today(self):
        reg = _Reg("Max power today", "4155/2", "kW", scale=10000)
        return self._get(reg)

    @property
    def total_power_today(self):
        reg = _Reg("Total power today", "4133/2", "kW")
        return self._get(reg)

    @property
    def total_power(self):
        reg = _Reg("Total power", "4129/2", "kW")
        return self._get(reg)

    @property
    def converter_temperature(self):
        reg = _Reg("Internal converter temperature", "4124/1", "°C")
        return self._get(reg)

    # XXX: improve API
    @property
    def voltage_1(self):
        reg = _Reg("Internal converter temperature", "4124/1", "°C")
        return self._get(reg)

    @property
    def current_1(self):
        reg = _Reg("Current 1", "4113", "A", scale=100.0)
        return self._get(reg)

    @property
    def power_1(self):
        reg = _Reg("Power 1", "4115", "kW", scale=10000.0)
        return self._get(reg)

    @property
    def voltage_2(self):
        reg = _Reg("Voltage 2", "4116", "V", scale=10.0)
        return self._get(reg)

    @property
    def current_2(self):
        reg = _Reg("Current 2", "4117", "A", scale=100.0)
        return self._get(reg)

    @property
    def power_2(self):
        reg = _Reg("Power 2", "4119", "kW", scale=10000.0)
        return self._get(reg)
