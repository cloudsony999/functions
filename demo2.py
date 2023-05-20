def test():
    print('I am test 1')

def test():
    print('I am test 2')

def test():
    print('I am test 3')


test()

def calc(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e,88,99,77,55,True,'esobki'

x,y,z,a,b,c,r,t,i=calc(20,10)
print(x,y,z,a,b,c,r,t,i)

ekta=calc(20,10)

print(type(ekta))

for i in ekta:
    print(i)


def f1(b=True,a=10,f=90.6):
    return type(b),type(a),type(f)


print(f1(12))
print(f1('True'))
print(f1())

def data(b,d,a,c):
    print(type(b),type(d),type(a),type(c))
    print(b,d,a,c)

def a(*a):
    print(a)













