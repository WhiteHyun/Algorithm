def from_input(sort_function, verbose=False):
    """
    >>> 1, 2, 3, 4, 5, 6, 7, 8
    then
    user_input = [1, 2, 3, 4, 5, 6, 7, 8]
    """
    user_input = input("','를 기준으로 수를 나누어 입력하세요: ").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(sort_function(unsorted, verbose))
