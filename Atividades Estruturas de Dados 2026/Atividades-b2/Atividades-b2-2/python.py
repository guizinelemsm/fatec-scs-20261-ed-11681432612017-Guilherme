""""------------------------------------------ *
Fatec
São
Caetano
do
Sul
Atividade
B2 - 1

Author[1681432612017]
Objetivo: X
data: 28 / 04 / 2026
*------------------------------------------ * """

filaAluno = []
filaAdmin = []
filaPrincipal = []
role = 0

class Pedido():
    def __init__(self, role, nome, paginas):
        self.role = role
        self.nome = nome
        self.paginas = paginas

    def __str__(self):
        return f"Função: {self.role} Nome: {self.nome} Paginas: {self.paginas}"


while True:
    opt = int(input("""
    0- definir sua função
    1- fazer um pedido
    2- mostrar filas
    3- reorganizar fila
    4- processar um pedido 
    """))
    if opt == 0:
        if role == 1:
            print("voce é um admnistrador")
        else:
            senha = int(input("insira a senha"))
            if senha == 123:
                role = 1
            else:
                print("senha errada")

    elif opt == 1:
        nome = input("nome do arquivo")
        paginas = int(input("numero de paginas"))
        pedido = Pedido(role, nome, paginas)

        if not filaPrincipal:
            if role == 1:
                filaAdmin.append(pedido)
            else:
                filaAluno.append(pedido)
        else: print("Você não pode adicionar pedidos com a fila ja organizada")

    elif opt == 2:
        print("========filaAluno========")
        for arquivo in filaAluno:
            print(arquivo)
        print("========filaAdmin========")
        for arquivo in filaAdmin:
            print(arquivo)
        print("========filaPrincipal========")
        for arquivo in filaPrincipal:
            print(arquivo)
    elif opt == 3:
        if filaAdmin or filaAluno:
            filaPrincipal = filaAdmin + filaAluno
            filaAdmin.clear()
            filaAluno.clear()
            print("fila organizada, filas antigas limpas")
        else:
            print("filas vazias")

    elif opt == 4:
        if not filaPrincipal:
            print("a fila nao esta organizada")
        else:
            print(filaPrincipal[0].nome)
            print(filaPrincipal[0].role)
            print(filaPrincipal[0].paginas)
            filaPrincipal.pop(0)

