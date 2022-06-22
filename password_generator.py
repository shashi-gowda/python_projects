import random
pass_len=int(input())
pass_sent='abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
password=''.join(random.sample(pass_sent,pass_len))
print(password)

peint('hello world')