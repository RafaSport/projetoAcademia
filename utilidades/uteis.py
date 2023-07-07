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


def string_para_data(data_string):

    formato = "%d/%m/%Y"  # Formato da string de data

    # Converter a string em um objeto datetime
    data = datetime.strptime(data_string, formato)

    return data


def data_para_string(data):
    """
    Converte um objeto datetime em uma string formatada (DD/MM/AAAA).
    :param data: objeto datetime contendo a data a ser convertida
    :return: string formatada da data (DD/MM/AAAA)
    """
    return data.strftime("%d/%m/%Y")


def hora_para_string(data):
    """
    Converte um objeto datetime em uma string formatada (HH:MM).
    :param data: objeto datetime contendo a hora a ser convertida
    :return: string formatada da hora (HH:MM)
    """
    return data.strftime("%H:%M")


def obter_nome_dia_semana(data):
    """
    Obtém o nome do dia da semana em português a partir de um objeto datetime.
    :param data: objeto datetime contendo a data para obter o dia da semana
    :return: string contendo o nome do dia da semana em português
    """
    import calendar

    dias_semana_pt = {
        0: 'Segunda-feira',
        1: 'Terça-feira',
        2: 'Quarta-feira',
        3: 'Quinta-feira',
        4: 'Sexta-feira',
        5: 'Sábado',
        6: 'Domingo'
    }

    numero_dia_semana = data.weekday()
    nome_dia_semana = dias_semana_pt.get(numero_dia_semana, '')
    return nome_dia_semana

def obtem_datas_horas_dia(data, labelData, labelHora, labelDia):
    """
    Atualiza as labels de data, hora e dia da semana com as
    informações obtidas a partir de uma data fornecida.

    :param data: Objeto datetime contendo a data e hora a serem exibidas.
    :param labelData: QLabel que representa a label onde a data será exibida.
    :param labelHora: QLabel que representa a label onde a hora será exibida.
    :param labelDia: QLabel que representa a label onde o dia da semana será exibido.
    """
    # Obter a data formatada
    data_formatada = data_para_string(data)

    # Obter a hora formatada
    hora_formatada = hora_para_string(data)

    # Obter o dia da semana em português
    dia_da_semana = obter_nome_dia_semana(data)

    # Atualizar as labels com as informações obtidas
    labelData.setText(data_formatada)
    labelHora.setText(hora_formatada)
    labelDia.setText(dia_da_semana)


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

from datetime import datetime

def verificar_data_valida(data: datetime):
    data_valida = True

    try:
        datetime.combine(data.date(), datetime.min.time())
    except ValueError:
        data_valida = False

    return data_valida
