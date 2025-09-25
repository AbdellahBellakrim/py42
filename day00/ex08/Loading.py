from time import sleep
from tqdm import tqdm


def percentage(part: int, whole: int) -> str:
    return f"{(int(float((part * 100) / whole)))}%"


def progress_counter(count: int, total: int) -> None:
    return f"{int(float((count)))}/{total}"


def progress_bar(part: int, whole: int, bar_length: int = 189) -> str:
    filled_length = int(bar_length * part // whole)
    bar = '█' * filled_length + ' ' * (bar_length - filled_length)
    return f"|{bar}|"


def ft_tqdm(lst: range):
    for index, elem in enumerate(lst):
        print(f"\r{percentage(index + 1, len(lst))}{progress_bar(index + 1, len(lst))} {progress_counter(index + 1, len(lst))}", end="")
        yield elem


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

for elem in tqdm(range(333)):
    sleep(0.005)
print()
