import numpy as np
import matplotlib.pyplot as plt
from statistic import statistic


def make_hist(target_words):
    """
    This functions creates static's histogram plot in .jpg
    :param target_words: parameter to pass it to statistic function
    :return: None
    """
    word_dict = statistic(target_words)

    # For each target word and for each user draws: user, word (x) — number of usages (y)

    bars = [(key, i) for key, item in word_dict.items() for i in item]
    height = [i for key, item in word_dict.items() for i in item.values()]
    y_pos = np.arange(len(bars))
    x_pos = np.arange(max(height) + 1)
    plt.barh(y_pos, height, color='green', edgecolor='black')
    plt.yticks(y_pos, bars)
    plt.xticks(x_pos)
    plt.tight_layout()
    plt.savefig('tg_plot.jpg')

