def insertion_sort():
    arr = input("Ingrese los números a ordenar separados por espacios: ").split()
    arr = [int(x) for x in arr]  # Convierte los elementos de la lista en enteros
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort())

## Brandon Morales https://www.instagram.com/lewenn19/