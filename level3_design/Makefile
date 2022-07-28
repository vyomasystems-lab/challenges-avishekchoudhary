# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/hex_keypad_design.v               # provide your design path

TOPLEVEL :=  Hex_Keypad_Grayhill_072        # design file
MODULE   :=  testbench_hex_keypad   # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
