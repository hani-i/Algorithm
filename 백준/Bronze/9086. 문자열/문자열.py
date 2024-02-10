import sys

if __name__ == '__main__':
     T = int(sys.stdin.readline())
     for _ in range(T):
         str = sys.stdin.readline().rstrip("\n")
         print(f'{str[0]}{str[len(str)-1]}')