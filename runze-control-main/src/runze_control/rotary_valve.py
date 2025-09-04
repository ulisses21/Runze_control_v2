"""Rotary Valve driver"""
from __future__ import annotations
from runze_control.protocol import Protocol
from runze_control.runze_protocol import ReplyStatus
from runze_control.runze_device import RunzeDevice
from runze_control.protocol_codes import rotary_valve_codes
from typing import Union


class RotaryValve(RunzeDevice):

    def __init__(self, com_port: str, baudrate: int = None, address: int = 0x31,
                 protocol: Union[str, Protocol] = Protocol.RUNZE,
                 position_count: int = None, position_map: dict = None):
        # Pass along unused kwargs to satisfy diamond inheritance.
        super().__init__(com_port=com_port, baudrate=baudrate,
                         address=address, protocol=protocol)
        self.codes = rotary_valve_codes
        self.position_count = position_count
        self.position_map = position_map
    
    def get_motor_status(self):
        self.log.debug("Querying motor status.")
        reply = self._send_common_cmd_runze(self.codes.CommonCmd.GetMotorStatus)
        return reply['parameter']

    def move_clockwise_to_position(self, position: Union[str, int]):
        if not (1<= position<= 10):
            raise ValueError("Position must be between 1 and 10")
        #parameter of move clockwive is desired positon + 1 and desire position 
        param= ((position+1)<<8)| position
        return self._send_common_cmd_runze(self.codes.RotaryValveCommonCmd.MoveToPort, param)
    
    def move_counterclockwise_to_position(self, position: Union[str, int]):
        if not (1<= position<= 10):
            raise ValueError("Position must be between 1 and 10")
        #parameter of move clockwive is desired positon + 1 and desire position 
        param= ((position-1)<<8)| position
        return self._send_common_cmd_runze(self.codes.RotaryValveCommonCmd.MoveToPort, param)
    
    def get_Port_position(self):
        self.log.debug("Querying Port position.")
        reply = self._send_common_cmd_runze(self.codes.CommonCmd.GetPortPositon)
        return reply['parameter']
