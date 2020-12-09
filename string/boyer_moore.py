MAX_CHAR_NUM = 26  # 알파벳만을 취급하여 처리하기위해 알파벳 개수인 26 할당
ERROR = -2
FAIL = -1


class BM():
    """
    보이어 무어 스트링 처리 알고리즘 입니다. 스트링 탐색에 사용되며, 알파벳 처리만을 취급하고 있습니다.
    숫자와 알파벳 그 외 아스키 코드에 연관되어있는 것들을 처리하고 싶을 경우 MAX_CHAR_NUM 을 255로 설정, index 메서드를 일부 수정하시면 되겠습니다.

    Attribute:
        text (str): 패턴을 검색할 때 사용되는 문자열입니다.
        pattern (str): text에서 값을 검색하기 위해 사용되는 문자열입니다.
        skip (list): text에서 pattern을 검색할 때, 검색에 실패할 경우 그 당시 pattern의 인덱스의 값을 참조하여
                     skip 값에 따라 pattern의 위치를 옮겨주는 역할을 수행합니다.
    """

    def __init__(self, pattern: str, text: str) -> None:
        self.pattern: str = pattern
        self.text: str = text
        self.skip: list = self.__make_skip()

    def __index(self, char: str):
        if ord(char) == 32:
            return 0
        else:
            return ord(char) - 64

    def __make_skip(self) -> list:
        """
        패턴을 가지고 skip list를 만든 뒤 리턴합니다.
        """
        p_len: int = len(self.pattern)
        skip: list = [p_len]*MAX_CHAR_NUM
        for i in range(p_len):
            skip[self.__index(self.pattern[i])] = p_len-(i+1)
        return skip

    def search(self, start: int) -> int:
        """
        보이어 무어 알고리즘을 이용하여 패턴을 탐색하는 함수입니다.


        Returns:
            -2: 탐색 오류
            -1: 탐색 실패
            etc: 탐색 성공 후 인덱스 리턴
        """
        p_len: int = len(self.pattern)  # 패턴의 길이
        t_len: int = len(self.text)  # 텍스트의 길이
        i = start
        j = p_len - 1
        try:
            while j >= 0:
                while self.text[i] != self.pattern[j]:  # 일치하지 않는 경우
                    # text에서 틀린 문자가 패턴에서 오른쪽으로 부터 몇 번째 위치하는지 값을 반환한다. 이 때, 패턴이 존재하지 않는다면 패턴 길이를 반환한다.
                    k = self.skip[self.__index(self.text[i])]
                    if p_len-j > k:
                        i += p_len-j
                    else:
                        i += k
                    if i >= t_len:
                        return t_len
                    j = p_len-1  # 다른 검사를 위해 패턴의 마지막 인덱스로 재초기화
                i -= 1
                j -= 1
        except:
            return ERROR
        return i+1


if __name__ == "__main__":
    text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
    pattern = 'ATION'
    d = BM(pattern, text)
    pos = 0
    while True:
        pos = d.search(pos)
        if pos >= 0:
            print(f"Pattern\'s Position : {pos}")
            print('String Search Complete!')
        else:
            print("String Search End")
            break
        pos += len(pattern)
