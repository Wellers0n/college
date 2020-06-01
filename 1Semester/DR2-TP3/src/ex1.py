import pygame

def main():
    arr = []

    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.append(4)
    arr.append(6)
    print(f'before: {arr}')
    for value in arr:
        value



        if value == 6 or value == 3:
            arr.remove(value)


    print(f'after: {arr}')
    print(f'Length list: {len(arr)}')
main()
