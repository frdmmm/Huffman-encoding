class Nodes:  
    def __init__(self, frequency, symbol, left = None, right = None):  
        self.frequency = frequency
        self.symbol = symbol  
        self.left = left  
        self.right = right  
        self.code = ''  

def CalculateFrequency(the_data):  
    symbols = dict()  
    for item in the_data:  
        if symbols.get(item) == None:  
            symbols[item] = 1  
        else:   
            symbols[item] += 1       
    return symbols  

the_codes = dict()  
  
def CalculateCodes(node, value = ''):  
    # a huffman code for current node  
    newValue = value + str(node.code)  
  
    if(node.left):  
        CalculateCodes(node.left, newValue)  
    if(node.right):  
        CalculateCodes(node.right, newValue)  
  
    if(not node.left and not node.right):  
        the_codes[node.symbol] = newValue  
           
    return the_codes  

def OutputEncoded(the_data, coding):  
    encodingOutput = []  
    for element in the_data:  
        # print(coding[element], end = '')  
        encodingOutput.append(coding[element])  
          
    the_string = ''.join([str(item) for item in encodingOutput])      
    return the_string  
  
def HuffmanEncoding(the_data):  
    symbolWithFreqs = CalculateFrequency(the_data)  
    symbols = symbolWithFreqs.keys()  
    the_nodes = []  
    for symbol in symbols:  
        the_nodes.append(Nodes(symbolWithFreqs.get(symbol), symbol))  
    while len(the_nodes) > 1:  
        # sort based on frequency
        the_nodes = sorted(the_nodes, key = lambda x: x.frequency)  
        right = the_nodes[0]  
        left = the_nodes[1]  
        left.code = 0  
        right.code = 1  
        newNode = Nodes(left.frequency + right.frequency, left.symbol + right.symbol, left, right)  
        the_nodes.remove(left)  
        the_nodes.remove(right)  
        the_nodes.append(newNode)  
    huffmanEncoding = CalculateCodes(the_nodes[0])  
    print("Base tree symbol dictionary: ", huffmanEncoding)  
    encodedOutput = OutputEncoded(the_data,huffmanEncoding)  
    return encodedOutput, the_nodes[0]  

def HuffmanEncodingWithBaseTree(the_data, base_tree):
    the_codes=CalculateCodes(base_tree)
    encodedOutput = OutputEncoded(the_data, the_codes)
    print("Encoded file :", encodedOutput)
    return encodedOutput

def HuffmanDecoding(encodedData, huffmanTree):  
    Root = huffmanTree  
    decodedOutput = []  
    for x in encodedData:  
        if x == '1':  
            huffmanTree = huffmanTree.right     
        elif x == '0':  
            huffmanTree = huffmanTree.left  
        try:  
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None:  
                pass  
        except AttributeError:  
            decodedOutput.append(huffmanTree.symbol)  
            huffmanTree = Root  
          
    string = ''.join([str(item) for item in decodedOutput])  
    return string   

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python main.py <basefile>(txt) <decode or encode>(d or e) <file> (txt to encode, binary to decode)")
        sys.exit(1)
    base = sys.argv[1]
    argument = sys.argv[2]
    filename = sys.argv[3]
    try:
        with open(base, 'r') as file:
            content = file.read()
        _,basetree=HuffmanEncoding(content)
    except FileNotFoundError:
        print(f"TXT file {base} not found.")
        sys.exit(1)
    if argument =='e':
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"TXT file {filename} not found.")
            sys.exit(1)
        encoded=HuffmanEncodingWithBaseTree(content, basetree)
        hasil=encoded.encode('utf-8')
        outputname=input("Enter the file name to store the encoded data: ")
        with open(outputname, 'wb') as file:
            file.write(hasil)
    elif argument =='d':
        try:
            with open(filename, 'rb') as file:
                content = file.read()
                stringcontent=content.decode('utf-8')
        except FileNotFoundError:
            print(f"binary file {filename} not found.")
            sys.exit(1)
        hasil=HuffmanDecoding(stringcontent, basetree)
        print("Decoded Output: ")
        print(hasil)
        write=input("Write to txt? [y/n]")
        if write=='y':
            name=input("Enter file name: ")
            with open(name, 'w') as file:
                file.write(hasil)
    else:
        print("Invalid argument")
        sys.exit(1)
