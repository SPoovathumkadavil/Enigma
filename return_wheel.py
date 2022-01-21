import random

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha = list(alpha)

# 10 wheels
for i in range(10):
    # 26 charecters
    tmp_alpha = alpha
    
    random.shuffle(tmp_alpha)
    
    alpha_s = "\n"
    for i in tmp_alpha:
        alpha_s += i
    
    
    wheels = open("wheels/wheel.txt", "r")
    content = wheels.readlines()
    wheels.close()
    
    wheels = open("wheels/wheel.txt", "w")
    content.append(alpha_s)
    wheels.writelines(content)
    wheels.close()