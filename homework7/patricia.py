from init import *


class Patricia(Tree):
    """
    탐색 알고리즘 중 패트리샤에 해당하는 클래스입니다.
    Tree를 상속받습니다. Tree에 대한 정보는 Tree.__doc__ 명령어를 사용해주세요.
    """

    def insert(self, key: int) -> int:
        """
        노드를 넣는 함수입니다.

        Args:

            key (int): 노드의 key값을 넣기 위한 파라미터입니다. 

        Returns:
            0 : Success
            -1 : Fail
        """
        try:
            pass
        except:
            return -1  # FAIL
        return 0  # Success

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
        pass

    def check(self, key_list: list, time: float) -> None:
        """
        트리가 정확하게 구축되었는지 확인하여 출력해주는 메서드입니다.
        """
        pass


if __name__ == "__main__":
    d = Patricia()
    keys = [1, 19, 5, 18, 3, 26, 9]
    for i in keys:
        d.insert(i)
