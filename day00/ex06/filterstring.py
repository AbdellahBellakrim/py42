from argparse import ArgumentParser


class CustomArgumentParser(ArgumentParser):
    def error(self):
        """Override the default error method to raise an AssertionError."""
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    """Filters words from string S longer
      than integer N using list comprehension and lambda,
      with argument validation."""
    try:
        parser = CustomArgumentParser(exit_on_error=False, add_help=False)
        parser.add_argument("S", type=str, help="input string")
        parser.add_argument("N", type=int, help="length filter")
        try:
            args, extra_args = parser.parse_known_args()
            if extra_args:
                raise AssertionError("the arguments are bad")
            words = args.S.split()
            filtered_words = [
                item for item in words if (lambda x: len(x) > args.N)(item)
            ]
            print(filtered_words)
        except Exception as e:
            raise AssertionError("the arguments are bad") from e
    except AssertionError as e:
        print(f"AssertionError: {e}")
