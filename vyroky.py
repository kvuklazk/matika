# funkce na vytvoření listu
def create_list(numbs=0):
    final_vector = []
    h = []

    comb_len = pow(2, numbs)

    for q in range(numbs):
        h.append(0)
    for index in range(comb_len):
        m = []
        for lindex in range(numbs):
            # last row
            if h[lindex] < pow(2, (numbs - lindex - 1)):
                m.append(1)

            else:
                m.append(0)
                if h[lindex] >= pow(2, (numbs - lindex - 1)) * 2 - 1:
                    h[lindex] = -1
        for x in range(numbs):
            h[x] += 1

        final_vector.append(m)
    return final_vector


# funkce výrokových spojek
def disjunkce(x, y):
    if x == 1 or y == 1:
        return 1
    else:
        return 0


def konjunkce(x, y):
    if x == 1:
        if y == 1:
            return 1
    return 0


def implikace(x, y):
    if x == 1:
        if y == 0:
            return 0
        else:
            return 1
    else:
        return 1


# funkce pro negaci
def negation(x):
    return 1 - x


def negation_check(o: list, num: str) -> int:
    if num.find('-') == 0:
        num = num.replace('-', '')
        return negation(o[int(num)])
    else:
        return o[int(num)]


def the_right_comb(letters=None, array=None, column=0):
    final_num_vec = []
    column = int(column)
    for i in array:
        if i[column] == 1:
            vector = []
            for m in range(len(letters)):
                vector.append(i[m])
            final_num_vec.append(vector)
    return final_num_vec


def operation(choice='', array=None, a: str = 0, b: str = 0):
    if choice == 'konjunkce':
        for o in array:
            # noinspection PyTypeChecker
            o.append(konjunkce(negation_check(o, a), negation_check(o, b)))
    elif choice == 'disjunkce':
        for o in array:
            # noinspection PyTypeChecker
            o.append(disjunkce(negation_check(o, a), negation_check(o, b)))
    elif choice == 'implikace':
        for o in array:
            o.append(implikace(negation_check(o, a), negation_check(o, b)))
    else:
        print("Operation failed")


def print_list(array=None):
    for w in range(len(array)):
        print(numb_final[w])


def create_udnf(lt=None, lit=None):
    txt = ""
    for lit_i in lit:
        plin = "("
        for lt_p in range(len(lt)):
            plin += lt[lt_p]
            if lit_i[lt_p] == 0:
                plin += "\'"
            plin += " a "
        plin = plin[:-3]
        if lit.index(lit_i) != 0:
            txt += ") v "
        txt += plin
    txt += ")"
    return txt


if __name__ == "__main__":
    print(" Demo - 1 \n DU - 2 \n ")
    # mode = int(input())
    mode = 1
    if mode == 1:
        print("Zadejte velká písmena oddělená mezerou:")
        letters = input()
        letters = letters.split(" ")
        numb_final = create_list(len(letters))
        end = True
        num_of_op = 0
        while end:
            print("Zadejte operaci:\n")
            opp = input()
            print("Zadejte první sloupec:")
            first_column = input()
            print("Zadejte druhý sloupec:")
            second_column = input()
            operation(opp, numb_final, first_column, second_column)
            num_of_op += 1
            print("Konec?\nano - 1\n ne - 0")
            if int(input()) == 1:
                end = 0
            print("Tisknout spravne kombinace?\nano - 1\n ne - 0")
            if int(input()) == 1:
                end = 0
                print("Zadejte sloupec:")
                combinations = the_right_comb(letters, numb_final, int(input()))
                for i in combinations:
                    print(i)
                print("vytvořit ÚDNF?\nano - 1\n ne - 0")
                if int(input()) == 1:
                    print(create_udnf(letters, combinations))

        k = 0
        for i in letters:
            if k < 1:
                print(" " + i, end='')
            else:
                print("  " + i, end='')
            k += 1
        for i in range(2, num_of_op + 2, 1):
            print(" ", i, end='')
        print("")
        for i in range(len(numb_final)):
            print(numb_final[i])

    elif mode == 2:
        numb_final = create_list(3)

        # (A v B’) → (B a C’)
        # [3]
        operation('disjunkce', numb_final,  '0', '-1')
        # [4
        operation('konjunkce', numb_final, '1', '-2')
        # [5]
        operation('implikace', numb_final, '3', '4')

        letters = ['A', 'B', 'C']
        listt = the_right_comb(letters, numb_final, 5)

        print(create_udnf(letters, listt))