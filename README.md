# 🐍 Week 1: Python Logic & Algorithms

This repository contains a collection of Python scripts designed to solve various algorithmic challenges, ranging from mathematical series summation to logic-based puzzles like parking fee calculation and palindrome discovery.

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `Week1_1.py` | **Series Summation** | Calculates $a + aa + aaa + aaaa$. |
| `Week1_2.py` | **Palindrome Product** | Finds the largest palindrome from the product of two $n$-digit numbers. |
| `Week1_3.py` | **Parking Fee** | Calculates parking costs based on specific time duration tiers. |
| `Week1_5.py` | **Smallest Number** | Sorts digits to form the smallest possible valid integer. |
| `Week1_6.py` | **Max Product** | Finds the maximum product of any two integers in a list (handling negatives). |

---

## 📝 Exercise Details

### 1. Series Summation (`Week1_1.py`)
**Goal:** Compute the value of $a + aa + aaa + aaaa$ given a single digit $a$.
* **Input:** A single integer $a$.
* **Logic:** Concatenates the string representation of the number before summing.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `9` | `11106` | $9 + 99 + 999 + 9999$ |
| `3` | `3702` | $3 + 33 + 333 + 3333$ |

---

### 2. Largest Palindrome Product (`Week1_2.py`)
**Goal:** Find the largest palindrome made from the product of two $n$-digit numbers.
* **Input:** An integer representing the number of digits ($n$).
* **Constraints:** If input $\le 1$ or non-numeric, returns "Invalid".

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `2` | `9009` | $91 \times 99 = 9009$ |
| `3` | `906609` | $913 \times 993 = 906609$ |
| `1` | `Invalid` | Digits must be $> 1$. |

---

### 3. Parking Fee Calculator (`Week1_3.py`)
**Goal:** Calculate parking fees based on entry and exit timestamps.
* **Input:** Four integers: `InHour InMinute OutHour OutMinute`.
* **Pricing Rules:**
    * $\le$ 15 mins: **Free** (0).
    * 15 mins to 3 hours: **10** per hour (fractions rounded up).
    * 3 hours to 6 hours: First 3 hrs is 30, then **20** per extra hour.
    * $>$ 6 hours: Flat fee of **200**.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `7 0 7 10` | `0` | Duration 10 minutes (Free). |
| `7 0 8 0` | `10` | Duration 1 hour. |
| `7 0 20 0` | `200` | Duration > 6 hours. |

---

### 4. Smallest Number Formation (`Week1_5.py`)
**Goal:** Given a list of digits, arrange them to form the smallest possible number.
* **Input:** A space-separated list of numbers.
* **Logic:** Sorts the array. If the smallest number is 0, it swaps it with the first non-zero number to ensure the number doesn't start with 0 (unless the answer is 0).

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `3 1 0 2` | `1023` | Sorted: `0 1 2 3` → Swapped: `1 0 2 3`. |
| `5 9 1 4` | `1459` | Digits sorted ascending. |
| `0 0 5` | `500` | Validates leading non-zero. |

---

### 5. Maximum Product Pair (`Week1_6.py`)
**Goal:** Find the maximum product of two integers in a list.
* **Input:** A list of integers (e.g., `[1, 2, 3]` or `1 2 3`).
* **Logic:** Checks the product of the two largest numbers versus the product of the two smallest (most negative) numbers.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `[1, 10, 100, 2]` | `200` | $10 \times 20 = 200$ (Largest pair). |
| `[-10, -20, 5, 3]` | `200` | $-10 \times -20 = 200$ (Negatives result in positive max). |
| `[5]` | `Invalid` | List too short. |

---

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example
python Week1_5.py
