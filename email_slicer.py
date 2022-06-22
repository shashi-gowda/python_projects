email=input('please enter your email address: ')
user=email[:email.index('@')]
domain=email[email.index('@')+1:]
print(f'User: {user}')
print(f'Domain name is: {domain}')

