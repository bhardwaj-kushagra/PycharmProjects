if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    list1 = student_marks[query_name]
    list2 = [float(names) for names in list1]
    avera = 0
    aver = float(avera)
    for l_items in list2:
        aver +=  l_items/len(list2)
    print("{:.2f}".format(aver))# half an hour wasted cuz of this .2f