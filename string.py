#Anw of Q1 using function & using docstring
def test1(s):
    """extact index from 1 to 300 with jump of 3"""
    s = s[1:300:3]
    print(s)
    return s
#test1("this is My First Python programming class and i am learNING python string and its function")

##Anw of Q2 using function & using docstring
def test2(s):
    '''reversing the string without using reverse function'''
    s=s[::-1]
    print(s)
    return s
#test2("this is My First Python programming class and i am learNING python string and its function")

##Anw of Q3 using function & using docstring
def test3(s):
    '''split string after conversion in uppercase'''
    s=s.upper()
    s=s.split()
    print(s)
    return s
#test3("this is My First Python programming class and i am learNING python string and its function")

##Anw of Q4 using function & using docstring
def test4(s):
    '''convert string into lower case'''
    s=s.lower()
    print(s)
    return s
#test4("this is My First Python programming class and i am learNING python string and its function")

##Anw of Q5 using function & using docstring
def test5(s):
    '''try to capitalize the string'''
    s=s.capitalize()
    print(s)
    return s
#test5("this is My First Python programming class and i am learNING python string and its function")

##Anw of Q7 using function & using docstring
def test7(s):
    '''example of expandtab'''
    s=s.expandtabs()
    print(s)
    return s
#test7("xyzyu\t12345\tabc")

##Anw of Q8 using function & using docstring
def test8(s):
    '''examples of strip,lstrip,rstrip'''
    #s=s.strip()
    #s=s.lstrip()
    #s=s.rstrip()

    print(s)
    return s
#test8("    tushar   ")

##Anw of Q9 using function & using docstring
def test9(s):
    '''replace string character by another character'''
    s=s.replace('t','z')
    print(s)

#test9('tushar')

##Anw of Q10 using function & using docstring
def test10(s):
    '''string center function'''
    s=s.center(20,'*')
    print(s)
    return s
test10('india')