from matplotlib import pyplot as plt
import sys
import random
import time
import mergesort
import quicksort
import heapsort

sys.setrecursionlimit(5100)
SORT_TYPE_LENGTH = 3
func_str = ["merge sort", "quick sort", "heap sort"]
sort_type_str = ["random", "sorted", "reversed"]
func = [mergesort.merge_sort, quicksort.quick_sort, heapsort.heap_sort]
RANDOM_TYPE = 1
SORTED_TYPE = 2
REVERSED_TYPE = 3


def calculate_sorted_times(type_num, sort_func, N):
    b = []
    arr = [None]
    if type_num == RANDOM_TYPE:
        for _ in range(N):
            arr.append(random.randint(1, N))
    elif type_num == SORTED_TYPE:
        for j in range(1, N + 1):
            arr.append(j)
    elif type_num == REVERSED_TYPE:
        for j in range(N, 0, -1):
            arr.append(j)
    if sort_func == mergesort.merge_sort:
        b = arr.copy()
        start_time = time.time()
        sort_func(arr, 1, len(arr)-1, b)
        end_time = time.time() - start_time
        check_sort(arr, N)
    elif sort_func == quicksort.quick_sort:
        start_time = time.time()
        sort_func(arr, 1, len(arr)-1)
        end_time = time.time() - start_time
        check_sort(arr, N)
    elif sort_func == heapsort.heap_sort:
        start_time = time.time()
        sort_func(arr, len(arr)-1)
        end_time = time.time() - start_time
        check_sort(arr, N)

    return end_time


def plot_line_graph(spent_time, sorted_type, N):
    for result in range(len(spent_time)):
        plt.plot(N, spent_time[result])
    plt.xticks(N)
    plt.xlabel("size of data")
    plt.ylabel("time")
    plt.legend(func_str)
    plt.title(
        f"Measurement of the alignment time of each sort algorithm ({sorted_type})")
    plt.show()


def plot_bar_graph(sort_type_times, sizeof_data):
    w = 0.3  # width

    plt.bar(range(len(sort_type_times[0])), sort_type_times[0], width=w)
    plt.bar([i+w for i in range(len(sort_type_times[1]))],
            sort_type_times[1], width=w)
    plt.bar([i-w for i in range(len(sort_type_times[2]))],
            sort_type_times[2], width=w)
    plt.xlabel("Sort Type")
    plt.ylabel("time")
    plt.title(
        f"Measurement of the alignment time of each sort algorithm (data = {sizeof_data})")
    plt.legend(sort_type_str)
    plt.xticks([i for i in range(len(sort_type_times[0]))], func_str)
    plt.show()


def plot_bar_graph_sensitivity(sort_type_times, sizeof_data, func_str):
    w = 0.3  # width

    for i in range(len(sort_type_times)):
        plt.bar(i, sort_type_times[i], width=w)
    plt.xlabel("Type")
    plt.ylabel("time")
    plt.title(
        f"{func_str} sensitivity measurement (data = {sizeof_data})")
    plt.legend(sort_type_str)
    plt.xticks([i for i in range(len(sort_type_times))], sort_type_str)
    plt.show()


def check_sort(arr, n):
    is_sorted = True
    for i in range(1, n):
        if arr[i] > arr[i+1]:
            is_sorted = False
        if not is_sorted:
            break
    if is_sorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")
        # print(arr)


if __name__ == "__main__":
    calc_time = []
    select = int(
        input("""
        ======Bar Graph======
        1. merge sort sensitivity
        2. quick sort sensitivity
        3. heap sort sensitivity
        4. Compare 1~3
        =======Line Graph======
        5. random array
        6. sorted array
        7. reversed array

Input>> """))
    if select >= 1 and select <= 3:
        sizeof_data = int(input("number of data?\nInput>> "))
        sort_function = func[select-1]
        for sorted_type in range(1, SORT_TYPE_LENGTH + 1):
            calc_time.append(calculate_sorted_times(
                sorted_type, sort_function, sizeof_data))
        plot_bar_graph_sensitivity(
            calc_time, sizeof_data, func_str[select-1])
    elif select == 4:
        sizeof_data = int(input("number of data?\nInput>> "))
        for sorted_type in range(1, SORT_TYPE_LENGTH + 1):
            sort_type_times = []
            for sort_function in func:
                sort_type_times.append(calculate_sorted_times(
                    sorted_type, sort_function, sizeof_data))
            calc_time.append(sort_type_times)
        plot_bar_graph(calc_time, sizeof_data)
    else:
        data = [100000, 200000, 300000]
        for sort_function in func:
            sort_type_times = []
            for size in data:
                sort_type_times.append(
                    calculate_sorted_times(select-4, sort_function, size))
            calc_time.append(sort_type_times)
        plot_line_graph(calc_time, sort_type_str[select-5], data)
