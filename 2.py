def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings, key=last_letter)
print (sort_by_last_letter(['hello', 'from', 'a', 'local', 'function']))

g = 'global'
def outer(p='param'):
    l = 'local'
    def inner():
        print(g,p,l) #looks from inner to outer
    inner()

outer()
#outer().inner() wrong

def enclosing():
    def local_func():
        print('local func')
    return local_func

lf = enclosing()
print (lf) #return 'zona de memorie'
print (lf()) #return the print from function + None because of print
lf() #return the print from function

def outer():
    x = 3
    def inner(y):
        return x+y
    return inner

i = outer() #se defineste ca zona de memorie
print (i(2))

print("function factories")
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x,exp)
    return raise_to_exp

square = raise_to(2)
print (square(3))

#=====
#decorators
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print (get_text("John"))

#=====
#ZeroDivisonError
try:
    print(1/0)
except ZeroDivisionError:
    print("No se puede")

def my_error(level):
    if level < 2:
        print(level)
    else:
        raise ValueError('test test')

try:
    my_error(3)
except ValueError as e:
    print ('lalala')
    print (e.args)
