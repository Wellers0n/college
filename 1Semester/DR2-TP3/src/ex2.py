def main():
    arr = []
    for value in range(10):
        inputValue = input('Digite uma palavra: ')
        arr.append(inputValue)


    for value in reversed(arr):
        print(value)


main()
