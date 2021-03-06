"""
Module provides function argument type and return type validators for @accept(a,b,c) and @returns(x,y,z) function decorators.

This simplifies the formalisation all function validation, particularly useful for API interfaces definition.

Usage Example:
    
    @accepts(int, int)
    @returns(int)
    def add(a, b)
        return a + b
    add(1,"3")

Original Author:    Jackson Cooper
Article:            Validate Python Function Parameter & Return Types with Decorators
Published at:       http://pythoncentral.io/validate-python-function-parameters-and-return-types-with-decorators/
Published:          Tuesday 20th August 2013 
Last Updated:       Friday 23rd August 2013
"""

import functools




def accepts(*accepted_arg_types):
    '''
    A decorator to validate the parameter types of a given function.
    It is passed a tuple of types. eg. (<type 'tuple'>, <type 'int'>)
 
    Note: It doesn't do a deep check, for example checking through a
          tuple of types. The argument passed must only be types.
    '''
 
    def accept_decorator(validate_function):
        # Check if the number of arguments to the validator
        # function is the same as the arguments provided
        # to the actual function to validate. We don't need
        # to check if the function to validate has the right
        # amount of arguments, as Python will do this
        # automatically (also with a TypeError).
        @functools.wraps(validate_function)
        def decorator_wrapper(*function_args, **function_args_dict):
            if len(accepted_arg_types) is not len(accepted_arg_types):
                raise InvalidArgumentNumberError(validate_function.__name__)
 
            # We're using enumerate to get the index, so we can pass the
            # argument number with the incorrect type to ArgumentValidationError.
            for arg_num, (actual_arg, accepted_arg_type) in enumerate(zip(function_args, accepted_arg_types)):
                if not type(actual_arg) is accepted_arg_type:
                    ord_num = ordinal(arg_num + 1)
                    raise ArgumentValidationError(ord_num,
                                                  validate_function.__name__,
                                                  accepted_arg_type)
 
            return validate_function(*function_args)
        return decorator_wrapper
    return accept_decorator
    
def returns(*accepted_return_type_tuple):
    '''
    Validates the return type. Since there's only ever one
    return type, this makes life simpler. Along with the
    accepts() decorator, this also only does a check for
    the top argument. For example you couldn't check
    (<type 'tuple'>, <type 'int'>, <type 'str'>).
    In that case you could only check if it was a tuple.
    '''
    def return_decorator(validate_function):
        # No return type has been specified.
        if len(accepted_return_type_tuple) == 0:
            raise TypeError('You must specify a return type.')
 
    	@functools.wraps(validate_function)
        def decorator_wrapper(*function_args):
            # More than one return type has been specified.
            if len(accepted_return_type_tuple) > 1:
                raise TypeError('You must specify one return type.')
 
            # Since the decorator receives a tuple of arguments
            # and the is only ever one object returned, we'll just
            # grab the first parameter.
            accepted_return_type = accepted_return_type_tuple[0]
 
            # We'll execute the function, and
            # take a look at the return type.
            return_value = validate_function(*function_args)
            return_value_type = type(return_value)
 
            if return_value_type is not accepted_return_type:
                raise InvalidReturnType(return_value_type,
                                        validate_function.__name__) 
 
            return return_value
 
        return decorator_wrapper
    return return_decorator


class ArgumentValidationError(ValueError):
    '''
    Raised when the type of an argument to a function is not what it should be.
    '''
    def __init__(self, arg_num, func_name, accepted_arg_type):
        self.error = 'The {0} argument of {1}() is not a {2}'.format(arg_num,
                                                                     func_name,
                                                                     accepted_arg_type)
 
    def __str__(self):
        return self.error
 
 
 
class InvalidArgumentNumberError(ValueError):
    '''
    Raised when the number of arguments supplied to a function is incorrect.
    Note that this check is only performed from the number of arguments
    specified in the validate_accept() decorator. If the validate_accept()
    call is incorrect, it is possible to have a valid function where this
    will report a false validation.
    '''
    def __init__(self, func_name):
        self.error = 'Invalid number of arguments for {0}()'.format(func_name)
 
    def __str__(self):
        return self.error
 
 
 
class InvalidReturnType(ValueError):
    '''
    As the name implies, the return value is the wrong type.
    '''
    def __init__(self, return_type, func_name):
        self.error = 'Invalid return type {0} for {1}()'.format(return_type,
                                                                func_name)
 
    def __str__(self):
        return self.error
