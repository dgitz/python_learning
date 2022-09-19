import time,sys
indent = 0
indentIncreasing = True
width = 20
length = 6
try:
    while True:
        print(' ' * indent,end='')
        print('*' * width)
        time.sleep(0.1)
        if indentIncreasing:
            indent = indent + 1
            if indent == length:
                indentIncreasing = False
        else:
            indent= indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()