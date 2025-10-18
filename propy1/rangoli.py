alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def print_rangoli(size):
    for i in range(2*n - 1):
        for j in range(4*n -3,-1,-1):
            print(alpha[i])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)




    for i in range(2*n - 1)