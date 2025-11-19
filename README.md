# 🔢 Arithmetic Arranger – Python (freeCodeCamp Project)

This project is part of the **Scientific Computing with Python Certification** by **freeCodeCamp**.  
The goal of this project is to build a function that formats arithmetic problems (addition and subtraction) in a clean, vertical, and readable layout — with an option to also calculate the result.

---

## 🚀 Features

### ✅ Input Validation
The program handles the following errors:

- ❌ More than five problems  
- ❌ Invalid operators (only `+` and `-` are allowed)  
- ❌ Inputs containing non-digit characters  
- ❌ Numbers longer than four digits  

### ✅ Clean Formatting
Each arithmetic problem is:

- Right-aligned  
- Padded properly  
- Separated by equal spacing  
- Displayed in neat columns  

### ✅ Optional Solver
Pass `solve=True` to also display the answer for each problem.

---

## 🧠 What I Learned

- String manipulation  
- Input processing  
- Alignment using `rjust()`  
- Clean formatting techniques  
- Breaking a problem into smaller steps  
- Writing maintainable, readable code  
- How to structure errors and validations  

---

## 🧪 Example Output

### Input:
```python
arithmetic_arranger(["32 + 698", "1 - 2", "45 + 43"], solve=True)
```

### Output:
```
   32      1      45
+ 698    - 2    + 43
-----    ---    ----
  730     -1      88
```

---

## 🧩 Function Definition

```python
def arithmetic_arranger(problems, solve=False):
    ...
```

---

## 📌 Complete Code

```python
def arithmetic_arranger(problems, solve=False):

    # -------------------- ERRORS --------------------
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for prob in problems:
        parts = prob.split()

        num1 = parts[0]
        op = parts[1]
        num2 = parts[2]

        # Operator error
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Digits only
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # Max 4 digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Width of each problem
        width = max(len(num1), len(num2)) + 2  # 2 = operator + space

        # -------------------- ARRANGE LINES --------------------
        first_line.append(num1.rjust(width))
        second_line.append(op + num2.rjust(width - 1))
        dashes.append('-' * width)

        # If solutions required
        if solve:
            if op == "+":
                ans = str(int(num1) + int(num2))
            else:
                ans = str(int(num1) - int(num2))

            results.append(ans.rjust(width))

    # Join with 4 spaces
    arranged = "    ".join(first_line) + "\n" + \
               "    ".join(second_line) + "\n" + \
               "    ".join(dashes)

    if solve:
        arranged += "\n" + "    ".join(results)

    return arranged
```

---

## 📂 How to Use

```python
print(arithmetic_arranger(["32 + 8", "1 - 2", "123 + 49"], solve=True))
```

---

## 🧾 License

This project is open-source and free to use.

---

## 👨‍💻 Author

**Keshav Kumar Sharma**  
Python Developer • Learner • freeCodeCamp Contributor
