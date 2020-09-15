from matplotlib import pyplot as plt
import bubblesort
import insertionsort
import selectionsort
import shellsort
import random
import time
SORTED_TYPE_LENGTH = 3

sort_functions = [selectionsort.selection_sort, bubblesort.bubble_sort,
                  insertionsort.insertion_sort, shellsort.shell_sort]

sortfunc_str = ["selection sort", "bubble sort",
                "insertion sort", "shell sort"]


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
        print(arr)


def calculate_sorted_times(select_num, sort_func, N=[5000, 10000, 15000]):
    calc_time = []
    for sizeof_data in N:
        arr = [-1]
        if select_num == 1:
            for _ in range(sizeof_data):
                arr.append(random.randint(1, sizeof_data))
        elif select_num == 2:
            for j in range(1, sizeof_data + 1):
                arr.append(j)
        elif select_num == 3:
            for j in range(sizeof_data, 0, -1):
                arr.append(j)
        start_time = time.time()
        arr_sorted = sort_func(arr, len(arr)-1)
        end_time = time.time() - start_time
        check_sort(arr, sizeof_data)
        calc_time.append(end_time)
    if len(calc_time) == 1:
        return calc_time[0]
    else:
        return calc_time


def plot_line_graph(spent_time, sorted_type, N=[5000, 10000, 15000]):
    for result in range(len(spent_time)):
        plt.plot(N, spent_time[result])
    plt.xticks(N)
    plt.xlabel("size of data")
    plt.ylabel("time")
    plt.legend(["selection sort", "bubble sort",
                "insertion sort", "shell sort"])
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
    plt.legend(["random", "sorted", "reversed"])
    plt.xticks([i for i in range(len(sort_type_times[0]))], sortfunc_str)
    plt.show()


def plot_bar_graph_sensitivity(sort_type_times, sizeof_data, func_str):
    w = 0.3  # width

    for i in range(len(sort_type_times)):
        plt.bar(i, sort_type_times[i], width=w)
    plt.xlabel("Type")
    plt.ylabel("time")
    plt.title(
        f"{func_str} sensitivity measurement (data = {sizeof_data})")
    plt.legend(["random", "sorted", "reversed"])
    plt.xticks([i for i in range(len(sort_type_times))], [
        "random", "sort", "reverse"])
    plt.show()


if __name__ == "__main__":
    sort_str = ["random", "sorted", "reversed"]
    calc_time = []
    select = int(
        input("""
        =======Line Graph======
        1. random array
        2. sorted array
        3. reversed array
        ======Bar Graph======
        4. Compare 1~3
        5. selection sort sensitivity
        6. bubble sort sensitivity
        7. insertion sort sensitivity
        8. shell sort sensitivity

Input>> """))

    if select >= 1 and select <= 3:
        for sort_function in sort_functions:
            calc_time.append(calculate_sorted_times(select, sort_function))
        plot_line_graph(calc_time, sort_str[select-1])
    elif select == 4:
        sizeof_data = int(input("number of data?\nInput>> "))
        for sorted_type in range(1, SORTED_TYPE_LENGTH + 1):
            sort_type_times = []
            for sort_function in sort_functions:
                sort_type_times.append(calculate_sorted_times(
                    sorted_type, sort_function, [sizeof_data]))
            calc_time.append(sort_type_times)
        plot_bar_graph(calc_time, sizeof_data)
    elif select >= 5 and select <= 8:
        sizeof_data = int(input("number of data?\nInput>> "))
        sort_function = sort_functions[select % 4 - 1]
        for sorted_type in range(1, SORTED_TYPE_LENGTH + 1):
            calc_time.append(calculate_sorted_times(
                sorted_type, sort_function, [sizeof_data]))
        print(calc_time)
        plot_bar_graph_sensitivity(
            calc_time, sizeof_data, sortfunc_str[select % 4 - 1])
