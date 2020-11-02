from time import time
from random import shuffle
from matplotlib import pyplot as plt
import numpy as np
from digital_search import DigitalSearch
from radix_search_trie import RadixSearchTrie
from patricia import Patricia


FUNC = [DigitalSearch, RadixSearchTrie, Patricia]
FUNC_STR = ["Digital Search Tree", "Radix Search Trie", "Patricia Tree"]


def show_line_graph():
    plt.xticks(data)
    plt.xlabel("size of data")
    plt.ylabel("time")
    plt.legend(FUNC_STR)
    plt.title(f"Measurement Tree Algorithm")
    plt.show()


if __name__ == "__main__":
    data = list(range(100000, 300001, 100000))
    for search_func in range(len(FUNC)):
        end_time = []
        for N in range(len(data)):
            key = list(range(1, data[N]+1))
            s_key = list(range(1, data[N]+1))
            shuffle(key)
            d = FUNC[search_func](data[N])
            for i in key:
                d.insert(i)
            start_time = time()
            for i in s_key:
                result = d.search(i)
                if result == -1 or result == -2 or result != i:
                    print(f'탐색 오류, result = {result}')
            end_time.append(time()-start_time)
            print(
                f'{FUNC_STR[search_func]}, maxb = {d.maxb} 의 실행 시간 (N= {data[N]}) : {end_time[N]:.3f}')

        plt.plot(data, end_time)
    show_line_graph()
