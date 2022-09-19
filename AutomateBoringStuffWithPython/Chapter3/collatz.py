import sys
def collatz(number):
    if number % 2 == 0:
        v = number // 2
        print(v)
        return v
    else:
        v = 3 * number + 1
        print(v)
        return v
print('Number to use?')
value = input()
try:
    value = int(value)
except ValueError:
    print('I need an integer!')
    sys.exit()
while True:
    out = collatz(value)
    if(out == 1):
        print('Done!')
        break
    value = out