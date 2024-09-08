def fun(str1,s):
    result=""
    for i in range(len(str1)):
        char= str1[i]
        if(char.isupper()):
            result +=chr((ord(char)+s-65)%26+65)
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result
string=input()
k=int(input())
print(fun(string,k))
