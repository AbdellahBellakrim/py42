from time import time
from utils import time_statistics
from utils import percentage
from utils import progress_counter
from utils import get_terminal_width
from utils import progress_bar


def ft_tqdm(lst: range):
    """A generator that mimics the behavior of tqdm
    for tracking progress in loops."""
    start_time = time()
    for index, elem in enumerate(lst):
        current_time = time()
        time_s = time_statistics(start_time, current_time, index, len(lst) - 1)
        progress = percentage(index + 1, len(lst))
        counter = progress_counter(index + 1, len(lst))
        barlenght = get_terminal_width() - len(progress) - \
            len(counter) - len(time_s) - 4
        bar = progress_bar(index + 1, len(lst), barlenght)
        print(f"\r{progress}{bar} {counter} {time_s}", end="", flush=True)
        yield elem
