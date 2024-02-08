import sys

if __name__ == '__main__':
    array=[]

    for _ in range(10):
        num = int(sys.stdin.readline())
        array.append(num%42)

    s = set(array)
    print(len(s))