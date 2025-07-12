def formatar_data(data):
    meses = ["jan", "fev", "mar", "abr", "mai", "jun", 
             "jul", "ago", "set", "out", "nov", "dez"]
    ano, mes, dia = data
    return f"{dia:02d}/{meses[mes - 1]}/{ano}"

def formatar_hora(hora):
    return f"{hora[0]:02d}:{hora[1]:02d}"

def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):
    for evento in eventos:
        data_evento, hora_evento, descricao = evento
        if de_data <= data_evento <= ate_data:
            data_formatada = formatar_data(data_evento)
            hora_formatada = formatar_hora(hora_evento)
            print(f"{data_formatada} - {hora_formatada}: {descricao}")

agenda = [
    ((2020, 1, 13), (11, 50), 'Renovar identidade'),
    ((2020, 1, 15), (16, 30), 'Fazer compras'),
    ((2020, 1, 25), (8, 45), 'Autenticar documentos'),
    ((2020, 2, 29), (14, 15), 'Prestar concurso'),
    ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),
    ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista'),
]

print("Eventos entre 20/jan/2020 e 17/mar/2020:")
imprimir_eventos(agenda, (2020, 1, 20), (2020, 3, 17))

print("\nEventos até 15/mar/2020:")
imprimir_eventos(agenda, ate_data=(2020, 3, 15))
