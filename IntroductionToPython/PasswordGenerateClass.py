from random import randint

alphabetLowers =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetUppers =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




def Generate_Password(m):
    gen_password =""
    for i in range(m):
        lower_upper_random = randint(0,1)
        if lower_upper_random ==0:
             lower_random = randint(0,25)
             gen_password+=alphabetLowers[lower_random]
        else:
           upper_random = randint(0,25)
           gen_password+=alphabetUppers[upper_random]
        digit_random = randint(0,9)
        gen_password+= str(digits[digit_random])

    return gen_password


def Password_Lists(n, m):
    passwords = list(range(n))
    for i in range(n):
        passwords.append(Generate_Password(m))
    return passwords

