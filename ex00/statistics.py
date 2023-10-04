import math

def ft_statistics(*args: any, **kwargs: any) -> None:
    '''
    Take in any amount of int or float, and generate mean,
    median, quartile, standard deviation and variance
    '''
    try:
        for i in args:
            assert isinstance(i, (int, float)), "value must be either int or float"
        num_array = sorted(args)
        if len(num_array) == 0:
            return
        operations = list(kwargs.values())
        if "mean" in operations:
            print(f"mean : {sum(num_array)/len(num_array)}")
        if "median" in operations:
            n = len(num_array)
            mid = n / 2
            median = num_array[math.floor(mid)] if n % 2 == 1 else sum(num_array[mid - 1]+ num_array[mid])/2
            print(f"median : {median}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")