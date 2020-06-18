import math
import functools

d = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six",\
     7 : "seven", 8 : "eight", 9 :"nine", 10 :"ten", -1: "dot"}
key = {'a' : 'q' , 'b' : 'w' , 'c' : 'e' , 'd' : 'r', 'e' : 't' , 'f' : 'y', 'g' : 'u', \
       'h' : 'i' , 'i' : 'o' , 'j' : 'p' , 'k' : 'a', 'l' : 's' , 'm' : 'd' ,'n' : 'f', \
       'o' : 'g' , 'p' : 'h' , 'q' : 'j' , 'r' : 'k' ,'s' : 'l'  ,'t' : 'z' ,'u' : 'x', \
       'v' : 'c'  ,'w' : 'v'  ,'x' : 'b' , 'y' : 'n' ,'z' : 'm'}

def decrypt(val):
    counter = 1
    location = dict()
    end = ""
    tab = dict()
    for i in key:
        #print(i,":",key[i],end="")
        if(key[i] not in tab):
            tab[key[i]] = i     #done to reverse the keys and values of the dictionary 'key'
    for i in range(len(val)):
        end = end+ tab[val[i]]  #this reverses the substitution process done in the encryption stage
    #print()

    #print(end)

    for i in d:
        if(end.find(d[i])!=-1):
            location[d[i]]=[]
            location[d[i]].append(end.find(d[i])) #finds the index of the first occurence of a known word (number present in dict d)
    #print(location)
    order = sorted(location.values())
    #print(order)
    done = ""
    for i in order:
        word = list(location.keys())[list(location.values()).index(i)] #obtains the key from the value of dictionary keys
        #print(word)
        end = end.replace(word,str(list(d.keys())[list(d.values()).index(word)]))
        end = end.replace("-1",'.')

    #print(end.replace('.',''))
    #print(end.replace('.','').isnumeric())
    if((end.replace('.','').isnumeric()) == True):
        #print(end)
        return end
    else:
        remaining = functools.reduce(lambda x,y: str(x)+str(y), list(filter(lambda x: x.isalpha(),end)))
        #print(end)
        #print(remaining)
        del location['dot'] #location of dot is taken care of by end
        #print(location)
        #left_keys = [*location]
        #print(left_keys)
        counter = 0
        while(counter<=5):
            for i in location:
                val = location[i]
                increment = functools.reduce(lambda x,y: x+y,[chr(ord(x)+counter) for x in i])
                if(end.find(increment)!= -1 ):
                    #print(increment,":",val)
                    end = end.replace(increment,str(list(d.keys())[list(d.values()).index(i)]))
            #print(location)
            counter+=1
        #print(end)
        return end
