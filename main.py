def enigmaEncrypt():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha = list(alpha)

    def encrypt(text):    
        f = open("/Users/spoovathumkadavil/Desktop/Coding/Class/Encryption/Enigma/wheels/wheel.txt", "r")    
        content = f.readlines()

        stuff = []

        

        for i in content:
            stuff.append(i.strip())
        acc_keys = []    
            
        for i in range(len(stuff)):
            wheel_keys = []
            things = list(stuff[i])
            
            tmp = []
            
            for j in range(len(text)):
                text[j] = things[j]
                a_s = "abcdefghijklmnopqrstuvwxyz"
                e = ""
                for i in things:
                    e += i
                wheel_keys.append(a_s.find(text[j]) - e.find(stuff[j]))
            
            acc_keys.append(wheel_keys)
                
        return [text,acc_keys]
        
    text = input("Text: ")
    if(text == ""):
        text = "the pigeon was very fast"

    text = list(text)    

    text,keys = encrypt(text)
    print(text)
    print(keys)
def enigmaDecrypt(text,keys):
    with open("/Users/spoovathumkadavil/Desktop/Coding/Class/Encryption/Enigma/wheels/wheel.txt", 'r') as file:
        content = file.readlines()
        stuff = []
        for i in content:
            a = i.strip()
            stuff.append(a)
    
    for i in range(len(stuff)):
        for j in range(len(keys[i])):
            # caessaar?     
            text[j] = stuff[i][j+keys[i][j]]
    
    return text

things = enigmaEncrypt()

print(things)