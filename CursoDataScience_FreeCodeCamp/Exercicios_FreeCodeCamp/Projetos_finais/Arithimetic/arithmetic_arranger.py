def arithmetic_arranger(problems, show_results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2
        arranged_problems["top"].append(operand1.rjust(width))
        arranged_problems["bottom"].append(operator + operand2.rjust(width - 1))
        arranged_problems["line"].append("-" * width)

        if show_results:
            result = str(eval(problem)).rjust(width)
            arranged_problems["result"].append(result)

    arranged_lines = []
    arranged_lines.append("    ".join(arranged_problems["top"]))
    arranged_lines.append("    ".join(arranged_problems["bottom"]))
    arranged_lines.append("    ".join(arranged_problems["line"]))

    if show_results:
        arranged_lines.append("    ".join(arranged_problems["result"]))

    return "\n".join(arranged_lines)
