while True:
    try: 
        while True:
            x = int(input('How many pencils would you like to use:'))
            if x <= 0:
                print('The number of pencils should be positive')
            else:
                break
    except: print('The number of pencils should be numeric')
    else: break
# ----------------
while True:
    y = input('Who will be the first (John, Jack):')
    if y not in ['John', 'Jack']:
        print("Choose between 'John' and 'Jack'")
    else:
        break
#-----------------
l = list()
while x > 0:
    l.append('|')
    x-=1
print(''.join(l))
print(f'{y}\'s turn!')
save = y
if save == "John": save = 'Jack'
elif save == 'Jack': save = 'John'
#------------------
while True:
    if save == 'John':
#---------------------
        while True:
            try:
                x_x = int(input())
            except:
                print("Possible values: '1', '2' or '3'")
            if  0 < x_x <= 3:
                if len(l) < x_x:
                    print('Too many pencils were taken')
                else:
                    break
            else:
                print("Possible values: '1', '2' or '3'")

        if len(l) == x_x:
            print(f'{save} won!')
            break
        while x_x > 0:
            l.pop()
            x_x-=1
        if len(l) <= 0:
            break
        else:
            print(f'{save}\'s turn:')
            print(''.join(l))
            save = 'Jack'
#------------------
    if save == 'Jack':
#---------------------
        while True:
            try:
                x_x = int(input())
            except:
                print("Possible values: '1', '2' or '3'")
            if  0 < x_x <= 3:
                if len(l) < x_x:
                    print('Too many pencils were taken')
                else:
                    break
            else:
                print("Possible values: '1', '2' or '3'")

        if len(l) == x_x:
            print(f'{save} won!')
            break
        while x_x > 0:
            l.pop()
            x_x-=1
        if len(l) <= 0:
            break
        else:
            print(f'{save}\'s turn:')
            print(''.join(l))
            save = 'John'
#--------------