import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt
import time

x = np.arange(0, 60, 0.1)
minutes_mv = [
    fuzzy.trapmf(x, [0, 0, 2.5, 5]),  # to_00
    fuzzy.trimf(x, [2.5, 5, 10]),  # to_05
    fuzzy.trimf(x, [5, 10, 15]),  # to_10
    fuzzy.trimf(x, [10, 15, 20]),  # to_15
    fuzzy.trimf(x, [15, 20, 30]),  # to_20
    fuzzy.trimf(x, [20, 30, 40]),  # to_30
    fuzzy.trimf(x, [30, 40, 45]),  # to_40
    fuzzy.trimf(x, [40, 45, 50]),  # to_45
    fuzzy.trimf(x, [45, 50, 60]),  # to_50
    fuzzy.trapmf(x, [50, 55, 60, 60]),  # to_60
]

fuzzy_labels = [
    "zero",
    "five after",
    "ten after",
    "fifteen after",
    "twenty after",
    "thirty after",
    "twenty to",
    "fifteen to",
    "ten to",
    "sixty",
]

hours = [
    "Twelve",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
]


def _get_time():
    h, m, s = time.strftime("%H:%M:%S", time.localtime()).split(":")
    return [int(h), int(m), int(s)]


def get_fuzzy_time():
    h, m, s = _get_time()
    c = 0
    max_mv = minutes_mv[0][m * 10]
    for i in range(1, 10):
        if minutes_mv[i][m * 10] > max_mv:
            max_mv = minutes_mv[i][m * 10]
            c = i

        if h >= 12:
            h -= 12

        if c > 0 and c <= 5:
            fuzzy_time = f"It is {fuzzy_labels[c]} {hours[h]}"
        elif c > 5 and c < 9:
            fuzzy_time = f"It is {fuzzy_labels[c]}  {hours[h+1]}"
        elif c == 0:
            fuzzy_time = f"It is {hours[h]}"
        elif c == 9:
            fuzzy_time = f"It is {hours[h+1]}"

    return fuzzy_time


def plot_fuzzy_minutes():
    h, m, s = _get_time()
    fig, axs = plt.subplots(1, figsize=(15, 6))
    axs.plot(x, minutes_mv[0], linewidth=1.5, label=fuzzy_labels[0])
    axs.plot(x, minutes_mv[1], linewidth=1.5, label=fuzzy_labels[1])
    axs.plot(x, minutes_mv[2], linewidth=1.5, label=fuzzy_labels[2])
    axs.plot(x, minutes_mv[3], linewidth=1.5, label=fuzzy_labels[3])
    axs.plot(x, minutes_mv[4], linewidth=1.5, label=fuzzy_labels[4])
    axs.plot(x, minutes_mv[5], linewidth=1.5, label=fuzzy_labels[5])
    axs.plot(x, minutes_mv[6], linewidth=1.5, label=fuzzy_labels[6])
    axs.plot(x, minutes_mv[7], linewidth=1.5, label=fuzzy_labels[7])
    axs.plot(x, minutes_mv[8], linewidth=1.5, label=fuzzy_labels[8])
    axs.plot(x, minutes_mv[9], linewidth=1.5, label=fuzzy_labels[9])
    axs.set_title("Fuzzy Minutes")
    axs.set_ylabel("Membership")
    axs.set_xlabel("Time")
    axs.axvline(x=m, c="r", ls="--")
    axs.legend(loc="upper left", bbox_to_anchor=(1.004, 1))
    plt.savefig(fname="graph.png")
