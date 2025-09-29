from time import sleep, time
# from tqdm import tqdm
from shutil import get_terminal_size


def get_terminal_width():
    """
    Retrieves the width of the terminal window in characters.
    """
    size = get_terminal_size()
    return size.columns


def percentage(part: int, whole: int) -> str:
    return f"{(int(float((part * 100) / whole)))}%"


def progress_counter(count: int, total: int) -> str:
    return f"{int(float((count)))}/{total}"


def progress_bar(part: int, whole: int, bar_length) -> str:
    filled_length = int(bar_length * part // whole)
    bar = '█' * filled_length + ' ' * (bar_length - filled_length)
    return f"|{bar}|"


def time_statistics(start_t, current_t) -> str:
    """
        [elapsed<remaining, rate]
        [00:01<00:00, 191.29it/s]
            │    │       │
            │    │       └── Processing speed (191.29 iterations per second)
            │    │
            │    └── Estimated time remaining (less than 1 second)
            │
            └── Elapsed time (1 second)
    """
    return ""


def ft_tqdm(lst: range):
    start_time = time()
    for index, elem in enumerate(lst):
        current_time = time()
        print(round(current_time - start_time, 2))
        progress = percentage(index + 1, len(lst))
        counter = progress_counter(index + 1, len(lst))
        barlenght = get_terminal_width() - len(progress) - len(counter) - 3
        bar = progress_bar(index + 1, len(lst), barlenght)
        # print(f"\r{progress}{bar} {counter}", end="", flush=True)
        yield elem


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()
