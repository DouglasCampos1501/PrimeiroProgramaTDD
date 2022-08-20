# Fazer uma função que receba um número e retorne
# uma string contendo a quantidade de dezenas e unidades.
# • Requisitos:
# • O número deve estar entre 1 e 99.
# • Se o número for menor que 1, retornar “Número inválido”
# • Se o número for maior que 99, retornar “Em construção”
# • Implementar primeiro números de 1 dígito e depois 2 dígitos
# 1 unidade
# 2 unidades
# ...
# 9 unidades
# 10, 20, 30, 40, 50, 60, 70, 80, 90
# 10 == 1 dezena
# 11 == 1 dezena e 1 unidade
# 20 == 2 dezenas
# 25 == 2 dezenas e 5 unidades


def descrever_numero(n):
    if n < 1:
        return "Número Inválido"
    elif n > 99:
        return "Em construção"

    saida = ""
    juncao = " e "
    unidade = n % 10

    if unidade == 1:
        saida += f"{unidade} unidade"
    elif 1 < unidade <= 9:
        saida += f"{unidade} unidades"
    else:
        juncao = ""

    dezena = n // 10
    if dezena == 1:
        saida = f"{dezena} dezena" + juncao + saida
    elif dezena > 1:
        saida = f"{dezena} dezenas" + juncao + saida
    return saida


def test_deve_falhar_quando_numero_menor_que_1():
    assert descrever_numero(0) == "Número Inválido"


def test_deve_falhar_quando_numero_maior_que_99():
    assert descrever_numero(100) == "Em construção"


def test_deve_retornar_1_unidade_caso_N_igual_1():
    assert descrever_numero(1) == "1 unidade"


def test_deve_retornar_X_unidades_caso_N_entre_2_e_9():
    assert descrever_numero(9) == "9 unidades"


def test_deve_retornar_1_dezena_caso_N_igual_10():
    assert descrever_numero(10) == "1 dezena"


def test_deve_retornar_Y_dezenas_caso_N_entre_20_e_90():
    valores = [20, 30, 40, 50, 60, 70, 80, 90]
    for valor in valores:
        assert descrever_numero(valor) == f"{valor // 10} dezenas"


def test_deve_retornar_99():
    assert descrever_numero(99) == "9 dezenas e 9 unidades"

