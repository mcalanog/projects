class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # stored as an integer - the ASCII character code value
        self.freq = freq  # the freqency associated with the node
        self.left = None  # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq > b.freq:
        return True
    if a.freq == b.freq: #if the frequencies are the same than the order of the characters will determine its order
        if a.char < b.char:
            return True
    return False


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    sumfreq = a.freq + b.freq #parent node will have sum of frequencies
    if a.char > b.char: #the lesser of the characters will be in the parent node
        new = HuffmanNode(b.char, sumfreq)
    else:
        new = HuffmanNode(a.char, sumfreq)
    if a.freq > b.freq: #whichever frequency is less will be to the left
        new.left = b
        new.right = a
    else:
        new.left = a
        new.right = b
    return new


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    file = open(filename, "r") #opens the file that has characters
    freq_list = [0] * 256 #create a list that we will store the frequencies at the index of the character order
    for i in file.read():
        freq_list[ord(i)] += 1 #increment the frequency of the character everytime the character is encountered
    file.close()
    return freq_list


def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    newlist = [] #list will store the nodes of the letters and the frequencies
    if len(char_freq) == 0:
        return None
    for char in range(len(char_freq)): # going through 256 characters
        if char_freq[char] != 0:
            newlist.append(HuffmanNode(char, char_freq[char])) #adds all nodes for characters that are in the file
    while len(newlist) != 1: #using minimum() function, takes the two smallest frequencies and combines them and adds back to list
        min1 = newlist[minimum(newlist)]
        newlist.pop(minimum(newlist))
        min2 = newlist[minimum(newlist)]
        newlist.pop(minimum(newlist))
        newlist.append(combine(min1, min2))
    return newlist[0]


def minimum(list):
    #helper function that takes list of nodes and returns the index of node with smallest frequency
    if list == []:
        return None
    min = 0
    for i in range(len(list)):
        if list[i].freq < list[min].freq:
            min = i
        elif list[i].freq == list[min].freq:
            if list[i].char < list[min].char:
                min = i
    return min


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    thelist = [''] * 256
    return create_code_help(node, '', thelist)


def create_code_help(node, string, list):
    #helpter function for create code, takes the root node and goes to every leaf node; going left adds 0 to string, right adds 1 and once the leaf is reached it adds string to list of all letter code
    if node.left is None and node.right is None:
        list[node.char] = string
    if node.left is not None:
        create_code_help(node.left, string + '0', list)
    if node.right is not None:
        create_code_help(node.right, string + '1', list)
    return list


def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list associated with "aaabbbbcc, would return “97 3 98 4 99 2” """
    thestring = ''
    for index in range(len(freqs)):
        if freqs[index] > 0: # for every nonzero frequency, adds the order of character and frequency to the final string
            if thestring != '':
                thestring += ' '
            thestring += '{} {}'.format(index, freqs[index])
    return thestring


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    input = open(in_file, "r") #open input file
    file = open(out_file, "w+") #create output file
    content = input.read() #save input files information
    input.close()
    if content == '': #if the file is empty it returns an empty file
        file.close()
        return file
    else:
        frequency_list = cnt_freq(in_file) #converts in_file to frequency list
        header = create_header(frequency_list) # creates the header for
        tree = create_huff_tree(frequency_list)
        code = create_code(tree)
        file.write(header + "\n")
        for letter in content:
            file.write(code[ord(letter)])
        file.close()
        return file

def parse_header(header_string):
    #string -> list
    '''takes in input header string and returns Python list (array)
of frequencies (256 entry list, indexed by ASCII value of character)'''
    thelist = [0]*256 #create ASCII list
    stringlist = header_string.split()
    for index in range(len(stringlist)):
        if index % 2 == 0: #every other item is the index and the others is the frequencies
            thelist[int(stringlist[index])] = int(stringlist[index+1])
    return thelist


def huffman_decode(encoded_file, decode_file, tree=None):
    #file -> file
    '''decodes encoded file, writes it to decode file'''
    input = open(encoded_file, "r")  # open input file
    file = open(decode_file, "w+")  # create output file
    line1 = input.readline()
    line2 = input.readline()
    input.close()
    if line1 == '': # if there is an empty file return empty file
        file.close()
        return file
    freq = parse_header(line1)
    tree = create_huff_tree(freq)
    node = tree
    if line2 == '': #if there is only one letter than there is no code
        for i in range(node.freq): #repeat as many frequencies there are
            file.write(chr(node.char))
    else:
        for num in line2: #Follow code left or right depending on code till it reaches a leaf
            if num == '0' and node.left is not None:
                node = node.left
            elif num == '1' and node.right is not None:
                node = node.right
            if node.right is None and node.left is None:
                file.write(chr(node.char)) #when reaches leaf, write letter and go back to root
                node = tree
    file.close()
    return file
