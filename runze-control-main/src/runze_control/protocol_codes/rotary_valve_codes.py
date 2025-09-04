"""Protocol codes exclusive to SV-04 Selector Valve."""
from enum import IntEnum
from itertools import chain
from runze_control.protocol_codes.common_codes import CommonCmd as RunzeCommonCmd


class RotaryValveCommonCmd(IntEnum):
  """Runze Protocol codes shared between Rotary Valves to issue
    when querying/specifying the states of various settings via a
    Common Command frame. Codes common to all devices are part of
    runze_protocol_codes.CommonCmdCode
  """
  # Queries
  GetMotorStatus = 0x4A 
  GetPortPositon = 0x3E #current channel(port) position
    
  # Commands
  MoveToPort = 0xA4 #Run to port position
  MoveBetweenPort = 0xB4 #Run in between specified ports 
  ResetvalvePosition = 0x45  # Move Valve to start position
  ForceStop = 0x49
  

# FIXME: we should be doing dict-like updates here so that later cmds with
#   the same name overwrite the previous cmd since we are building these
#   containers of codes general-to-specific.
# Combine enums
# https://stackoverflow.com/a/41807919/3312269
CommonCmd = IntEnum('CommonCmd',
                    [(i.name, i.value) for i in chain(RunzeCommonCmd, RotaryValveCommonCmd)])
