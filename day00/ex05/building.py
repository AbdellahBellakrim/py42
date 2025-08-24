import sys


def get_input_text():
    """"Gets input text from command-line arguments or user input"""
    if len(sys.argv) < 2:
        try:
            text = input("What is the text to count?\n")
            text += "\n"
        except EOFError:
            pass
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    elif len(sys.argv) > 2:
        raise AssertionError("Too many arguments provided")
    return text


def summarizeStringComposition(text: str) -> None:
    """gets a single string argument,
    displays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces."""
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in '''!()-[]{};:'",<>./?@#$%^&*_~''')
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    """Main function to execute the script."""
    try:
        text = get_input_text()
        summarizeStringComposition(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception:
        sys.exit()
