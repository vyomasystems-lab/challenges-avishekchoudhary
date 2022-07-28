# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
*Make sure to include the Gitpod id in the screenshot*

![gitpod_id](https://user-images.githubusercontent.com/56909326/181071537-0c9b8aa7-2d89-479d-bfc1-93128b5121ce.png)



## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Sequence Detector module here) which takes in 1-bit inputs *inp_bit,reset,clk* and gives 1-bit output *seq_seen*

1.The values are assigned to the input port using 
```
dut.inp_bit.value = 1

```
The assert statement is used for comparing the Detector's output to the expected value.

The following error is seen:
```
 assert dut.next_state.value == dut.SEQ_1.value,f"Design has a bug beause {dut.next_state.value} != {dut.SEQ_1.value}"
                     AssertionError: Design has a bug beause 000 != 1
                     
```

2.The values are assigned to the input port using 
```
dut.inp_bit.value = 0

```
The assert statement is used for comparing the Detector's output to the expected value.

The following error is seen:
```
 assert dut.next_state == dut.SEQ_10.value,f"Design has a bug {dut.next_state.value}!={dut.SEQ_10.value}"
                     AssertionError: Design has a bug 000!=2

```

3.The values are assigned to the input port using 
```
dut.inp_bit.value = 0

```
The assert statement is used for comparing the Detector's output to the expected value.

The following error is seen:
```
 assert dut.next_state == dut.SEQ_10.value,f"Design has a bug {dut.next_state.value}!={dut.SEQ_10.value}"
                     AssertionError: Design has a bug 000!=2

```
4.The values are assigned to the input port using 
```
dut.inp_bit.value = 1

```
The assert statement is used for comparing the Detector's output to the expected value.

The following error is seen:
```
 assert dut.next_state.value == dut.SEQ_1.value,f"Design has bug because {dut.next_state.value}!={dut.SEQ_1.value}"
                     AssertionError: Design has bug because 000!=1

```

## Test Scenario **(1)**
- Test Inputs: inp_bit=1 
- Expected Output: next_state=001,seq_seen=0
- Observed Output in the DUT dut.next_state.value=000

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 1
Based on the above test input and analysing the design, we see the following

```
 SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;
        else
          next_state = SEQ_10;
      end

```
For the Detector design, the case should be ```next_state=SEQ_1``` instead of ```next_state = IDLE``` as in the design code.

## Test Scenario **(2)**
- Test Inputs: inp_bit=0
- Expected Output: next_state=010,seq_seen=0
- Observed Output in the DUT dut.next_state=000

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 2
Based on the above test input and analysing the design, we see the following

```
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE; ==>bug
      end

```
For the Detector design, the case should be ```next_state=SEQ_10``` instead of ```next_state=IDLE```in the design code.

## Test Scenario **(3)**
- Test Inputs: inp_bit=0
- Expected Output: next_state=010,seq_seen=0
- Observed Output in the DUT dut.next_state=000

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 3
Based on the above test input and analysing the design, we see the following

```
SEQ_1011:
      begin
        next_state = IDLE; ==>bug
      end

```
For the Detector design, the case should be ```if(input ==1)begin next_state=SEQ_1 end else begin next_state=SEQ_1 end ``` instead of ```next_state=IDLE```in the design code.

## Test Scenario **(4)**
- Test Inputs: inp_bit=1
- Expected Output: next_state=001,seq_seen=0
- Observed Output in the DUT dut.next_state=000

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 4
Based on the above test input and analysing the design, we see the following

```
SEQ_1011:
      begin
        next_state = IDLE; ==>bug
      end

```
For the Detector design, the case should be ```if(input ==1)begin next_state=SEQ_1 end else begin next_state=SEQ_1 end ``` instead of ```next_state=IDLE```in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![bugs](https://user-images.githubusercontent.com/56909326/181071609-a9145987-8ffc-4b28-a26f-944f1c92b416.png)


The updated design is checked in as seq_detect_1011_corrected.v

## Verification Strategy
Firstly I designed the state diagram of the sequence detector and analysed the current and next states in code and I found bug  there.Then i wrote testbench targeted for exposing the bug.During This process i faced some issue like for same code the simulator/env was giving different outputs this is maybe due to internet connectivity issue or maybe due to some bug in simulator/env. 

## Is the verification complete ?
No, the Verfication is incomplete as i used brute force technique to expose bug, I have not used random testing.
