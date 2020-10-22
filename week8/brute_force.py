def brute_force(p: list, t: list, k: int):
    i, j = k, 0
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1

    if j == M:
        return i-M
    else:
        return i


# 시간복잡도 O(MN)
if __name__ == "__main__":
    text = "ababbabababaabbaababababababbbababababbbaabaa"
    pattern = "aabbaababab"
    M = len(pattern)  # 패턴의 길이
    N = len(text)  # 텍스트의 길이
    K = 0
    while True:
        pos = brute_force(pattern, text, K)
        K = pos + M
        if K < N:
            print(f"패턴이 나타난 위치: {pos}")
        else:
            break
    print("스트링 탐색 종료")
