# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def hex_bug(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    assert dut.state.value == 1,f"state = {dut.state.value}!=1.So there is a bug in the design."  
    dut.reset.value = 0
    await FallingEdge(dut.clk)


 