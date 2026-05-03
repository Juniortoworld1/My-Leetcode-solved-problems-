def processStr(s):
    apd = ''
    new= ''
    for i in s:
        if i.isalnum()==True:
            new+=i
        else:
            if i=='%':
                if len(new)==0:
                    pass
                else:
                    for k in range (len(new)-1 , 0 , -1):
                        apd+=new[k]
                    new = apd + new[0]
                    apd = ''
            elif i=="*":
                if len(new)==0:
                    pass
                else:
                    new = new[:len(new)-1]
            elif i=='#':
                if len(new)==0:
                    pass
                else:
                    new = new*2
    return new    


s = "a+b%*"

print(processStr(s))

