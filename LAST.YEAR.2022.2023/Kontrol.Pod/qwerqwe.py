hate_ = love = 0
pl = input()
while pl != 'SILENCE':
    if 'hate' in pl:
        hate_ += 1
    if 'love' in pl:
        love += 1
    pl = input()
if hate_ > love:
    print('To the rain')
elif love > hate_:
    print('To the sun')
else:
    print(' Cloudy')

