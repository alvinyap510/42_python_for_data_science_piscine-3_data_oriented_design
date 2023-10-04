# Introducing the idea of higher order function
# and closure function. Also introduces non local
# variables

def square(x: int | float) -> int | float:
    '''
    Return the square of x
    '''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''
    Return x to the power of itself
    '''
    return x ** x


def outer(x: int | float, function) -> object:
    '''
    Ourter function. In python functions can be
    passed around and assigned to variables.
    This function returns the inner function to
    the variable when called.
    '''
    count = 0

    def inner() -> float:
        '''
        Closure function. Closures can capture and
        remember external values, with the nonlocal
        keyword allows the closue to access the variable
        of its nearest outer scope, excluding global
        variables.
        '''
        nonlocal count
        count += 1
        res = x
        for i in range(count):
            res = function(res)
        return res
    return inner
