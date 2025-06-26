# Questão 1 - Você está desenvolvendo um sistema básico de controle de horas trabalhadas para uma pequena empresa. 
# Crie um programa que permita aos funcionários registrar o horário de entrada e saída, calcular a quantidade 
# total de horas trabalhadas por dia e também por semana. Utilize o laço de repetição “while” para tornar o 
# programa mais interativo.

horasTotaisSemana = 0

print('\nBem-vindo ao Sistema de Controle de Horas Trabalhadas!')

iniciar = int(input('Você deseja iniciar os regitros de horas trabalhadas (1 - SIM  |  2 - NÃO)? '))

while iniciar == 1:
    print('\nOpções:')
    print('1 - Registrar entrada.')
    print('2 - Registrar saída.')
    print('3 - Verificar horas trabalhadas no dia.')
    print('4 - Verificar horas trabalhadas na semana.')

    opcao = int(input('\nEscolha uma opção (1 a 4): '))

    if opcao == 1:
        entrada = int(input('Informe a hora de entrada (hora cheia - Formato 24 horas): '))
        print(f'Horário de entrada registrado às {entrada} horas.')
    
    elif opcao == 2:
        saida = int(input('Informe a hora de saída (hora cheia - Formato 24 horas): '))
        print(f'Horário de saída registrado às {saida} horas.')
        horasTrabalhadasDia = saida - entrada
        horasTotaisSemana = horasTotaisSemana + horasTrabalhadasDia
    
    elif opcao == 3:
        print(f'Horas trabalhadas hoje: {horasTrabalhadasDia}.')
    
    elif opcao == 4:
        print(f'Total de horas trabalhadas na semana: {horasTotaisSemana}.')

    else:
        print('Opção inválida. Tente novamente.')
    
    iniciar = int(input('Você deseja continuar com os regitros de horas trabalhadas (1 - SIM  |  2 - NÃO)? '))