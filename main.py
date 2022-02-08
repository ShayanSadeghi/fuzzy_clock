import time
from utility import get_fuzzy_time, plot_fuzzy_minutes

fuzzy_time_prime = ""
while True:
    fuzzy_time = get_fuzzy_time()
    if fuzzy_time != fuzzy_time_prime:
        fuzzy_time_prime = fuzzy_time
        print(fuzzy_time)
    plot_fuzzy_minutes()
    time.sleep(60)
get_fuzzy_time()
