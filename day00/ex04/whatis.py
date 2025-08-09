import sys

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            sys.exit()
        if len(sys.argv) > 2:
            raise AssertionError("AssertionError: more than one argument is provided")
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
