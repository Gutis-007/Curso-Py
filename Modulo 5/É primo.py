num =int(input())



def maior_primo(x):
    for i in range(x):
     if éPrimo(i) == 0:
       primo = i

    if primo != 0:
     print(primo) 
    


def éPrimo(x):
 mult=0
 for count in range(2,x):
    if (x % count == 0):
        False
        mult += 1
 if(mult==0):
    True
 return mult 

maior_primo(num)