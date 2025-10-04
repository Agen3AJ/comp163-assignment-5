# comp163-assignment-5w
## Overview
This assignment demonstrates mastery of `while` loops, `for` loops, and nested loops through three challenges.  
Each challenge highlights why a particular loop type is the most appropriate and shows how to structure code clearly.

---

## Challenge 1: Collatz Sequence
**Loop Used:** `while` loop  
**Reasoning:**  
The number of iterations is unknown until the sequence reaches 1. A `for` loop would not work naturally since we don’t know the upper limit in advance. The `while` loop continues running until the condition (`current_number != 1`) is false.  

**How it Works:**  
- Start from a positive integer.  
- If even, divide by 2. If odd, multiply by 3 and add 1.  
- Continue until reaching 1.  
- Print the sequence and step count.  

---

## Challenge 2: Prime Number Checker
**Loop Used:** `for` loop  
**Reasoning:**  
The possible divisors are in a known, fixed range (`2` to `n-1`). A `for` loop is the most natural way to test each divisor one at a time.  

**How it Works:**  
- User enters a number greater than 1.  
- The program tests divisors from 2 up to `n-1`.  
- If any divisor divides evenly, the number is not prime.  
- Otherwise, it is declared prime.  

---

## Challenge 3: Multiplication Table Grid
**Loop Used:** Nested `for` loops  
**Reasoning:**  
A multiplication table is two-dimensional: rows and columns. The outer loop handles rows, and the inner loop handles columns. This ensures every combination is covered.  

**How it Works:**  
- Prints a header row (1–10).  
- For each row, prints the row number and the product of row × column.  
- Uses formatted spacing for alignment.  

---

## Git Commit History
1. `Challenge 1: Collatz sequence - while loop for unknown iterations`  
2. `Challenge 2: Prime checker - for loop for known range`  
3. `Challenge 3: Multiplication grid - nested loops for 2D data`  
4. `Add loop design documentation`  

---

## AI Usage
- I only used AI for concept clarification, debugging help, and formatting guidance.  
- I did not use AI to generate the code; it was typed out myself.  
- All logic and implementation were written and understood by me.  
