import sys


def check_even_odd():
    """
    Checks if the provided command-line argument is an integer.
    prints whether it is even or odd.
    Raises an AssertionError if there are too many arguments,
    or if the argument is not an integer.
    """
    try:
        if len(sys.argv) < 2:
            exit("Usage: python whatis.py <number>")
        if len(sys.argv) > 2:
            raise AssertionError(
                "AssertionError: more than one argument is provided"
            )
        try:
            int_value = int(sys.argv[1])
        except ValueError:
            raise AssertionError("AssertionError: argument is not an integer")
        if int_value % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    check_even_odd()
