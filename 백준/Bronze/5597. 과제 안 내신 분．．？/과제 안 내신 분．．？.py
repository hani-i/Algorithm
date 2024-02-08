import sys

if __name__ == '__main__':
    array = [0 for i in range(28)]

    for _ in range(28):
        submit = int(sys.stdin.readline())
        array.append(submit)

    for i in range(1,31):
        if i not in array:
            print(i)