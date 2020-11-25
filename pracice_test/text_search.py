
class BruteForce():
    def __init__(self, text: str, pattern: str) -> None:
        self.text = text
        self.pattern = pattern

    def find(self):
        i = j = 0
        text_length = len(self.text)
        pattern_length = len(self.pattern)
        while i < text_length:
            if self.text[i] == self.pattern[j]:
                j += 1
            else:
                j = 0
            i += 1
            if j == pattern_length:
                j = 0
                k = i
                while self.text[i] != '"':
                    i += 1
                print(self.text[k:i])


if __name__ == "__main__":
    text = """
    <ul> <li> <a href="mailto:gdhong@hanmail.net">Gildong Hong</a> <li> <a
href="mailto:gsjang@yahoo.co.kr">Gilsan Jang</a> <li> <a
href="mailto:yhkim@naver.com">Younghee Kim</a> <li> <a
href="mailto:cslee@gmail.com">Cheolsu Lee</a> </ul>
"""
    pattern = "mailto:"
    d = BruteForce(text, pattern)
    d.find()
