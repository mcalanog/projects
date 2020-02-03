
""" For each character in the input string:
 Form a simpler string by removing the character from the input string
 Generate all permutations of the simpler string recursively (i.e. call the
perm_gen_lex function with the simpler string)
 Add the removed character to the front of each permutation of the simpler string, and
add the resulting permutation to the list """

#helper function; chances a string into a list and a list into a string
def string_list(stringorlist):
    if type(stringorlist)== str:
        list1=[]
        for i in stringorlist:
            list1+=i
        return list1
    if type(stringorlist)== list:
        return ''.join(stringorlist)

#main function
def perm_gen_lex(word):
    if len(word)== 1:#when there is only one item it returns back that item in a list
        return [word]
    if len(word) == 2:
        if type(word)== str:
            ogword=word #when there is 2 items in the word it saves the original two letter formation, (makes sure ogword is a string
            word= string_list(word)
        else:
            ogword=string_list(word)
        word[0], word[1] = word[1], word[0]#switches the index of 2 characters
        word = string_list(word) #changes back to string
        return [ogword, word] #returns both combinations of 2 letters
    else:
        lst = []
        for letter in word: #goes through letters in a word
            inx=word.index(letter)#saves index of letter in word
            minilist = perm_gen_lex(string_list(word[:inx] +word[inx+1:])) #recursion with word besides the letter
            for some in minilist:
                lst+=[str(letter)+str(some)]#add letter back to front of the word
        return lst
print(perm_gen_lex('abcd'))
