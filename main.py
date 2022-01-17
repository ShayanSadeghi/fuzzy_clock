import time
from utility import get_fuzzy_time

fuzzy_time_prime = ""
while True:
    fuzzy_time = get_fuzzy_time()
    if fuzzy_time != fuzzy_time_prime:
        fuzzy_time_prime = fuzzy_time
        print(fuzzy_time)

    time.sleep(60)
