def average(array):
    # your code goes here
    New_array = set(array)
    return sum(New_array)/len(New_array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)