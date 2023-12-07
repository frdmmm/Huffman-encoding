# Node of a Huffman Tree
class Nodes:
    def __init__(self, probability, symbol, left=None, right=None):
        # probability of the symbol
        self.probability = probability

        # the symbol
        self.symbol = symbol

        # the left node
        self.left = left

        # the right node
        self.right = right

        # the tree direction (0 or 1)
        self.code = ''

""" A supporting function in order to calculate the probabilities of symbols in specified data """
def CalculateProbability(the_data):
    the_symbols = dict()
    for item in the_data:
        if the_symbols.get(item) is None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols

""" A supporting function in order to print the codes of symbols by traveling a Huffman Tree """
the_codes = dict()

def CalculateCodes(node, value=''):
    # a Huffman code for the current node
    newValue = value + str(node.code)

    if node.left:
        CalculateCodes(node.left, newValue)
    if node.right:
        CalculateCodes(node.right, newValue)

    if not node.left and not node.right:
        the_codes[node.symbol] = newValue

    return the_codes

""" A supporting function in order to get the encoded result """
def OutputEncoded(the_data, coding):
    encodingOutput = []
    for element in the_data:
        # print(coding[element], end = '')
        encodingOutput.append(coding[element])

    the_string = ''.join([str(item) for item in encodingOutput])
    return the_string

""" A supporting function in order to calculate the space difference between compressed and non-compressed data"""
def TotalGain(the_data, coding):
    # total bit space to store the data before compression
    beforeCompression = len(the_data) * 8
    afterCompression = 0
    the_symbols = coding.keys()
    for symbol in the_symbols:
        the_count = the_data.count(symbol)
        # calculating how many bit is required for that symbol in total
        afterCompression += the_count * len(coding[symbol])
    print("Space usage before compression (in bits):", beforeCompression)
    print("Space usage after compression (in bits):", afterCompression)

def HuffmanEncodingWithBaseTree(the_data, base_tree):
    huffmanEncoding = CalculateCodes(base_tree)
    print("Symbols with codes:", huffmanEncoding)
    TotalGain(the_data, huffmanEncoding)
    encodedOutput = OutputEncoded(the_data, huffmanEncoding)
    return encodedOutput

# Example usage:
base_tree = Nodes(1, '''!@#$%^&*()-=_+[]{}|;':",.<>/?`~\   1234567890abeeeeeeeeyutijhkbnm,cxzxbvnve6438dbxcvbxssstere\\\|abbklaklakASKLJOIUBOIJSDMLKFJDSKLOcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ''')  # Replace this with the actual Huffman tree from another file

the_data = "testing 123 matdis"
print("Original data:", the_data)

encoded_output = HuffmanEncodingWithBaseTree(the_data, base_tree)
print("Encoded output:", encoded_output)
