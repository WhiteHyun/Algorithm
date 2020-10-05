from sort.sorts import bubble_sort, counting_sort, heap_sort, insertion_sort, merge_sort, quick_sort, radix_sort, selection_sort, shell_sort
from matplotlib import pyplot as plt
import random
import time
from sorts import *

# 선택, 버블, 삽입, 쉘, 퀵, 머지, 힙, 계수, 기수 순서
SORT_STRING = ["Selection Sort", "Bubble Sort", "Insertion Sort", "Shell Sort",
               "Quick Sort", "Merge Sort", "Heap Sort", "Counting Sort", "Radix Sort"]

SORT_FUNCTION = [selection_sort, bubble_sort, insertion_sort, shell_sort,
                 quick_sort, merge_sort, heap_sort, counting_sort, radix_sort]


ARR_TYPE = ["Random", "Sorted", "Reversed", "All"]


def calculate_times(type_index: str, func_index: int, data: list):

    return 0


def line_graph(type_index: str, sort_index: list, data: list):

    calculate_times()

    for result in range(len(spent_time)):
        plt.plot(data, spent_time[result])
    plt.xticks(data)
    plt.xlabel("size of data")
    plt.ylabel("time")
    plt.legend(SORT_STRING)
    plt.title(
        f"201601639 Algorithm ({ARR_TYPE[type_index]})")
    plt.show()


# 1. 그래프 선택(Line, Bar)
# 2. 각 정렬비교할 함수들을 선택 (1, 3, 4, 5 이런 식으로)
# 3. 데이터 개수 정함(5000, 10000, 15000 식으로 진행될 수 있음)
# 4. 배열 종류를 선택, 바 그래프면 전부비교도 가능
