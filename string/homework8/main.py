from huffman import Huffman

if __name__ == "__main__":
    text = "A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS"
    # text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
    d = Huffman(text)
    name = d.encode()
    print("---------encoded text---------")
    for i in range(0, len(name), 50):
        print(name[i:i+50])
    print("------------------------------")
    print(f"decode(encode_text) = {d.decode(name)}")
