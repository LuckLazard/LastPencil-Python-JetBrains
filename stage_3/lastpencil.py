x = int(input('How many pencils would you like to use:'))
y = input('Who will be the first (John, Jack):')
l = list()
while x > 0:
    l.append('|')
    x-=1
print(''.join(l))
print(f'{y}\'s turn!')
save = y
if save == "John": save = 'Jack'
elif save == 'Jack': save = 'John'
while True:
    if save == 'John':
        x_x = int(input())
        while x_x > 0:
            l.pop()
            x_x-=1
        if len(l) <= 0:
            break
        else:
            print(f'{save}\'s turn:')
            print(''.join(l))
            save = 'Jack'

    if save == 'Jack':
        x_x = int(input())
        while x_x > 0:
            l.pop()
            x_x-=1
        if len(l) <= 0:
            break
        else:
            print(f'{save}\'s turn:')
            print(''.join(l))
            save = 'John'