from shutil import get_terminal_size


def get_terminal_width():
    """
    Retrieves the width of the terminal window in characters.
    """
    size = get_terminal_size()
    return size.columns


def percentage(part: int, whole: int) -> str:
    """Calculates the percentage of 'part' with respect to 'whole'
    and returns it as a formatted string with a percentage sign."""
    return f"{(int(float((part * 100) / whole)))}%"


def progress_counter(count: int, total: int) -> str:
    """Returns a formatted string representing the progress counter."""
    return f"{int(float((count)))}/{total}"


def progress_bar(part: int, whole: int, bar_length) -> str:
    """Generates a progress bar string based on the current progress."""
    filled_length = int(bar_length * part // whole)
    bar = '█' * filled_length + ' ' * (bar_length - filled_length)
    return f"|{bar}|"


def time_statistics(start_t, current_t, current_iter, total_iter) -> str:
    """
    Computes and formats time statistics for progress tracking.
        [elapsed<remaining, rate]
        [00:01<00:00, 191.29it/s]
            │    │       │
            │    │       └── Processing speed (191.29 iterations per second)
            │    │
            │    └── Estimated time remaining (less than 1 second)
            │
            └── Elapsed time (1 second)
    """
    elapsed_t = current_t - start_t
    rate = (current_iter + 1) / elapsed_t if elapsed_t else 0
    remaining_t = (total_iter - current_iter) / rate if rate else 0

    def format_time(seconds):
        minutes = int(seconds) // 60
        secs = int(seconds) % 60
        return f"{minutes:02}:{secs:02}"

    elapsed_str = format_time(elapsed_t)
    remaining_str = format_time(remaining_t)
    rate_str = f"{rate:7.2f}it/s"  # Always 7 chars before 'it/s'
    # Pad the whole string to a fixed length (e.g., 24 chars)
    stat = f"[{elapsed_str}<{remaining_str},{rate_str}]"
    return stat.ljust(24)
