x = y = z = t = 0
string_x = string_y = string_z = string_t = ""

notacao = "8 9 6 / 1 + - 2 *"
entradas = notacao.split(' ')

pilhasize = 0

for entrada in entradas:
    if entrada in ['+', '-', '*', '/']:
        if pilhasize < 2:
            raise ValueError("falta números")
        if entrada == '+':
            x = y + x
        elif entrada == '-':
            x = y - x
        elif entrada == '*':
            x = y * x
        elif entrada == '/':
            x = y / x

        string_x = f"({string_y} {entrada} {string_x})"

        y = z
        z = t
        string_y = string_z
        string_z = string_t
        string_t = ""
        pilhasize -= 1
    else:
        try:
            valor = int(entrada)
        except ValueError:
            raise ValueError(f"Entrada inválida: {entrada}")
        t = z
        z = y
        y = x
        x = valor
        string_t = string_z
        string_z = string_y
        string_y = string_x
        string_x = entrada
        pilhasize += 1
    print(f"Pilha: T={t}, Z={z}, Y={y}, X={x}")

print(f"Expressão em notação algébrica: {string_x}")
print(f"O resultado da expressão é: {x}")