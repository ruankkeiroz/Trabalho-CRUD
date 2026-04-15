from modelo import *
from dao import GutinDAO

def exibir_menu():
    print("-" * 30)
    print("Gestão de gutinhos")
    print("-" * 30)
    print("1 - Colocar gutin no freezer")
    print("2 - Mostrar gutin que tem")
    print("3 - Trocar gutin")
    print("4 - Comer gutin")
    print("0 - Sair")
    print("-" * 30)

def main():
    gutinhos = GutinDAO()
    while True:
        exibir_menu()
        opcao = int(input("Digite a opcao desejada: "))

        if opcao == 1:
            Sabor = input("Digite o sabor do gutin: ")
            Localidade = input("Informe onde vende o gutin: ")
            Marca = input("Digite a marca do gutin: ")
            Vendedor = input("Digite o nome do vendedor do gutin: ")
            gutin = Gutin(Sabor, Localidade, Marca, Vendedor,)
            gutinhos.inserir(gutin)

        elif opcao == 2:
            lista_gutin = gutinhos.buscar_todos()
            for gutin in lista_gutin:
                print(gutin)
            
        elif opcao == 3:
            id_gutin = int(input("Digite o ID do gutin a ser trocado: "))
            Sabor = input("Digite o novo sabor do gutin: ")
            Localidade = input("Digite a nova localidade do gutin: ")
            Marca = input("Digite a nova marca do gutin: ")
            Vendedor = input("Digite o novo vendedor de gutin: ")
            gutin_atualizado = Gutin(Sabor, Localidade, Marca, Vendedor, id_gutin)
            gutinhos.atualizar(gutin_atualizado)

        elif opcao == 4:
            id_gutin = int(input("Digite o ID do gutin a ser comido: "))
            gutinhos.comer(id_gutin)

        elif opcao == 0:
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
