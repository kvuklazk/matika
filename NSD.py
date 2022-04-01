def nsd(list_of_num: list = None, sort_list: bool = True):
    if sort_list:
        list_of_num.sort(reverse=True)
        sort_list = False
    k = list_of_num[1]
    list_of_num[1] = list_of_num[0] % list_of_num[1]
    list_of_num[0] = k
    if list_of_num[1] == 0:
        if len(list_of_num) > 2:
            list_of_num[1] = list_of_num[2]
            nsd(list_of_num, sort_list=True)
        else:
            return list_of_num[0]
    return nsd(list_of_num, sort_list+1)


inp = [12, 3456]
print(nsd(inp))
