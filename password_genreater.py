
import random
import math
print("hello")
print("enter 1 check for password or enter 2  for create a password")
a = int(input())
if a == 1:
    print("password length is 8 b/w to 13")
    password = input("enter your password")
    splch = "! @ # $ % ^ & * + - = * / : \' \" < > . , ? / \ |".split()
    res = (any(list(letter.islower() for letter in password)) and any(list(letter.isupper() for letter in password)) and any(list(letter.isdigit() for letter in password)) and
           len(password) >= 8 and len(password) <= 13 and any(list(letter in splch for letter in password)))
    if res == True:
        print("password is storng")
    else :
        print("password is weak")
if a== 2:
    print("enter number b/w 8 to 13")
    pass_len = int(input())
    if pass_len >= 8 and pass_len <= 13:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_up = alpha.upper()
        num = "1234567890"
        splch = "! @ # $ % ^ & * + - = * / \ :' \" < > . , ? / \ | ( ) [ ] { }".split()
    # alpha 30   alpha_up 20   num 30 splch20
        pa = int(pass_len * 50/100)
        pn = int(pass_len*30/100)
        pau = int(pass_len* 20/100)
        psp = pass_len - (pa + pn + pau)
        password = []
    
        def generate_pass(length, array):
            for i in range(length):
                index = random.randint(0, len(array) - 1)
                character = array[index]
                password.append(character)
    else:
        print("please enter password len b/w 8 to 13")
if pass_len >= 8 and pass_len <= 13:
    generate_pass(pa,alpha)
    generate_pass(pau,alpha_up)
    generate_pass(pn,num)
    generate_pass(psp,splch)
    pp = ""
    for i in password:
        pp = pp + str(i)
    print(pp)
    





    
