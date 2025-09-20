from argparse import ArgumentParser

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    ' ': '/'  # Represents a space between words
}


class CustomArgumentParser(ArgumentParser):
    def error(self):
        """Override the default error method to raise an AssertionError."""
        raise AssertionError("the arguments are bad")


def toMorseCode(string):
    """Convert a given text to Morse code."""
    morse_code = ' '.join(MORSE_CODE_DICT[char.upper()] for char in string)
    print(morse_code)


if __name__ == "__main__":
    """Main program."""
    try:
        parser = CustomArgumentParser(exit_on_error=False, add_help=False)
        parser.add_argument("text", type=str, help="Text to convert")
        try:
            args, extra_args = parser.parse_known_args()
            if extra_args or not all(
                 list(char.isalnum() or char.isspace() for char in args.text)
             ):
                raise AssertionError("the arguments are bad")
            toMorseCode(args.text)
        except Exception as e:
            raise AssertionError("the arguments are bad") from e
    except Exception as e:
        print(f"AssertionError: {e}")
