from time import time
from random import shuffle
from matplotlib import pyplot as plt

FUNC_STR = ["Digital Search Tree", "Radix Search Trie", "Patricia Tree"]
data = [100000, 200000, 300000]


def show_line_graph():
    plt.xticks(data)
    plt.xlabel("size of data")
    plt.ylabel("time")
    plt.legend(FUNC_STR)
    plt.title(f"Measurement Tree Algorithm")
    plt.show()


if __name__ == "__main__":

    # end_time = [[1.401, 2.825, 4.580], [1.941, 3.977, 7.193], [1.358, 2.946, 4.565]]
    end_time = [[1.740, 2.944, 4.597], [
        1.961, 3.828, 6.738], [1.315, 2.754, 4.318]]
    for i in end_time:
        plt.plot(data, i)
    show_line_graph()
