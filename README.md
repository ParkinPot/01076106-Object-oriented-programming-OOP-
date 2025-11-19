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

# 🐍 Week 2: Data Structures & Date Logic

This repository contains Python scripts focused on two main areas: **Calendar/Date Algorithms** (handling leap years, day counting) and **Dictionary/JSON Manipulation** (updating nested records and calculating averages).

## 📂 Table of Contents

| File | Challenge Name | Description |
| :--- | :--- | :--- |
| `week2_1.py` | **Day of Year** | Calculates the specific day number (1-366) for a given date. |
| `week2_2.py` | **Date Difference** | Calculates the number of days between two specific dates (inclusive). |
| `week2_3.py` | **Simple Grade Update** | Updates a subject score and calculates the average for a single student. |
| `week2_4.py` | **Nested Grade System** | Manages a multi-student gradebook (nested dictionaries) and calculates per-student averages. |
| `week2_5.py` | **Music Collection** | A complex record updater for a music library (handling tracks, artists, and albums). |

---

## 📝 Exercise Details

### 1. Day of Year (`week2_1.py`)
**Goal:** Determine the ordinal day number (1st to 365th/366th) of a specific date.
* **Input:** A date string in format `Day-Month-Year`.
* **Logic:**
    * Checks for Leap Years to adjust February to 29 days.
    * Sums the days of full months preceding the current month, then adds the current day.
    * Returns "Invalid" for non-existent dates (e.g., 30-02-2023).

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1-1-2023` | `day of year: 1 is_leap: False` | First day of the year. |
| `1-3-2020` | `day of year: 61 is_leap: True` | 2020 is a leap year (Feb has 29 days). |
| `32-1-2023`| `Invalid` | January only has 31 days. |

---

### 2. Date Difference (`week2_2.py`)
**Goal:** Calculate the total number of days between two dates, inclusive of the start and end date.
* **Input:** Two dates separated by a comma: `D-M-Y,D-M-Y`.
* **Logic:**
    * Calculates the "Day of Year" index for both dates.
    * If years differ, it sums the remaining days of the start year + all days in intervening years + days in the end year.
    * **Note:** The calculation is inclusive (End - Start + 1).

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `1-1-2023,2-1-2023` | `2` | January 1st and January 2nd (2 days total). |
| `31-12-2022,1-1-2023`| `2` | Spanning across a new year. |
| `28-2-2023,1-3-2023` | `2` | Normal year (No Feb 29th). |

---

### 3. Simple Grade Update (`week2_3.py`)
**Goal:** Update a dictionary of scores and return the new average.
* **Input:** A string containing a dictionary, a subject, and a new score separated by ` | `.
* **Logic:**
    * Parses the input string into a Python dictionary.
    * Adds or updates the score for the specified subject.
    * Calculates the arithmetic mean of all values.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `{'Math': 50} | 'Science' | 100` | `{'Math': 50, 'Science': 100}, Average score: 75.00` | (50+100)/2 = 75. |
| `{ } | 'Art' | 80` | `{'Art': 80}, Average score: 80.00` | Adding to empty dict. |

---

### 4. Nested Grade System (`week2_4.py`)
**Goal:** Manage a complex gradebook where students have their own dictionaries of subjects.
* **Input:** `Dictionary | Student_ID | Subject | Score`.
* **Structure:** `{ Student_ID: { Subject: Score } }`.
* **Logic:**
    * Accesses the specific student's record (creates it if it doesn't exist).
    * Updates the subject score.
    * Returns the entire updated structure and a dictionary of average scores for **all** students.

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `{'1': {'Math': 50}} | '1' | 'Eng' | 100` | `{'1': {'Math': 50, 'Eng': 100}}, Average score: {'1': '75.00'}` | Updates Student 1. |
| `{'1': {'Math': 50}} | '2' | 'Math' | 10` | `{'1': {'Math': 50}, '2': {'Math': 10}}, Average score: {'1': '50.00', '2': '10.00'}` | Adds new Student 2. |

---

### 5. Music Collection Updater (`week2_5.py`)
**Goal:** Manipulate a JSON-like music collection based on specific business rules.
* **Input:** A dictionary followed by updates: `Dict}} | ID|Prop|Value | ID|Prop|Value...`.
* **Rules:**
    * If `value` is empty string: Delete the property.
    * If `property` is "tracks": Add value to the end of the tracks list (create list if missing).
    * Otherwise: Update the property value.

| Input | Output |
| :--- | :--- |
| `{2548: {'artist': 'Bon Jovi', 'tracks': []}}} | 2548|tracks|It's My Life` | `{2548: {'artist': 'Bon Jovi', 'tracks': ["It's My Life"]}}` |
| `{2548: {'artist': 'Bon Jovi', 'tracks': []}}} | 2548|artist|` | `{2548: {'tracks': []}}` (Artist deleted) |

---
