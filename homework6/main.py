import time
from random import *
from matplotlib import pyplot as plt
import numpy as np
from binary_search import BinarySearch
from redblack import RedBlack
from avl import AVL


# FUNC = [BinarySearch, RedBlack, AVL]
FUNC = [RedBlack, AVL]
# FUNC_STR = ["Binary Tree", "Red Black Tree", "AVL Tree"]
FUNC_STR = ["Red Black Tree", "AVL Tree"]
SORT_STR = ["Random", "Sorted", "Sorted diagonally"]
WIDTH = 0.3


def show_bar_graph():
    plt.xticks(np.arange(0, 13, 3), data)
    plt.xlabel("size of data")
    plt.ylabel("time")
    plt.legend(ALL_STR)
    plt.title(f"Measurement Tree Algorithm")
    plt.show()


def show_line_graph():
    plt.xticks(data)
    plt.xlabel("size of data")
    plt.ylabel("time")
    plt.legend(ALL_STR)
    plt.title(f"Measurement Tree Algorithm")
    plt.show()


if __name__ == "__main__":
    # ALL_STR = []
    # w = -2
    # for i in FUNC_STR:
    #     for j in SORT_STR:
    #         ALL_STR.append(f"{i}({j})")
    # data = list(range(50000, 250001, 50000))
    # for tree in range(len(FUNC)):
    #     for type in range(3):
    #         end_time = []
    #         for N in range(len(data)):
    #             key = list(range(1, data[N]+1))
    #             s_key = list(range(1, data[N]+1))
    #             if type == 0:
    #                 shuffle(key)
    #             elif type == 1:
    #                 key.sort()
    #             else:
    #                 key.sort()
    #                 for j in range(1, len(key)//2, 2):
    #                     key[j], key[-j-1] = key[-j-1], key[j]
    #             d = FUNC[tree]()
    #             for i in key:
    #                 d.insert(i)
    #             start_time = time.time()
    #             for i in s_key:
    #                 result = d.search(i)
    #                 if result == -1 or result != i:
    #                     print('탐색 오류')
    #             end_time.append(time.time()-start_time)
    #             print(
    #                 f'{FUNC_STR[tree]}({SORT_STR[type]})의 실행 시간 (N= {data[N]}) : {end_time[N]:.3f}')

    #         # plt.plot(data, end_time)
    #         plt.bar(np.arange(0, 13, 3)+WIDTH*w, end_time, WIDTH)
    #         w += 1
    # show_bar_graph()
    key = [2, 1, 8, 9, 7, 3, 6, 4, 5]
    s_key = list(range(1, 10))
    d = AVL()
    for i in key:
        d.insert(i)
    start_time = time.time()
    for i in s_key:
        result = d.search(i)
        if result == -1 or result != i:
            print('탐색 오류')
    end_time = time.time()-start_time
    d.check(key, end_time)
