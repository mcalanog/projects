from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            stopwords = open(filename, 'r')
            self.stop_table = HashTable( 191 )
            for word in stopwords:
                self.stop_table.insert(word.strip(), 0)
            stopwords.close()
        except:
            raise FileNotFoundError


    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            openfile = open( filename, 'r' )
            self.concordance_table = HashTable( 191 )
            linecount = 0
            for line in openfile:
                linecount += 1
                word = ''
                for letter in line:
                    if letter.isalpha():
                        word += letter.lower()
                    elif letter == "'":
                        word += ''
                    elif letter in string.punctuation or letter == " " or letter == line[-1]:
                        if word != '' and not self.stop_table.in_table( word ):
                            self.concordance_table.insert( word, linecount )
                        word = ''
            openfile.close()
        except:
            raise FileNotFoundError


    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        output= ''
        file = open( filename, "w+" )
        newlist= self.concordance_table.get_all_keys()
        newlist.sort()
        for item in newlist:
            linecount = list(self.concordance_table.get_value(item))
            linecount.sort()
            stringcount = ''
            for num in linecount:
                if num == linecount[0]:
                    stringcount = str( num )
                else:
                    stringcount  += " " + str( num )
            if item != newlist[-1]:
                output += "{}: {}\n".format(item, stringcount)
            else:
                output += "{}: {}".format( item, stringcount )
        file.write(output)
        file.close()