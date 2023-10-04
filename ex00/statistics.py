# This exercise is about learning to use
# *args and **kwargs

def cal_mean(num_array: list[int or float]):
    '''
    Calculate and print out the mean of a given array
    of num_array
    '''
    if len(num_array) == 0:
        print("ERROR")
        return
    print(f"mean : {sum(num_array)/len(num_array)}")


def cal_median(num_array: list[int or float], print_out: bool = True) -> float:
    '''
    Calculate and print out the mean of a given array
    of num_array
    '''
    if len(num_array) == 0:
        print("ERROR")
        return
    n = len(num_array)
    if n % 2 == 1:
        median = num_array[n // 2]
        if print_out is True:
            print(f"median : {median}")
        return median
    else:
        mid_a = num_array[n // 2 - 1]
        mid_b = num_array[n // 2]
        median = (mid_a + mid_b) / 2
        if print_out is True:
            print(f"median : {median}")
        return median


def cal_quartile(num_array: list[int or float]):
    '''
    Calculate and print out the 25% quartile and 75%
    quartile of num_array
    '''
    if len(num_array) == 0:
        print("ERROR")
        return
    n = len(num_array)
    if n % 2 == 0:
        lower_half = num_array[:n//2]
        upper_half = num_array[n//2:]
        q1 = float(cal_median(lower_half, False))
        q3 = float(cal_median(upper_half, False))
        print(f"quartile : [{q1}, {q3}]")
    else:
        lower_half = num_array[:n//2 + 1]
        upper_half = num_array[n//2:]
        q1 = float(cal_median(lower_half, False))
        q3 = float(cal_median(upper_half, False))
        print(f"quartile : [{q1}, {q3}]")


def cal_variance(num_array: list[int or float],
                 print_out: bool = True) -> float:
    '''
    Calculate and print the variance
    of num_array
    '''
    if len(num_array) == 0:
        print("ERROR")
        return
    mean = sum(num_array) / len(num_array)
    squared_diff = [(num - mean) ** 2 for num in num_array]
    variance = sum(squared_diff) / len(num_array)
    if print_out is True:
        print(f"var : {variance}")
    return variance


def cal_std_dev(num_array: list[int or float]):
    '''
    Calculate and print the standard deviation
    of num_array
    '''
    if len(num_array) == 0:
        print("ERROR")
        return
    variance = cal_variance(num_array, False)
    std = variance ** 0.5
    print(f"std: {std}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    '''
    Take in any amount of int or float, and generate mean,
    median, quartile, standard deviation and variance
    '''
    try:
        for i in args:
            assert isinstance(
                i, (int, float)), "value must be either int or float"
        num_array = sorted(args)
        operations = list(kwargs.values())
        if "mean" in operations:
            cal_mean(num_array)
        if "median" in operations:
            cal_median(num_array)
        if "quartile" in operations:
            cal_quartile(num_array)
        if "std" in operations:
            cal_std_dev(num_array)
        if "var" in operations:
            cal_variance(num_array)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
