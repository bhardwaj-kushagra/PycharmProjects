if __name__ == '__main__':

    n = int(input())
    carr = map(int, input().split())
    arr = list(carr)
    f_max = arr[0]
    f_ind = 0
    for scores in range(len(arr) - 1):
        if arr[scores + 1] > f_max:
            f_max = arr[scores + 1]
            f_ind = scores + 1
    arr.pop(f_ind)
    print(arr)

    smax = arr[0]
    for scores in range(len(arr) - 1):
        if arr[scores + 1] > smax:
            smax = arr[scores + 1]
    print(smax)

#     n = int(input())
#     carr = map(int, input().split())
#     arr = list(carr)
#     f_max = arr[0]
#     print(arr)
#     print(len(arr))
#     print(f_max)
#     for scores in range(len(arr)-1):
#         print(scores+1)
#     #     if arr[scores] > f_max:
#     #         f_max = arr[scores]
#     # smax = arr[0]
#     # for scores in range(len(arr)-1):
#     #     if arr[scores+1] > smax and arr[scores+1] != f_max:
#     #         smax = arr[scores]
#     # print(smax)




