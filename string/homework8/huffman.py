CHAR_LENGTH = 27


class Heap:
    """
    힙에 대한 클래스입니다. 해당 힙은 최소 힙으로 구성되어져있습니다.

    Attributes:
        heap (list): 허프만의 빈도수를 가지고 최소힙으로 이루어진 리스트 입니다.
        info (list): 히프 값에 따른 각각의 인덱스가 어느 문자인지를 나타냅니다 각 요소는 정수로 되어있습니다.
    """

    def __init__(self, count: list) -> None:
        self.__heap = [0]*50
        self.__info = [0]*50
        self.__size = 0
        for index in range(0, CHAR_LENGTH):
            if count[index] == 0:
                continue
            self.insert(count[index], index)

    @property
    def heap(self):
        return self.__heap

    @property
    def info(self):
        return self.__info

    @property
    def size(self):
        return self.__size

    def insert(self, count: int, index: int) -> None:
        """
        최소 힙을 갖추며 데이터를 삽입합니다.
        """
        self.__size += 1
        i = self.__size  # 힙 노드 수부터 시작

        # 최소 힙에 맞게 데이터를 옮기는 과정
        while i != 1:
            if count >= self.__heap[i//2]:
                break

            self.__heap[i] = self.__heap[i//2]
            self.__info[i] = self.__info[i//2]
            i //= 2

        self.__heap[i] = count
        self.__info[i] = index

    def pop(self):
        """
        최상위 노드의 info값을 리턴하되 최소힙을 갖춘 후에 리턴합니다.
        """
        temp_heap = self.__heap[self.__size]  # 최하위 노드
        temp_info = self.__info[self.__size]  # 최하위 노드
        index = self.__info[1]
        p = 1  # 부모노드
        x = 2  # 자식노드
        self.__size -= 1  # 힙 크기 1 줄임
        # 최소 힙에 맞게 데이터를 옮기는 과정
        while x <= self.__size:
            if x < self.__size and self.__heap[x] > self.__heap[x+1]:
                x += 1
            if temp_heap <= self.__heap[x]:
                break
            self.__heap[p] = self.__heap[x]
            self.__info[p] = self.__info[x]
            p = x
            x *= 2
        self.__heap[p] = temp_heap
        self.__info[p] = temp_info

        return index

    def is_empty(self) -> bool:
        """
        힙 트리가 비어있는지 확인합니다. 비어있으면 True를 리턴하고 비어있지 않으면 False를 리턴합니다.
        """
        if self.__size == 0:
            return True
        else:
            return False


class Huffman():
    """
    허프만 트리 알고리즘에 해당하는 클래스입니다.

    Attributes:
        text (str): 문자열 값입니다. 이 값을 가지고 허프만 트리 알고리즘이 만들어집니다.
        count (list): text에서 각 문자당 빈도수 나타내는 리스트입니다.
        parent (list): 허프만 트라이가 구현되었을 때 인덱스마다 각 노드의 부모인덱스를 가리킵니다. 
                       자신이 부모노드의 왼쪽자식이면 양수, 오른쪽자식이면 음수로 나타냅니다.
                       속칭 dad라고도 불리웁니다.
        heap (Heap): 힙 트리를 구성합니다. 힙에 대해서는 Heap.__doc__() 명령어로 알아보실 수 있습니다.
        code (list): encoding에 해당되는 각각의 문자 코드를 의미합니다.
        length (list): encoding된 코드에서 사용될 길이를 의미합니다. 코드보다 길이가 길 경우 0으로 대체하여 길이를 맞춥니다.
    """

    def __init__(self, text: str) -> None:
        self.__text: str = text
        self.__count = self.__get_frequency(text)
        self.__parent = [0]*50
        self.__heap = Heap(self.__count)
        self.__code = [0]*27
        self.__length = [0]*27
        self.__end = self.__make_trie()
        self.__make_code_and_length()

    @property
    def text(self):
        return self.__text

    @property
    def count(self):
        return self.__count

    @property
    def parent(self):
        return self.__parent

    @property
    def heap(self):
        return self.__heap

    @property
    def code(self):
        return self.__code

    @property
    def length(self):
        return self.__length

    def __get_index(self, char: str) -> int:
        """
        문자에 따른 정수형 인덱스를 리턴합니다.
        """
        if char == " ":
            return 0
        else:
            return ord(char) - 64

    def __get_frequency(self, text: str) -> list:
        """
        텍스트의 따른 문자 빈도수를 구합니다.

        Returns:
            count (list): 각 문자에 따른 빈도수를 구한 리스트입니다.

        """
        count = [0]*50
        for i in text:
            count[self.__get_index(i)] += 1  # 빈도수 구함
        return count

    def __make_trie(self) -> int:
        """
        허프만 트리를 구축합니다. 기수 탐색 트라이의 개념으로 접근하여 만들어집니다.

        Returns:
            i-1 (int): 트라이의 최상단노드의 인덱스를 나타냅니다. decode에서 사용되어집니다.
        """
        i = CHAR_LENGTH
        while not self.heap.is_empty():
            l_index = self.heap.pop()  # 왼쪽 자식노드가 될 예정
            r_index = self.heap.pop()  # 오른쪽 자식노드가 될 예정

            self.__parent[l_index] = i
            self.__parent[r_index] = -i
            # 각 자식노드의 빈도수를 더함
            self.__count[i] = self.__count[l_index] + self.__count[r_index]

            if not self.heap.is_empty():
                self.heap.insert(self.__count[i], i)
            i += 1
        return i - 1

    def __make_code_and_length(self) -> None:
        """
        구현된 트라이를 가지고 코드와 길이를 구합니다.
        """
        for i in range(CHAR_LENGTH):
            code = 0    # code[k]를 구하기 위해 사용되는 변수
            length = 0  # length[k]를 구하기 위해 사용되는 변수
            digit = 1  # 자리수를 나타내는 변수이며 코드의 값을 구할 때 사용되어집니다.

            if self.__count[i]:
                # parent_index, 자신의 parent값을 인덱스로 사용합니다.
                p_index = self.__parent[i]
                while p_index != 0:  # 최상단 인덱스를 참조할 때 까지
                    if p_index < 0:  # dad값이 음수일 때
                        p_index = -p_index
                        # 1일 때를 음수 값으로 설정했으므로 해당 자리수를 1로 설정
                        code += digit
                    p_index = self.__parent[p_index]  # 다시 parent 참조
                    digit <<= 1  # 자리수 왼쪽 시프트
                    length += 1  # 길이 1 증가
            self.__code[i] = code
            self.__length[i] = length

    def encode(self) -> str:
        encoding_text = ""
        for i in self.__text:
            l = self.__length[self.__get_index(i)]  # 코드값에 따른 길이 리스트
            while l != 0:
                encoding_text += str((self.__code[self.__get_index(i)]
                                      >> l - 1) & 1)
                l -= 1
        return encoding_text

    def decode(self, encoding_text: str) -> str:
        """
        encode된 텍스트를 decode하여 읽을 수 있는 본 텍스트로 리턴합니다.
        """
        decoding_text = ""
        i = 0
        end = self.__end  # 초기 디코드 세팅값
        while i < len(encoding_text):
            if encoding_text[i] == "1":  # 1이면 음수를 붙혀주어야함
                end = -end
            # end값을 가지고 있는 parent의 인덱스를 리턴하여 다시 end에 저장
            end = self.__parent.index(end)
            if end < CHAR_LENGTH:   # 문자노드를 만났을 경우
                # 해당되는 알파벳 또는 spacing 문자 넣어줌
                decoding_text += chr(end + 64) if end != 0 else " "
                end = self.__end  # end를 초기 값으로 세팅
            i += 1

        return decoding_text
