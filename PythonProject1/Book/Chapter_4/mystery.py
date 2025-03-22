def double(arg):
    print('Before:', arg)
    arg = arg * 2
    print('After:', arg)

def change(arg):
        print('Before:', arg)
        arg.append('more data')
        print('After:', arg)

double(42)
double([1, 2, 3])
double('hello')
print()
change([1, 2, 3])
change(['Dave', 'Paula', 'Kent'])
#change('hello')