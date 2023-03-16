x = int(input('How many pencils would you like to use:'))
y = input('Who will be the first (John, Jack):')
l = list()
while x > 0:
    l.append('|')
    x-=1
print(''.join(l))
print(f'{y} is going first!')