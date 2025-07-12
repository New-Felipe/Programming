class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.fome = 0 

    def __str__(self):
        return f"{self.nome} é um {self.especie} e está com nível de fome: {self.fome}"

    def andar(self):
        self.fome += 1
        print(f"{self.nome} foi passear e agora está com fome {self.fome}.")

    def comer(self, quantidade):
        if quantidade >= self.fome:
            print(f"{self.nome} comeu até ficar saciado e deixou o resto da comida no prato.")
            self.fome = 0
        else:
            self.fome -= quantidade
            print(f"{self.nome} comeu {quantidade} unidades de comida e agora está com fome {self.fome}.")

animal = Animal("Toby", "cachorro")

while True:
    print("\nMenu:")
    print("1. Alimentar o animal")
    print("2. Andar com o animal")
    print("3. Mostrar estado atual do animal")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        try:
            quantidade_comida = int(input("Quantas unidades de comida deseja dar ao animal? "))
            animal.comer(quantidade_comida)
        except ValueError:
            print("Por favor, insira um número válido.")
    
    elif opcao == '2':
        animal.andar()
    
    elif opcao == '3':
        print(animal)
    
    elif opcao == '4':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
