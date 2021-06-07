import random as rn

s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen = int(input("Enter the Length of Password: "))

password = "".join(rn.sample(s,passlen))

print(password)
