#!/usr/bin/python3


def safe_print_division(a, b):
    """ write a fn that divides 2 integers and prints result

    you can assume a and b are integers

    result of the division should print on finally
    """
    try:
        value = a/b
    except (ZeroDivisionError, ValueError, TypeError):
        value = None
    finally:
        print("Inside result: {}".format(value))
    return (value)
