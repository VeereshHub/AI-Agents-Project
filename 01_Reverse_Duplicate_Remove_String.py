

def reverse_and_duplicate(s):
    # strreverse=s[::-1]
    strreverse = ''
    for char in s:
        strreverse =  char + strreverse
    
    seen=set()
    dupStr=[]
    
    for char in strreverse:
        if char not in seen:
            seen.add(char)
            dupStr.append(char)
    
    return ''.join(dupStr)
    

strUserInput=input("Enter any String:")



returnValue=reverse_and_duplicate(strUserInput)
print(returnValue)