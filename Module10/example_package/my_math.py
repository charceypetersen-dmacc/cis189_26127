PI = 3.14

operations = ["mean", "median", "mode", "average", "std_deviation"]


def mean(input_vals):
    sum = 0
    for input_val in input_vals:
        sum += input_val
    if sum > 0:
        return sum / len(input_vals)
