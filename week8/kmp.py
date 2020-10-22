class KMP():
    """
    KMP 스트링 처리 알고리즘 입니다.
    """

    def __init__(self, p: str, t: str) -> None:
        M = len(p)  # 패턴의 길이
        N = len(t)  # 텍스트의 길이
        self.next = self.__init_next(p, M)
        i, j = 0, 0
        while j < M and i < N:
            while j >= 0 and t[i] != p[j]:
                j = self.next[j]
            i += 1
            j += 1
        if j == M:
            self.answer = i-M
        else:
            self.answer = i

    def __init_next(self, p: str, M: int) -> list:
        next = list(range(M))
        next[0] = -1
        print(f"text: '{p}'")
        i, j = 0, -1
        while i < M:
            next[i] = j
            while j >= 0 and p[i] != p[j]:
                j = next[j]
            i += 1
            j += 1
        print(f"next[before]: {next}")
        return next


# 시간복잡도 O(M+N)
if __name__ == "__main__":
    pattern = "bbaabcabcabcab"
    text = "abcabcabc"
    d = KMP(pattern, text)
    for i in range(1, len(d.next)):
        print(d.next[i], end=' ')
