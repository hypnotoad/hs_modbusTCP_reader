# coding: utf-8

import pymodbus  # To not delete this module reference!!
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Hs_modbusTCP_fetcher14184(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hs_modbusTCP_fetcher14184")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_SWITCH=1
        self.PIN_I_FETCH_INTERVAL=2
        self.PIN_I_MAN_TRIGGER=3
        self.PIN_I_MODBUS_SLAVE_IP=4
        self.PIN_I_PORT=5
        self.PIN_I_SLAVE_ID=6
        self.PIN_I_MODBUS_WORDORDER=7
        self.PIN_I_MODBUS_BYTEORDER=8
        self.PIN_I_HOLDING_REGISTER1=9
        self.PIN_I_HR1_DATATYPE=10
        self.PIN_I_HR1_STR_LEN=11
        self.PIN_I_HOLDING_REGISTER2=12
        self.PIN_I_HR2_DATATYPE=13
        self.PIN_I_HR2_STR_LEN=14
        self.PIN_I_HOLDING_REGISTER3=15
        self.PIN_I_HR3_DATATYPE=16
        self.PIN_I_HR3_STR_LEN=17
        self.PIN_I_HOLDING_REGISTER4=18
        self.PIN_I_HR4_DATATYPE=19
        self.PIN_I_HR4_STR_LEN=20
        self.PIN_I_HOLDING_REGISTER5=21
        self.PIN_I_HR5_DATATYPE=22
        self.PIN_I_HR5_STR_LEN=23
        self.PIN_I_HOLDING_REGISTER6=24
        self.PIN_I_HR6_DATATYPE=25
        self.PIN_I_HR6_STR_LEN=26
        self.PIN_I_HOLDING_REGISTER7=27
        self.PIN_I_HR7_DATATYPE=28
        self.PIN_I_HR7_STR_LEN=29
        self.PIN_I_HOLDING_REGISTER8=30
        self.PIN_I_HR8_DATATYPE=31
        self.PIN_I_HR8_STR_LEN=32
        self.PIN_O_HR1_VAL_NUM=1
        self.PIN_O_HR1_VAL_STR=2
        self.PIN_O_HR2_VAL_NUM=3
        self.PIN_O_HR2_VAL_STR=4
        self.PIN_O_HR3_VAL_NUM=5
        self.PIN_O_HR3_VAL_STR=6
        self.PIN_O_HR4_VAL_NUM=7
        self.PIN_O_HR4_VAL_STR=8
        self.PIN_O_HR5_VAL_NUM=9
        self.PIN_O_HR5_VAL_STR=10
        self.PIN_O_HR6_VAL_NUM=11
        self.PIN_O_HR6_VAL_STR=12
        self.PIN_O_HR7_VAL_NUM=13
        self.PIN_O_HR7_VAL_STR=14
        self.PIN_O_HR8_VAL_NUM=15
        self.PIN_O_HR8_VAL_STR=16
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

        self.DEBUG = self.FRAMEWORK.create_debug_section()
        self.interval = None
        self.client = None
        self.data_types = {
            'int8': {'size': 1, 'numeric': True, 'method': 'decode_8bit_int'},
            'uint8': {'size': 1, 'numeric': True, 'method': 'decode_8bit_uint'},
            'int16': {'size': 1, 'numeric': True, 'method': 'decode_16bit_int'},
            'uint16': {'size': 1, 'numeric': True, 'method': 'decode_16bit_uint'},
            'int32': {'size': 2, 'numeric': True, 'method': 'decode_32bit_int'},
            'uint32': {'size': 2, 'numeric': True, 'method': 'decode_32bit_uint'},
            'int64': {'size': 4, 'numeric': True, 'method': 'decode_64bit_int'},
            'uint64': {'size': 4, 'numeric': True, 'method': 'decode_64bit_uint'},
            # 'float16': {'size': 2, 'numeric': True, 'method': 'decode_16bit_float'}, Doesn't work with python 2
            'float32': {'size': 2, 'numeric': True, 'method': 'decode_32bit_float'},
            'float64': {'size': 4, 'numeric': True, 'method': 'decode_64bit_float'},
            'string': {'size': -1, 'numeric': False, 'method': 'decode_string'}
        }

    def on_interval(self):

        ip_address = str(self._get_input_value(self.PIN_I_MODBUS_SLAVE_IP))
        port = int(self._get_input_value(self.PIN_I_PORT))
        unit_id = int(self._get_input_value(self.PIN_I_SLAVE_ID))

        try:
            self.DEBUG.set_value("Conn IP:Port (UnitID)", ip_address + ":" + str(port) + " (" + str(unit_id) + ") ")
            if self.client is None:
                self.client = ModbusTcpClient(ip_address, port)
            if self.client.is_socket_open() is False:
                self.client.connect()

            self.fetch_register(1, self.PIN_I_HOLDING_REGISTER1, self.PIN_I_HR1_DATATYPE, self.PIN_I_HR1_STR_LEN,
                                self.PIN_O_HR1_VAL_NUM, self.PIN_O_HR1_VAL_STR, unit_id)
            self.fetch_register(2, self.PIN_I_HOLDING_REGISTER2, self.PIN_I_HR2_DATATYPE, self.PIN_I_HR2_STR_LEN,
                                self.PIN_O_HR2_VAL_NUM, self.PIN_O_HR2_VAL_STR, unit_id)
            self.fetch_register(3, self.PIN_I_HOLDING_REGISTER3, self.PIN_I_HR3_DATATYPE, self.PIN_I_HR3_STR_LEN,
                                self.PIN_O_HR3_VAL_NUM, self.PIN_O_HR3_VAL_STR, unit_id)
            self.fetch_register(4, self.PIN_I_HOLDING_REGISTER4, self.PIN_I_HR4_DATATYPE, self.PIN_I_HR4_STR_LEN,
                                self.PIN_O_HR4_VAL_NUM, self.PIN_O_HR4_VAL_STR, unit_id)
            self.fetch_register(5, self.PIN_I_HOLDING_REGISTER5, self.PIN_I_HR5_DATATYPE, self.PIN_I_HR5_STR_LEN,
                                self.PIN_O_HR5_VAL_NUM, self.PIN_O_HR5_VAL_STR, unit_id)
            self.fetch_register(6, self.PIN_I_HOLDING_REGISTER6, self.PIN_I_HR6_DATATYPE, self.PIN_I_HR6_STR_LEN,
                                self.PIN_O_HR6_VAL_NUM, self.PIN_O_HR6_VAL_STR, unit_id)
            self.fetch_register(7, self.PIN_I_HOLDING_REGISTER7, self.PIN_I_HR7_DATATYPE, self.PIN_I_HR7_STR_LEN,
                                self.PIN_O_HR7_VAL_NUM, self.PIN_O_HR7_VAL_STR, unit_id)
            self.fetch_register(8, self.PIN_I_HOLDING_REGISTER8, self.PIN_I_HR8_DATATYPE, self.PIN_I_HR8_STR_LEN,
                                self.PIN_O_HR8_VAL_NUM, self.PIN_O_HR8_VAL_STR, unit_id)

        except Exception as err:
            self.DEBUG.set_value("Last exception msg logged", "Message: " + err.message)

    def fetch_register(self, input_num, pin_input_addr_id, pin_input_type_id, pin_input_fetch_size_id,
                       pin_output_num_id, pin_output_str_id, unit_id):

        register_addr = int(self._get_input_value(pin_input_addr_id))
        if register_addr < 0:  # Skip: Neg. values skips register execution
            return None

        register_type_str = self._get_input_value(pin_input_type_id)
        register_settings = self.data_types.get(register_type_str)
        if register_settings is None:  # No matching type entry found. lets skip over
            self.DEBUG.set_value("No matching data type found: ",  register_settings)
            return None

        reg_fetch_size = int(register_settings.get('size'))
        if reg_fetch_size == -1:  # Strings have individual length
            reg_fetch_size = self._get_input_value(pin_input_fetch_size_id)

        result = self.client.read_holding_registers(register_addr, reg_fetch_size, unit=unit_id)
        decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=self.byte_order(),
                                                     wordorder=self.word_order())

        # Fetch values. Num-Values written in num and str output, Strings only as in str output.
        if register_settings.get('numeric') is True:
            value = eval('decoder.' + register_settings.get('method') + '()', {"decoder": decoder})
            self._set_output_value(pin_output_num_id, value)
        else:
            # Strings must fetched with individual length
            value = eval('decoder.' + register_settings.get('method') + '(' + str(reg_fetch_size) + ')',
                         {"decoder": decoder})

        self.DEBUG.set_value("Output value " + str(input_num) + " of type " + register_type_str, str(value))
        self._set_output_value(pin_output_str_id, str(value))

    def word_order(self):
        if int(self._get_input_value(self.PIN_I_MODBUS_WORDORDER)) == 1:
            return Endian.Big
        else:
            return Endian.Little

    def byte_order(self):
        if int(self._get_input_value(self.PIN_I_MODBUS_BYTEORDER)) == 1:
            return Endian.Big
        else:
            return Endian.Little

    def on_init(self):
        self.interval = self.FRAMEWORK.create_interval()
        if self._get_input_value(self.PIN_I_SWITCH) == 1:
            self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
            self.interval.start()

    def on_input_value(self, index, value):
        if index == self.PIN_I_SWITCH:
            self.interval.stop()
            if value == 1:
                self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
                self.interval.start()
        elif index == self.PIN_I_FETCH_INTERVAL:
            self.interval.stop()
            self.interval.set_interval(self._get_input_value(self.PIN_I_FETCH_INTERVAL) * 1000, self.on_interval)
            if self._get_input_value(self.PIN_I_SWITCH) == 1:
                self.interval.start()
        elif index == self.PIN_I_MAN_TRIGGER:
            self.interval()
