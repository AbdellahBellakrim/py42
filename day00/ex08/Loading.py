from time import sleep
from tqdm import tqdm


def ft_tqdm(iterable):
    for index, elem in enumerate(iterable):
        print(f"\r{(int(float((index + 1) * 100) / len(iterable)))}% [] {int(float((index + 1)))}/{len(iterable)} [00:01<00:00, 191.61it/s]", end="")
        yield elem


for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()



# Displays a progress bar that updates in real-time
# Shows completion percentage
# Displays elapsed time and estimated time remaining
# Shows iterations per second rate
# Updates dynamically without spamming the console
