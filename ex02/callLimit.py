# This exercise teaches about decorators,
# at the same time uses nonlocal vars as
# well.
# Decorators are similar with modifiers in
# Solidity. It modifies the behaviour of a
# function.

# @callLimit(3)
# def f():
# 	print ("f()")
# is equals to
# def f():
# 	print ("f()")
# f = callLimit(3)(f)

def callLimit(limit: int):
    '''
    The higher order function used
    to store count.
    '''
    count = 0

    def callLimiter(function):
        '''
        This function be the actual decorator itself.
        '''

        def limit_function(*args: any, **kwargs: any):
            '''
            Wrapper function that wraps the original function,
            and adds additional functions to it
            '''
            nonlocal count
            if count < limit:
                count += 1
                function()
            else:
                print(f"Error: {function} call too many times")
        return limit_function  # return the decorated function
    return callLimiter  # return the actual decorator
