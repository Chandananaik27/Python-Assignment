def second_large(arr):
    n=list(set(arr))
    n.sort()
    b=n[-2]
    return b
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(second_large(arr))