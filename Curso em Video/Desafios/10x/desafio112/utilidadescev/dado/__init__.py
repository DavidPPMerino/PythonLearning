def leiaDinheiro(msg):
    check = True
    while check:
        v = input(msg).strip().replace(",", ".")
        for digits in v.split("."):
            if not digits.isnumeric():
                print("\033[31;1mERRO! Digite apenas números!\033[m")
                check = True
                break
            else:
                check = False
                continue
    return float(v)
