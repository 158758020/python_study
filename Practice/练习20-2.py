str1 = "AAAAyAAAyAAAsAAAxAAAlAAxAy123AAAxAAA"

def findPwd(str1):
    length = len(str1)
    temp = ""
    
    for i in range(3,length-3):
        if str1[i].islower():
            if (str1[i-3:i].isupper()) and (str1[i+1:i+4].isupper()):
                if i ==3 or i == length - 4:
                    temp += str1[i]
                    continue
                if (not (str1[i-4:i].isupper())) and (not (str1[i+1:i+5].isupper())):
                    temp += str1[i]
    print("密码是",temp)
            
findPwd(str1)
    
