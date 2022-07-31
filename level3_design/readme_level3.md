# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
*Make sure to include the Gitpod id in the screenshot*

![gitpod_id](https://user-images.githubusercontent.com/56909326/181591993-80b70ef5-2b40-45d7-9438-289830793176.png)



## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Hex Keypad here) which takes in 4 inputs  and gives 3 outputs.

1.The values are assigned to the input port using 
```
dut.reset.value = 1

```
The assert statement is used for comparing the Keypad's output to the expected value.

The following error is seen:
```
 assert dut.state.value == 1,f"state = {dut.state.value}!=1.So there is a bug in the design."
                     AssertionError: state = 000010!=1.So there is a bug in the design.
                     
```

## Test Scenario **(1)**
- Test Inputs: reset=1 
- Expected Output: state = 1 or 000001
- Observed Output in the DUT dut.state.value=000010

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 1
Based on the above test input and analysing the design, we see the following

```
  always @(posedge clk or posedge reset)
    if (reset) state <= S_1; == bug
    else state <= next_state;

```
For the Hex_keypad design, the state should be ```S_0 i.e 000001``` instead of ```8'S_1 i.e 000010``` as in the design code.


## Verification Strategy
In this I just reviewed the code thoroughly and found a bug then using appropriate testcase i exposed it.

## Is the verification complete ?
No, the Verfication is incomplete as i used brute force technique to expose bug, I have not used random testing.
