from datetime import datetime


global pessoaLogada
pessoaLogada = None

def calcular_idade(nascimento):
    atual = datetime.now()
    idade = atual.year - nascimento.year

    # Verificar se ainda não fez aniversário no ano corrente
    if atual.month < nascimento.month or (
            atual.month == nascimento.month and atual.day < nascimento.day):
        idade -= 1

    return idade

def data_para_string(data):

    # Converter a data em uma string com o formato desejado
    data_string = data.strftime("%d/%m/%Y")  # Formato: dia/mês/ano

    return data_string

def string_para_data(data_string):

    formato = "%d/%m/%Y"  # Formato da string de data

    # Converter a string em um objeto datetime
    data = datetime.strptime(data_string, formato)

    return data

def senha_disponivel(lista, senha):
    s = True
    for p in lista:
        if p.senha == senha:
            s = False
    return s

def mesmoMes(data):
    return datetime.now().month == data.month

def diaDaSemanaParaIndice(data):
    """
    Recebe uma data e retorna o indice do treino tipo A, B, C aplicada no sistema da academia
    e retorna o indice correspondente para cada dia e -1 se for domingo
    :param data: datetime
    :return: inteiro
    """
    dia = data.strftime('%A') # atribui o dia da semana da data informada
    if dia in ["Monday", "Thursday"]:
        return 0
    elif dia in ["Tuesday", "Friday"]:
        return 1
    elif dia in ["Wednesday", "Saturday"]:
        return 2
    else:
        return -1

def verificar_data_valida(data):
    data_valida = True

    try:
        datetime(data)
    except ValueError:
        data_valida = False

    return data_valida