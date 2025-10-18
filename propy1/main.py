# def mutate_string(string, position, character):
#     string = string[:position - 1] + character + string[position:]
#     return string
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# dont delete
def count_substring(string, sub_string):
    num = 0
    ##method1
    ss_len = len(sub_string)
    for a in range(len(string)-ss_len+1):
        ##print(string[a:a+ss_len])
        if sub_string== string[a:a+ss_len]:
            num+=1

    ##method2
    # for i in range(len(string)):
    #     for j in range(i, len(string)):
    #         if sub_string == string[i:j + 1]:
    #             num += 1
    return num

