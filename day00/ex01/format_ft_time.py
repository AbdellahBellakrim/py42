import time
import datetime

now = time.time()
current_datetime = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
print(current_datetime.strftime("%b %d %Y"))
