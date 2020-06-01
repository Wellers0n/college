def main():

    def menu():
        print('===================================================')
        print('\n PRESSIONE UM NúMERO PARA ESCOLHER UMA OPÇÃO \n')
        print('(1) - Mostrar lista')
        print('(2) - Incluir elemento')
        print('(3) - Remover elemento')
        print('(4) - Apagar todos os elementos da lista.')
        print('(5) - EXIT.')
        print('=================================================== \n')

    arr = []

    while True:
        menu()
        option = int(input('Digite um número: '))

        if option == 1:
            print(f'\n - Lista: {arr} \n')

        if option == 2:
            valueToList = input('\n Digite um valor para a lista: ')
            arr.append(valueToList)
            print('\n - Incluido na lista com sucesso \n')

        if option == 3:
            inputValueRemove = input('\n Digite o nome do valor que deseja remover: ')
            for value in arr:
                if value == inputValueRemove:
                    arr.remove(inputValueRemove)
                    print('\n - Removido com sucesso!')
                elif value != inputValueRemove:
                    print('\n - Valor não encontrado')

        if option == 4:
            arr = []
            print('\n - Todos elementos apagados com sucesso \n')


        if option == 5:
            print('\n - EXIT! \n')
            break

        elif option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
            print('\n - Digite um valor válido de 1 a 5 \n')



main()
