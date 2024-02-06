def rehour(h):
    if h>=24:
        h=h-24
    return h

def main():
    hour, mi = map(int, input().split())
    time = int(input())
    th = time // 60  # 시간
    tm = time % 60  # 분
    hour += th
    hour = rehour(hour)

    if 60 <= (mi + tm):
        hour += 1
        hour = rehour(hour)
        mi = (mi+tm)-60

    else:
        mi+=tm

    print(f'{hour} {mi}')

if __name__ == "__main__":
    main()