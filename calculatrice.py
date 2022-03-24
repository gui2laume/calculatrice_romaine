import os


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def verification(element):
    Lettres_Romaines = "M D C L X V I"

    for i in element:  # verifier pour chaque lettres dans l'element

        if i in Lettres_Romaines:  # si il existe dans les lettres romaines (chiffres)
            pass
        else:
            return False  # et si il n'exsite pas ben erreur

    return True  # et si pas d'erreur détecter ben true


def sort(elements):
    # on a ex: "MDXC"
    L = (("&M&", 1000), ("&IM&", 999), ("&VM&", 995), ("&XM&", 990), ("&LM&", 950), ("&CM&", 900), ("&D&", 500),
         ("&ID&", 499), ("&VD&", 495), ("&XD&", 490), ("&LD&", 450), ("&CD&", 400), ("&C&", 100), ("&IC&", 99),
         ("&VC&", 95), ("&XC&", 90), ("&L&", 50), ("&IL&", 49), ("&VL&", 45), ("&XL&", 40), ("&X&", 10), ("&IX&", 9),
         ("&V&", 5), ("&IV&", 4), ("&I&", 1))

    elements = list(elements)
    result = []
    t = 999999
    for element in elements:
        for l in L:

            if element == l[0].split("&")[1]:

                if l[1] > t:
                    result[-1] = "&" + result[-1].split("&")[1] + l[0].split("&")[1] + "&"
                    break
                else:
                    result.append(l[0])
                    t = l[1]
                    break

    return result  # on doit return ["&M&","&D&","&XC&"]


def parse_roman_number(tr_element):
    for i in tr_element:
        if not verification(str(i)):  # Verfier si chaques chiffres son bien ecrit et avec des lettres existantes
            return False, 0

    # global L
    L = (("&M&", 1000), ("&IM&", 999), ("&VM&", 995), ("&XM&", 990), ("&LM&", 950), ("&CM&", 900), ("&D&", 500),
         ("&ID&", 499), ("&VD&", 495), ("&XD&", 490), ("&LD&", 450), ("&CD&", 400), ("&C&", 100), ("&IC&", 99),
         ("&VC&", 95), ("&XC&", 90), ("&L&", 50), ("&IL&", 49), ("&VL&", 45), ("&XL&", 40), ("&X&", 10), ("&IX&", 9),
         ("&V&", 5), ("&IV&", 4), ("&I&", 1))

    n = [0, 0]

    tr_element[0] = sort(tr_element[0])
    tr_element[1] = sort(tr_element[1])

    for i in range(0, 2):  # Pour chaques nombres

        x = 0  # Posistion ou on en est dans la traduction
        try:
            for t in L:
                while t[0] in tr_element[i][x]:
                    n[i] += t[1]
                    x += 1
        except:
            pass

    return n[0], n[1]  # Renvoyer les nombre traduits


def write_as_roman_number(tr_element):
    L = (
        ("M", 1000), ("IM", 999), ("VM", 995), ("XM", 990), ("LM", 950), ("CM", 900), ("D", 500), ("ID", 499),
        ("VD", 495),
        ("XD", 490), ("LD", 450), ("CD", 400), ("C", 100), ("IC", 99), ("VC", 95), ("XC", 90), ("L", 50), ("IL", 49),
        ("VL", 45), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))
    resultR = ""

    for i in L:  # Pour chaques lettres d'unités romaines

        if tr_element >= i[1]:  # Si le tr_element est plus grand que la valeur ou on est alors:

            v = tr_element // i[1]

            resultR = resultR + i[
                0] * v  # Rajouter a la traduction la lettre qui vient just d'etre plus grand ou egal au nombre
            tr_element -= i[1] * v  # Enlever a tr_element la valeur que on a ecrit en lettre

            if tr_element == 0:
                break

    return resultR


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def find_operation(x):
    y = ""  # Bon la ya pas trop grand chose a expliquer , le code parle de lui meme
    if "+" in x: y = y + "+"
    if "-" in x: y = y + "-"
    if "*" in x: y = y + "*"
    if "/" in x: y = y + "/"
    if len(y) > 1:
        return y, True  # le true sert a dire que ya plus qu'un symbol
    else:
        return y, False


def do_operation(symbol, n1, n2):
    match symbol:  # Faire le calcule selon le symbol

        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            if n2 != 0:
                return n1 // n2
            else:
                return ""  # Si division par 0


def single_letter(x):
    x, y = parse_roman_number([x, "I"])
    del y

    if not x:
        error(1)
    else:
        x = write_as_roman_number(x)
        print("= " + x)


def execute_command(command):
    symbol, more_then_one = find_operation(command)

    if more_then_one:  # Si il y a plus qu'un symbol
        error(3)

    elif symbol == "":  # Si il n'y a pas de symbol
        single_letter(command)

    elif len(command.split(symbol)) == 2:  # Si du coté simbol opération est normale

        n1, n2 = parse_roman_number(command.split(symbol))  # Traduction de Romain en normal pour les deux nombres

        # si lettres inexsitantes ou mal composées va raporter false a n1 et 0 a n2
        if not n1 and n2 == 0:
            error(1)
            return

        result = do_operation(symbol, n1, n2)  # Calculer l'opération en nombre normals

        if str(result) == "":
            error(5)
        elif result > 0:  # Si le resutlat est positif on va le traduire en nombre romain
            print(f"= {write_as_roman_number(result)}")
        elif result == 0:
            print("= NUL")


        else:  # result negatif error
            error(2)

    else:  # Si l'opération a une syntax fausse
        error(0)


def error(x):
    error_msg = (
        "Invalid Operation [ex:'NumsSymbolNums'] [Symbol: +;-;*;/] [Nums: 'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, '':0]",
        "Invalid Letters Or Order [ex:'NumsSymbolNums'] [Symbol: +;-;*;/] [Nums: 'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, '':0]",
        "Negatif Result", "Opération Can't have more than one symbol [Symbol: +;-;*;/] ", "UnKnow", "Division par 0")
    print(colored(255, 128, 0, "Error: " + error_msg[x]))


def input_command():
    print()
    return "".join(str(input(colored(0, 153, 0,
                                     "Calculatrice: "))).upper().split())  # Demander le calcul et le mettre en maj et supprimer les espaces innutiles


if __name__ == '__main__':

    clear_console()

    while True:

        command = input_command()

        match command:
            case "EXIT":
                exit()
            case _:

                try:
                    execute_command(command)
                except:
                    error(4)
