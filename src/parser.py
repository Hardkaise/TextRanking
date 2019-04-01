import re
import operator


def parse(content):
    tab = re.findall(r"[\w']+", content)
    return count_words(tab)


def count_words(tab):
    count_dic = {}.fromkeys(set(tab), 0)
    for value in tab:
        count_dic[value] += 1
    sorted_d = sorted(count_dic.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_d