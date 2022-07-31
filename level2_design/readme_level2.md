# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
*Make sure to include the Gitpod id in the screenshot*

![gitpod_id](https://user-images.githubusercontent.com/56909326/181591993-80b70ef5-2b40-45d7-9438-289830793176.png)



## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Bit Manipulation co-processor) which takes in 4 inputs  and gives 1 output.

1.The values are assigned to the input port using 
```
dut.mav_putvalue_src1.value = 0
dut.mav_putvalue_src2.value = 0
dut.mav_putvalue_src3.value = 2217
dut.mav_putvalue_instr.value = 16843019

```
The error statement is used for comparing the coprocessor's output to the expected value.

The following error is seen:
```
 Value mismatch DUT = 0x1152 does not match MODEL = 0x0
                     
```

## Test Scenario **(1)**
- Test Inputs: mav_putvalue_src1.value = 0,mav_putvalue_src2.value = 0,mav_putvalue_src3.value = 2217,mav_putvalue_instr.value =16843019 
- Expected Output: MODEL = 0
- Observed Output in the DUT dut=0x1152

Output mismatches for the above inputs proving that there is a design bug



## Verification Strategy
It's just a random testing without understanding the internal of the coprocessor.Based on the knowledge of inputs and outputs i just applied random bits at input and compared the output with the model given and found a bug.

## Is the verification complete ?
No, the Verfication is incomplete as i found a bug by chance and I have no understanding of the internal working of Coprocessor.
