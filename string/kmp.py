class KMP():
    """
    KMP 스트링 처리 알고리즘 입니다. 스트링 탐색에 사용됩니다.

    Attribute:
        text (str): 패턴을 검색할 때 사용되는 문자열입니다.
        pattern (str): text에서 값을 검색하기 위해 사용되는 문자열입니다.
        next (list): text에서 pattern을 검색할 때, 검색에 실패할 경우 그 당시 pattern의 인덱스의 값을 참조하여
                     next 값에 따라 pattern의 위치를 옮겨주는 역할을 수행합니다.
    """

    def __init__(self, pattern: str, text: str) -> None:
        self.pattern: str = pattern
        self.text: str = text
        self.next: list = self.__make_next()

    def __make_next(self) -> list:
        """
        패턴을 가지고 스트링 검색에 이용할 next 를 구하는 함수입니다.
        재시작 위치 알고리즘 수행 후 개선된 유한 상태 장치를 구하여 리턴합니다.

        Variable:
            p_len (int): 패턴의 길이입니다.
            next (list): 클래스의 속성으로 리턴될 리스트 변수입니다.
            pos1, pos2 (int, int): 재시작 위치를 구하기 위해 패턴의 인덱스로 적용되는 변수입니다.    
        """
        p_len: int = len(self.pattern)
        next: list = [-1] * p_len
        pos1, pos2 = 1, 0
        for i in range(1, p_len):
            # 재시작 위치 알고리즘 수행
            next[i] = pos2
            if self.pattern[pos1] != self.pattern[pos2]:
                pos2 = 0
            else:
                pos2 += 1
            pos1 += 1
            # 개선된 유한 상태 장치 구현
            if self.pattern[i] == self.pattern[next[i]]:
                next[i] = next[next[i]]
        return next

    def search(self) -> None:
        """
        KMP 알고리즘을 이용하여 패턴을 탐색하는 함수입니다.
        """
        i, j = 0, 0
        p_len: int = len(self.pattern)
        t_len: int = len(self.text)
        while j < p_len and i < t_len:
            while j >= 0 and self.text[i] != self.pattern[j]:
                j = self.next[j]
            i += 1
            j += 1
        if j == p_len:
            return i - p_len
        else:
            return i


# 시간복잡도 O(M+N)
if __name__ == "__main__":
    pattern = "abracadabra"
    text = "bbaabcababracadabracabcababracadabra"
    d = KMP(pattern, text)
    print(f"pattern: {pattern}")
    print(f"next: {d.next}")
    print(f"처음으로 발견된 패턴의 인덱스 위치는 {d.search()}")
