# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
*Make sure to include the Gitpod id in the screenshot*

![181071537-0c9b8aa7-2d89-479d-bfc1-93128b5121ce](https://user-images.githubusercontent.com/56909326/181500609-fe88ba6f-7a68-43ca-a67a-08dc431fce89.png)



## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Mux module here) which takes in 5-bit and 2-bit inputs *sel* and *inp0-30* respectively and gives 2-bit output *out*

1.The values are assigned to the input port using 
```
dut.Col.value = 2

```
The assert statement is used for comparing the Detector's output to the expected value.

The following error is seen:
```
 assert dut.Code.value == 1,f"There is bug in the design because {dut.Code.value}!=2"
                     AssertionError: There is bug in the design because 0000!=2
                     
```

## Test Scenario **(1)**
- Test Inputs: Col=2 
- Expected Output: Code = 1 or 0001
- Observed Output in the DUT dut.Code.value=0000

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 1
Based on the above test input and analysing the design, we see the following

```
 always @ (Row or Col)
    case ({Row, Col})
        8'b0001_0001: Code = 0; 
        8'b0001_0001: Code = 1; ==>bug

```
For the Hex_keypad design, the case should be ```8'b0001_0010``` instead of ```8'b0001_0001``` as in the design code.


## Verification Strategy
In this I just reviewed the code thoroughly and found a bug then using appropriate testcase i exposed it.

## Is the verification complete ?
No, the Verfication is incomplete as i used brute force technique to expose bug, I have not used random testing.
