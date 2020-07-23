import re
from collections import defaultdict
import string
from os import remove


def statistic(target_words):
    """
    The function creates statistics of words usage frequency by users
    (list) -> (dict)
    :param target_words: statistics will be formed by users' usage of words from this list
    :return: dict (key — word, value — number of times the user used the corresponding word)
    """
    word = defaultdict(dict)

    with open('data.txt', 'r', encoding='UTF-8') as f:

        for line in f:

            # delete emojis and other symbols, which are obstacles for creating statistics
            emoji_pattern = re.compile("["
                                       u"\U0001F600-\U0001F64F"  # emoticons
                                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                       u"\U00002702-\U000027B0"
                                       u"\U000024C2-\U0001F251"
                                       "]+", flags=re.UNICODE)
            line = emoji_pattern.sub(r'', line)

            # The code below is parsing 'data.txt' information and preprocessing it for statistic's dict creation
            if '\t' in line:
                t = line[:line.index('\t') - 1]
                line = line[line.index('\t') + 1:]

            # delete digits and punctuation signs
            line = ''.join(c.lower() for c in line if c not in string.punctuation + string.digits)
            line = ' ' + line[:-1] + ' '

            for i in target_words:
                temp = ' ' + i.lower() + ' '
                if not i.lower() in word[t].keys():
                    word[t][i.lower()] = line.count(temp)
                if temp in line:
                    word[t][i.lower()] += line.count(temp)
    remove('data.txt')
    return word
