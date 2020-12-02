import time


def from_input(insert_function, search_function, verbose=False):
    """
    Params:
        void insert_function(str, bool): A function that processes user input.
    """

    input_keys = map(lambda x: x.strip(),
                     input("','를 기준으로 나누어 입력하세요: ").split(','))
    search_key = input("찾고자 하는 key 값을 입력하세요: ").strip()

    for key in input_keys:
        insert_function(key, verbose)

    start = time.perf_counter()
    found = search_function(search_key, verbose)
    end = time.perf_counter()

    elapsed = end - start

    print(f"Search finished in {elapsed}s.")
    print(f"Key is {'found' if found else 'not found'}")
