# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state.value == dut.IDLE.value,f"Design has a bug beause {dut.next_state.value} != {dut.IDLE.value}"
    
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    assert dut.next_state.value == dut.SEQ_1.value,f"Design has a bug beause {dut.next_state.value} != {dut.SEQ_1.value}"
    


@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f" seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state.value == dut.SEQ_1.value,f"Design has a bug beause {dut.next_state.value} != {dut.SEQ_1.value}"

    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f"seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state.value == dut.IDLE.value,f"Design has a bug beause {dut.next_state.value} != {dut.IDLE.value}"

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")

    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f"seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    assert dut.next_state == dut.SEQ_10.value,f"Design has a bug {dut.next_state.value}!={dut.SEQ_10.value}"

@cocotb.test()
async def test_seq_bug3(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state.value == dut.SEQ_1.value,f"Design has a bug beause {dut.next_state.value} != {dut.SEQ_1.value}"

    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state.value == dut.IDLE.value,f"Design has a bug beause {dut.next_state.value} != {dut.IDLE.value}"

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state == dut.SEQ_10.value,f"Design has a bug because {dut.next_state.value}!={dut.SEQ_10.value}"

    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f"seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    assert dut.next_state.value == dut.SEQ_10.value,f"Design has bug because {dut.next_state.value}!={dut.SEQ_10}"


@cocotb.test()
async def test_seq_bug4(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state.value == dut.SEQ_1.value,f"Design has a bug beause {dut.next_state.value} != {dut.SEQ_1.value}"

    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state.value == dut.IDLE.value,f"Design has a bug beause {dut.next_state.value} != {dut.IDLE.value}"

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f" seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    # assert dut.next_state == dut.SEQ_10.value,f"Design has a bug because {dut.next_state.value}!={dut.SEQ_10.value}"

    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut._log.info(f"seq_seen={dut.seq_seen.value} curr_state={dut.current_state}  next_state={dut.next_state.value} input={dut.inp_bit.value}")
    assert dut.next_state.value == dut.SEQ_1.value,f"Design has bug because {dut.next_state.value}!={dut.SEQ_1.value}"
    