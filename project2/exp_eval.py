#Name: Maeve Calanog
#CPE 202-05
#Project 2:
#Reformating algebraic expression; using stacks, prioritization of operators


from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    thelist= Stack(30)
    newinput = input_str.split()
    operlist= ['+', '-', '*', '/', '**', '<<', '>>'] #to recall operators throughout function
    if len(newinput)== 0: #if nothing in input nothing gets returned
        return ''
    for item in newinput: #go through all number or operator in input
        if item in operlist: #if it is an operator
            if thelist.size() < 2: #there must be two numbers to preform an operation
                raise PostfixFormatException("Insufficient operands")
            value1= thelist.pop()
            value2= thelist.pop()#pop top two items in list
            if item == '+':
                thelist.push(value2 + value1)
            if item == '-':
                thelist.push(value2 - value1)
            if item == '*':
                thelist.push(value2 * value1)
            if item == '/': #cannot divide by zero
                if value1 == 0:
                    raise ValueError
                thelist.push(value2 / value1)
            if item == '**':
                thelist.push(value2 ** value1)
            if item == '>>' or item == '<<':
                if type(value1) == float or type(value2) == float: #cannot preform operation if a float is used
                    raise PostfixFormatException("Illegal bit shift operand")
                if '-' in str(value1):
                    raise PostfixFormatException("cannot shift with negative number")
                if item == '>>':
                    thelist.push(int(value2) >> int(value1))
                if item == '<<':
                    thelist.push(int(value2) << int(value1))
        elif item.isdigit() or item.replace('-', '', 1).isdigit(): #check that it is a integer or float before putting into list
            thelist.push(int(item))
        else:
            try:
                thelist.push(float(item))
            except ValueError:
                raise PostfixFormatException('Invalid token')
    if thelist.size()>1: #there should be one more number than operator in order to preform this function
        raise PostfixFormatException('Too many operands')
    return thelist.pop() #after going through whole list, only item in stack should be the solution


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    newlist= [] #will store the items until string is complete
    newinput = input_str.split()#string split up into list
    if len(input_str) == 0:
        return ''
    thelist= Stack(30)
    operlist = ['+', '-', '*', '/', '**', '<<', '>>', '(', ')']
    for item in newinput:#go through every number or operator from input
        if item not in operlist: #makes sure its a number or float
            if item.isdigit():
                newlist += [item]
            elif item.replace('-', '', 1).isdigit() or item.replace('.', '', 1).isdigit():
                newlist += [item]
        if item in operlist and thelist.size() > 0: #for any operator and the stack already has something in it
            if item == '+' or item== '-': #lowest priority (anything besides other + - can go on top, in the stack)
                if thelist.peek() != '(':
                    while thelist.size() > 0 and thelist.peek() != '(':
                        next= thelist.pop()
                        if next!= '(':
                            newlist += [next]
                thelist.push(item)
            if item == '*' or item == '/':
                if thelist.peek() == "+" or thelist.peek() == "-" or thelist.peek() == "(":
                    thelist.push(item)
                else:
                    while thelist.size() > 0 and (thelist.peek() != '+' and thelist.peek() != '-' and thelist.peek() != '('):
                        next = thelist.pop()
                        if next != '(':
                            newlist += [next]
                    thelist.push(item)
            if item == "**":
                if thelist.peek() != ">>" and thelist.peek() != "<<":
                    thelist.push(item)
                else:
                    while thelist.size() > 0 and (thelist.peek() == ">>" or thelist.peek() == "<<"):
                        next = thelist.pop()
                        if next != '(':
                            newlist += [next]
                    thelist.push(item)
            if item == ">>" or item == "<<":
                while thelist.size() > 0 and (thelist.peek() == ">>" or thelist.peek() == "<<"):
                    next = thelist.pop()
                    if next != '(':
                        newlist += [next]
                thelist.push(item)
            if item == "(":
                thelist.push(item)
            if item == ")":
                while thelist.size() > 0 and thelist.peek()!= "(":
                    newlist += [thelist.pop()]
                if thelist.size() > 0 and thelist.peek() == "(":
                    thelist.pop()
        elif item in operlist and thelist.size() == 0:
            thelist.push(item)
    while thelist.size() > 0:
        theitem= thelist.pop()
        if theitem != '(':
            newlist += [theitem]
    return ' '.join(newlist)

def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    listinput= input_str.split()
    if len(input_str) == 0:
        return ''
    listinput= list(reversed(listinput))
    thislist= Stack(30)
    operlist = ['+', '-', '*', '/', '**', '<<', '>>', '(', ')']
    for object in listinput:
        if object in operlist and thislist.size() >= 2:
            item1 = thislist.pop()
            item2 = thislist.pop()
            word = [str(item1), str(item2), str(object)]
            thislist.push(" ".join(word))
        elif object.replace('-', '', 1).isdigit() or object.replace('.', '', 1).isdigit():
            thislist.push(object)
    return thislist.pop()
