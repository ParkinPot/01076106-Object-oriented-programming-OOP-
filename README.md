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
```

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

## 🚀 How to Run

Ensure you have Python 3 installed. Open your terminal and run any file:

```bash
# Example
python week2_1.py
```

# 🎓 Week 3: Object-Oriented Programming (Enrollment System)

This week focuses on building a complete **University Enrollment System** using Python's Object-Oriented Programming (OOP) features. The script manages complex relationships between Students, Subjects, Teachers, and Enrollments, demonstrating encapsulation, property decorators, and logic for grading and GPA calculation.

## 📂 File Overview

| File | System Name | Description |
| :--- | :--- | :--- |
| `week3.py` | **University Registrar** | A comprehensive system to manage student enrollments, assigning teachers, recording grades, and calculating GPA (GPS). |

---

## 🏗️ System Architecture (Classes)

The system is built upon four primary classes that interact with each other:

| Class | Description | Key Attributes |
| :--- | :--- | :--- |
| **`Student`** | Represents a university student. | `student_id`, `student_name` |
| **`Subject`** | Represents a course offered. | `subject_id`, `subject_name`, `credit`, `teacher` |
| **`Teacher`** | Represents an instructor. | `teacher_id`, `teacher_name` |
| **`Enrollment`** | Link table connecting a Student to a Subject. | `student` (obj), `subject` (obj), `grade` |

---

## 📝 Key Features & Logic

### 1. Enrollment Management
**Goal:** Manage students signing up for or dropping classes.
* **Logic:**
    * **Enroll:** Checks if the student is already enrolled to prevent duplicates. Creates an `Enrollment` object linking the Student and Subject.
    * **Drop:** Removes the specific `Enrollment` instance. Returns "Not Found" if the student wasn't enrolled.

| Function Call | Return / Output | Explanation |
| :--- | :--- | :--- |
| `enroll_to_subject(student1, cs101)` | `"Done"` | Successfully registered. |
| `enroll_to_subject(student1, cs101)` | `"Already Enrolled"` | Prevents duplicate registration. |
| `drop_from_subject(student1, cs101)` | `"Done"` | Successfully removed. |

### 2. Grading & GPA (GPS)
**Goal:** Assign grades to enrollments and calculate the Grade Point Average.
* **Grading Scale:** A=4, B=3, C=2, D=1.
* **Formula:** $\frac{\sum(\text{Grade Point} \times \text{Credit})}{\sum(\text{Total Credits})}$
* **Logic:**
    * `assign_grade`: Updates the `grade` attribute in the Enrollment object.
    * `get_student_GPS`: Iterates through all subjects a student is enrolled in, converts letter grades to points, and calculates the weighted average.

| Function Call | Return / Output | Explanation |
| :--- | :--- | :--- |
| `assign_grade(student2, cs101, 'A')` | `"Done"` | Grade 'A' assigned. |
| `get_student_GPS(student2)` | `3.0` | (A=4, B=3, C=2) across 3-credit courses averages to 3.0. |

### 3. Search & Reporting
**Goal:** Retrieve data about the system state.
* **Logic:** Functions filter the main `enrollment_list` to find specific associations.

| Function Call | Return / Output | Explanation |
| :--- | :--- | :--- |
| `get_no_of_student_enrolled(cs101)` | `5` | Counts total students in CS101. |
| `get_teacher_teach(cs101)` | `Mr. Welsh` | Returns the teacher object assigned to the subject. |
| `get_student_record(student2)` | `{'CS101': ['Comp Prog 1', 'A']...}` | Dictionary of all courses and grades for a student. |

---

## 🧪 Test Cases (Built-in)

The `week3.py` file includes a suite of **14 Test Cases** that run automatically when the file is executed. These tests verify everything from basic enrollment to complex GPA calculations.

### Sample Test Output
When you run the code, you will see output verifying the logic:

```text
Test Case #1 : test enroll_to_subject complete
Answer : {'66010001': 'Keanu Welsh', ...}
{'66010001': 'Keanu Welsh', ...}

...

Test case #14 get_student_GPS
Answer : 3.0
3.0
```

# 🏦 Week 4: ATM & Bank System Simulation

This week's project is a comprehensive object-oriented simulation of a Banking System. It models the interactions between a central Bank, ATM machines, Users, Accounts, and ATM Cards, handling logic for authentication, transaction limits, and fund transfers.

## 📂 File Overview

| File | System Name | Description |
| :--- | :--- | :--- |
| `week4.py` | **ATM Simulator** | A complete system managing accounts, cards, and ATM operations including deposits, withdrawals, and transfers. |

---

## 🏗️ System Architecture (Classes)

The simulation relies on five interconnected classes:

| Class | Description | Key Attributes |
| :--- | :--- | :--- |
| **`Bank`** | The central entity holding all users and ATM machines. | `users`, `atms` |
| **`User`** | Represents a bank customer. | `citizen_id`, `name`, `accounts` (list) |
| **`Account`** | Holds financial data and transaction history. | `account_number`, `balance`, `transactions` |
| **`ATMCard`** | Represents the physical card used for access. | `card_number`, `pin`, `max_withdraw_limit` (40,000) |
| **`ATMMachine`** | The interface for performing transactions. | `machine_id`, `initial_amount` (Cash inside machine) |

---

## 💳 Key Features & Logic

### 1. Authentication (`insert_card`)
**Goal:** Validate user access before allowing transactions.
* **Logic:** The ATM accepts a card instance and a PIN string. It iterates through the Bank's users to find the matching account.
* **Security:** Returns `None` (access denied) if the PIN is incorrect.

### 2. Withdrawal Logic
**Goal:** Safe money removal with multiple validation layers.
* **Checks Performed:**
    1. **Account Balance:** User must have enough money.
    2. **Daily Limit:** Cannot exceed the card's limit (default **40,000** baht).
    3. **ATM Cash:** The physical machine must have enough bills (`initial_amount`).
* **Output:** Returns "Success", "Insufficient Funds" (ATM empty), or "Error" (User broke).

### 3. Transfers & Deposits
**Goal:** Moving funds between entities.
* **Deposit:** Increases account balance and adds cash to the ATM machine's reserve.
* **Transfer:** Atomic operation that decrements the sender's balance and increments the receiver's balance, recording a transaction log for both.

---

## 🧪 Test Cases (Built-in)

The file includes **10 comprehensive test cases** to verify the system's robustness.

### Sample Scenarios

| Case # | Scenario | Expected Outcome |
| :--- | :--- | :--- |
| **#1** | **Card Insertion** | Returns Account object if PIN matches; otherwise `None`. |
| **#3** | **Negative Deposit** | Returns `Error` (Cannot deposit -1 baht). |
| **#9** | **Limit Exceeded** | Returns `Error` when trying to withdraw **45,000** (Limit is 40,000). |
| **#10** | **ATM Empty** | Returns `Insufficient Funds` if the ATM machine lacks cash (even if user has money). |

### Sample Output
Running the script produces a detailed log of operations:

```text
Harry account before test: 20000
Attempting to withdraw 45,000 baht...
Expected result: Exceeds daily withdrawal limit of 40,000 baht
Actual result: Error
Harry account after test: 20000
```

# 🏦 Week 5: Advanced Banking System (OOP & Unit Testing)

This project is an advanced evolution of the previous banking simulation. It introduces a robust Object-Oriented architecture using **Inheritance** (Base classes for Accounts, Cards, and Channels) and relies on Python's `unittest` framework to verify system integrity through 19 specific test scenarios.

## 📂 File Overview

| File | System Name | Description |
| :--- | :--- | :--- |
| `Lab5_skeleton.py` | **Banking Unit Tests** | A complete banking ecosystem implementation including `Bank`, `User`, `Account` types, `Card` types, and `TransactionChannel` types, verified by a suite of unit tests. |

---

## 🏗️ System Architecture

The system is designed around three main abstract hierarchies:

### 1. Accounts (`Account` Parent Class)
* **`SavingAccount`**: Standard account; calculates 0.5% interest. Limits withdrawals to 50,000/transaction.
* **`FixedAccount`**: High-interest account (2.5%) with a maturity period. Withdrawing early results in a penalty (reduced interest).
* **`CurrentAccount`**: Standard transactional account for merchants.

### 2. Cards (`Card` Parent Class)
* **`ATMCard`**: Can only be used at ATM machines. Annual fee: 150.
* **`DebitCard`**: Base for cards that work at ATMs and EDC machines.
    * **`ShoppingDebitCard`**: Earns 1% cashback on EDC purchases > 1000.
    * **`TravelDebitCard`**: Standard debit card (simulated insurance benefits).

### 3. Transaction Channels (`TransactionChannel` Parent Class)
* **`ATMMachine`**: Machine for withdrawals/deposits using Cards + PIN.
* **`Counter`**: Human-operated branch services. Requires **Identity Verification** (Citizen ID).
* **`EDCMachine`**: Merchant devices for swiping Debit Cards to pay for goods.

---

## 🧪 Key Logic & Features

### 1. Fixed Account Maturity Logic
**Goal:** Calculate interest differently based on whether the withdrawal is before or after the fixed term.
* **Logic:**
    * If `current_date >= maturity_date`: Full interest (2.5%) is applied.
    * If `current_date < maturity_date`: Reduced interest (approx 1.25%) is calculated based on months passed.
    * **Constraint:** Cannot withdraw if no initial deposit exists.

### 2. EDC Payment & Cashback
**Goal:** Allow merchants to accept payments and give cashback to specific cards.
* **Logic:**
    * `swipe_card`: Verifies the card is a `DebitCard` (ATM cards fail here) and checks the PIN.
    * `pay`: Transfers money from Customer to Merchant.
    * `calculate_cashback`: If the card is a `ShoppingDebitCard` and amount > 1000, returns 1% back to the user.

### 3. Counter Identity Verification
**Goal:** Secure transactions performed at a physical bank branch.
* **Logic:** Methods like `deposit` or `withdraw` at the `Counter` require `citizen_id`. The system verifies that `account.user.citizen_id` matches the person standing at the counter.

---

## 📊 Test Cases (Unit Tests)

The file uses `unittest` to run ~19 specific scenarios. Below are examples of the inputs and expected behaviors defined in the tests.

### Test Group: Account Management
| Test | Input / Action | Expected Output |
| :--- | :--- | :--- |
| **Interest** | `thor_savings.calculate_interest(1)` (1 year) | Balance increases by **0.5%**. Transaction type `I` recorded. |
| **Fixed Early** | Withdraw from `FixedAccount` after 6 months (Term: 12). | Success, but interest is calculated at a **reduced rate** (~1.25%). |
| **No Deposit** | Withdraw from `FixedAccount` with 0 balance. | **Error:** "No initial deposit". |

### Test Group: Channels & Security
| Test | Input / Action | Expected Output |
| :--- | :--- | :--- |
| **Counter Deposit** | `counter.deposit(..., citizen_id="WRONG_ID")` | **Error:** "Invalid identity". |
| **ATM Withdraw** | `atm.withdraw` > Account Balance | **Error** (Insufficient funds). |
| **ATM Limit** | `atm.withdraw(50001)` on Saving Account | **Error** (Exceeds 50k limit). |

### Test Group: Cards & EDC
| Test | Input / Action | Expected Output |
| :--- | :--- | :--- |
| **Shopping Card** | `edc.pay(steve_shopping_card, 2000)` | Merchant +2000. Steve -2000. Steve gets **20 cashback** (1%). |
| **ATM Card on EDC** | `edc.swipe_card(tony_atm_card, ...)` | **Error:** "Invalid card or PIN" (ATM cards cannot be used on EDC). |

---

## 🚀 How to Run

Since this file uses the `unittest` framework, you execute it differently than a standard script. It will automatically discover and run all test cases.

```bash
# Run all tests with verbose output
python -m unittest Lab5_skeleton.py -v
```
