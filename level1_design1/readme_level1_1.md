# Mux Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
*Make sure to include the Gitpod id in the screenshot*

![gitpod_id](https://user-images.githubusercontent.com/56909326/181591542-ec5ab634-d09e-4cf0-8c2e-0a76247618ba.png)



## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Mux module here) which takes in 5-bit and 2-bit inputs *sel* and *inp0-30* respectively and gives 2-bit output *out*

1.The values are assigned to the input port using 
```
dut.sel.value = 13
dut.inp12.value = 2
dut.inp13.value = 1
```
The assert statement is used for comparing the Mux's output to the expected value.

The following error is seen:
```
 assert dut.out.value == dut.inp13.value,f'Mux result is incorrect: {bin(dut.out.value)} != {bin(dut.inp13.value)}'
                     AssertionError: Mux result is incorrect: 0b10 != 0b1
                     
```

2.The values are assigned to the input port using 
```
dut.sel.value = 30
dut.inp30.value = 3

```
The assert statement is used for comparing the Mux's output to the expected value.

The following error is seen:
```
 assert dut.out.value == dut.inp30.value,f"Mux result is incorrect: {dut.out.value} != {dut.inp30.value}"
                     AssertionError: Mux result is incorrect: 00 != 11

```

## Test Scenario **(1)**
- Test Inputs: sel=13 inp12=2 inp13=1
- Expected Output: out=1
- Observed Output in the DUT dut.out=2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 1
Based on the above test input and analysing the design, we see the following

```
 5'b01101: out = inp12;  ==> BUG
 5'b01101: out = inp13; 
```
For the mux design, the case should be ``5'b01100`` instead of ``5'b01101`` as in the design code.

## Test Scenario **(2)**
- Test Inputs: sel=30 inp30=3
- Expected Output: out=3
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug 2
Based on the above test input and analysing the design, we see the following

```
5'b11101: out = inp29;
              ==>Bug
default: out = 0; 
```
For the mux design, there should be one more case ``5'b11110`` in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![bug_passed_1](https://user-images.githubusercontent.com/56909326/180762425-89923095-c773-4be1-bed9-a1663103e27d.png)
_________________________________________________________________________________________________________________________________
![bug_passed_2](https://user-images.githubusercontent.com/56909326/180759632-6e51546a-3e7c-4ad6-b506-7576c8bdd1f1.png)


The updated design is checked in as mux_corrected.v

## Verification Strategy
For such a small design I prefered to inspect the whole code and while doing so I found 2 bugs.After finding these bugs i applied constrained random inputs which all passed.

## Is the verification complete ?
Yes, the Verfication is complete Because after finding 2 bugs by inspection i applied constrained inputs and found 0 bug.
