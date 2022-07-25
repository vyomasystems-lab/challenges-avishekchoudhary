# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux_inp12_inp13(dut):

    cocotb.log.info('#### CTB:Exposing Bug 1 ####')
    dut.inp12.value = 2
    dut.inp13.value = 1

    dut.sel.value=13

    await Timer(2,units='ns')
    dut._log.info(f"inp12={bin(dut.inp12.value)}  inp13={bin(dut.inp13.value)}  sel={bin(dut.sel.value)}")
    assert dut.out.value == dut.inp13.value,f'Mux result is incorrect: {bin(dut.out.value)} != {bin(dut.inp13.value)}'

@cocotb.test()
async def test_mux_inp30(dut):

    cocotb.log.info('#### CTB:Exposing Bug 2 ####')
    dut.inp30.value = 3
    dut.sel.value = 30

    await Timer(2,units='ns')
    dut._log.info(f"inp30={bin(dut.inp30.value)}  sel={bin(dut.sel.value)} out={dut.out.value}")
    assert dut.out.value == dut.inp30.value,f"Mux result is incorrect: {dut.out.value} != {dut.inp30.value}"

