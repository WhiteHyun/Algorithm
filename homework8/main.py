from huffman import Huffman

if __name__ == "__main__":
    text = "A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS"
    # text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
    d = Huffman(text)
    name = d.encode()
    print(d.decode(name))
