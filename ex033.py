z = int(input('digite um número'))
x = int(input('Digite outro'))
c = int(input('Digite outro'))
if z>x>c:
    print('{} {} {}'.format(z,x,c))
else:
    if x>z>c:
        print('{} {} {}'.format(x,z,c))
    else:
        if c>x>z :
            print('{} {} {}'.format(c,x,z))
        else:
            print('{} {} {}'.format(c,x,z))