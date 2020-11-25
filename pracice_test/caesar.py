plain_text = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Caesar():
    def __init__(self, pattern: str, key: int) -> None:
        self.pattern = pattern  # 평문 텍스트
        self.key = key if key < len(plain_text) else key % len(plain_text)

    def encipher(self) -> str:
        encipher_text = ""
        for i in self.pattern:
            char_code = ord(i)
            if char_code == 32:
                char_code = 96
            elif 65 < char_code < 97:
                char_code += 58
            text_code = char_code + self.key
            if text_code > 148:
                text_code -= len(plain_text)
            if text_code > 122:
                text_code -= 58
            if 90 < text_code < 96:
                text_code += 5
            if text_code == 96:
                text_code = 32
            encipher_text += chr(text_code)
        return encipher_text


if __name__ == "__main__":
    # print(plain_text)
    # for i in plain_text:
    #     print(ord(i), end=", ")
    while(True):
        key = int(input("키: "))
        if key == 999:
            print("프로그램 종료")
            break
        pattern = input("평  문: ")
        d = Caesar(pattern, key)
        print(f"암호문: {d.encipher()}")
        print()
