import random
from init import *
import time


class Patricia(Tree):
    """
    탐색 알고리즘 중 패트리샤에 해당하는 클래스입니다.
    Tree를 상속받습니다. Tree에 대한 정보는 Tree.__doc__ 명령어를 사용해주세요.
    """

    def __init__(self, data_size) -> None:
        super().__init__(data_size)
        self.head.left = self.head
        self.head.right = self.head

    def __bitcmp(self, binary: str, bit: int, cmp_num: str) -> bool:
        try:
            if binary[bit] == cmp_num:
                return True
            else:
                return False
        except:
            return True

    def insert(self, key: int) -> int:
        """
        노드를 넣는 함수입니다.

        Args:

            key (int): 노드의 key값을 넣기 위한 파라미터입니다.

        Returns:2
            0 : Success
            -2 : Fail
        """
        p: Node = self.head
        x: Node = p.right
        temp_node: Node = Node(key, self.maxb)
        i: int = self.maxb - 1
        try:
            # 비교인덱스(compare)만을 비교하며 트리를 따라 내려가는 반복문
            # upward link를 만날 때 까지 반복
            while p.compare > x.compare:
                p = x
                if self.__bitcmp(temp_node.binkey, x.compare, "1"):
                    x = x.right
                else:
                    x = x.left
            # 같은 키 값을 가지는 경우 단순 리턴
            if temp_node.key == x.key:
                return -1
            # 비교할 때 비트가 다른 부분을 찾는 과정
            while self.__bitcmp(x.binkey, i, "1") == self.__bitcmp(temp_node.binkey, i, "1"):
                i -= 1

            p = self.head
            x = p.right
            # 노드 연결 과정
            while p.compare > x.compare and x.compare > i:
                p = x
                if self.__bitcmp(temp_node.binkey, x.compare, "1"):
                    x = x.right
                else:
                    x = x.left

            temp_node.compare = i
            if self.__bitcmp(temp_node.binkey, temp_node.compare, "1"):
                temp_node.left = x
                temp_node.right = temp_node
            else:
                temp_node.left = temp_node
                temp_node.right = x

            if self.__bitcmp(temp_node.binkey, p.compare, "1"):
                p.right = temp_node
            else:
                p.left = temp_node
        except:
            return ERROR
        return SUCCESS

    def search(self, search_key: int) -> int:
        """
        패트리샤 트리 알고리즘에 따라 탐색하는 함수입니다.

        Args:

            search_key (int): 트리 내에서 탐색할 key 값입니다.

        Returns:
            0: Success
            -1: Search Failed
            -2: Search Error
        """
        try:
            p: Node = self.head
            x: Node = p.right
            bin_skey = self.head.key_to_bin(search_key)[::-1]
            while p.compare > x.compare:
                p = x
                if self.__bitcmp(bin_skey, x.compare, "1"):
                    x = x.right
                else:
                    x = x.left
            if search_key != x.key:
                return FAIL
        except:
            return ERROR
        return x.key

    def check(self, key_list: list, time: float) -> None:
        """
        트리가 정확하게 구축되었는지 확인하여 출력해주는 메서드입니다.
        """
        print("=================================================================")
        print(key_list)
        for key in sorted(key_list):
            p = x = self.head.right
            bin_key = self.head.key_to_bin(key)[::-1]
            for i in range(len(bin_key)-1, -1, -1):
                if x.key == key:
                    print(f"key: {x.key}, parents: {p.key}")
                    break
                p = x
                if bin_key[i] == "1":
                    x = x.right
                else:
                    x = x.left

        print(f"""패트리샤 트리의 실행 시간 (N = {len(key_list)}: {time:.3f})
탐색 완료
=================================================================""")


if __name__ == "__main__":
    N = 30000
    key = list(range(1, N+1))
    s_key = list(range(1, N+1))
    # random.shuffle(key)
    d = Patricia(N)
    for i in range(N):
        d.insert(key[i])
    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result != s_key[i]:
            print('탐색 오류')
    end_time = time.time() - start_time
    print(f'내 패트리샤 트리의 실행시간 N = {N} : {end_time:.3f}')
