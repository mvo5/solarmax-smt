#!/usr/bin/python3

import unittest

from unittest.mock import patch

from pymodbus.client.sync import ModbusTcpClient

import smaxsmt


class ModbusApi(unittest.TestCase):
    def setUp(self):
        patcher = patch("smaxsmt.ModbusTcpClient", spec=ModbusTcpClient)
        self.addCleanup(patcher.stop)
        mock_modbus_client_class = patcher.start()
        self.mock_modbus_client = mock_modbus_client_class.return_value
        self.mock_modbus_client.connect.return_value = True
        self.mock_holding_registers = (
            self.mock_modbus_client.read_holding_registers.return_value
        )

    def test_current_power(self):
        self.mock_holding_registers.registers = [12000]
        smax = smaxsmt.SolarmaxSmt("example.com")
        self.assertEqual(smax.current_power, 1.2)
        self.assertEqual(str(smax.current_power), "Current power: 1.20 kW")
        self.assertEqual(self.mock_modbus_client.connect.called, True)
        self.assertEqual(self.mock_modbus_client.close.called, True)

    def test_max_power_today(self):
        self.mock_holding_registers.registers = [22000]
        smax = smaxsmt.SolarmaxSmt("example.com")
        self.assertEqual(smax.max_power_today, 2.2)
        self.assertEqual(str(smax.max_power_today), "Max power today: 2.20 kW")

    def test_total_power_today(self):
        self.mock_holding_registers.registers = [72]
        smax = smaxsmt.SolarmaxSmt("example.com")
        self.assertEqual(smax.total_power_today, 72)
        self.assertEqual(str(smax.total_power_today), "Total power today: 72.00 kW")

    def test_total_power(self):
        self.mock_holding_registers.registers = [7200]
        smax = smaxsmt.SolarmaxSmt("example.com")
        self.assertEqual(smax.total_power, 7200.0)
        self.assertEqual(str(smax.total_power), "Total power: 7200.00 kW")

    def test_converter_temperature(self):
        self.mock_holding_registers.registers = [45]
        smax = smaxsmt.SolarmaxSmt("example.com")
        self.assertEqual(smax.converter_temperature, 45.0)
        self.assertEqual(
            str(smax.converter_temperature), "Internal converter temperature: 45.00 °C"
        )
