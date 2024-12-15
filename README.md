# Uncommon Recursive Function Error in Python

This repository demonstrates a subtle bug in a recursive Python function that can lead to a stack overflow error and unexpected behavior. The bug stems from an improperly defined base case in the recursion, and it also lacks exception handling for cases such as negative inputs. The `bug.py` file contains the buggy code. A solution to this problem is provided in `bugSolution.py`.

## Bug Description

The function `function_with_uncommon_error` uses recursion to compute a value.  However, it only checks for a base case of n equals zero.  If a negative number is input, the recursion never ends.  Additionally, it is vulnerable to errors arising from non-integer inputs.

## Solution

The solution introduces proper error handling and a more robust base case to prevent the stack overflow error and enhance overall reliability.