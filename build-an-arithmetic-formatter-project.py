

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



