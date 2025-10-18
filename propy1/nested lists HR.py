if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])

    fmax = min(lst, key=lambda vals: vals[1])
    lstr = [l_item for l_item in lst if l_item[1] != fmax[1]]

    fmax = min(lstr, key=lambda vals: vals[1])
    new = [l_items for l_items in lstr if l_items[1] == fmax[1]]

    new = dict(sorted(dict(new).items()))

    for key in new:
        print(key)

    #
    # lst = dict(lst)
    # lst = dict(sorted(lst.items()))
    # lst = dict(sorted(lst.items(),lambda itm: itm[1]))
    #
    # print(lst)
    # def swap(alph, beta):
    #
    # for i in range(len(lst)):
    #     for j in range(2):
    #         if lst[i]

    # print(sorted(dict(lst)))
    # print(lst.sort())