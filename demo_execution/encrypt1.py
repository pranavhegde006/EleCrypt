import math
import functools

d = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six",\
     7 : "seven", 8 : "eight", 9 :"nine", 10 :"ten", -1: "dot"}
key = {'a' : 'q' , 'b' : 'w' , 'c' : 'e' , 'd' : 'r', 'e' : 't' , 'f' : 'y', 'g' : 'u', \
       'h' : 'i' , 'i' : 'o' , 'j' : 'p' , 'k' : 'a', 'l' : 's' , 'm' : 'd' ,'n' : 'f', \
       'o' : 'g' , 'p' : 'h' , 'q' : 'j' , 'r' : 'k' ,'s' : 'l'  ,'t' : 'z' ,'u' : 'x', \
       'v' : 'c'  ,'w' : 'v'  ,'x' : 'b' , 'y' : 'n' ,'z' : 'm'}
def encrypt(val):
    counter = 1
    occurence = dict()
    res = []
    res = [(int(x) if x.isdigit() else -1) for x in str(val)]  #enlists the various digits in val
    #print(res)
    for i in range(len(res)):
        res[i]=d[res[i]]
        if(res[i] not in occurence):
            occurence[res[i]]=0          #checks number of times a digit is present in the value
        else:
            occurence[res[i]]+=1        #if a number is repeated, increments the ascii by number of times it occurs
            res[i]=functools.reduce(lambda x,y: x+y,[chr(ord(x)+occurence[res[i]]) for x in res[i]])
        #res[i]=d[res[i]]
    #print("res:",val,res)

    for i in range(len(res)):
        ls = [key[x] for x in res[i]]   #this substitutes the previously obtained values with the key (qwerty)
        res[i] = functools.reduce(lambda x,y: x+y,ls)
    #print(res)
    final = functools.reduce(lambda x,y: x+y,res) #concatenates the encrypted segments into one string
    #print(final)
    return final
