import random
## here we r going to use random.choice method
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['bali', 'gulkan','jamun', 'ram', 'lakhman']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when)+','+random.choice(who)+' that lived in '+random.choice(residence)+', went to the '+random.choice(went)+' and '+random.choice(happened))
