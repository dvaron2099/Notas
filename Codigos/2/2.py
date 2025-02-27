def palindromo(palabra):
    separar = list(palabra)
    reversar = separar[::-1]
    union = "".join(reversar)
    if palabra == union:
        return True
    else:
        return False


print(palindromo('otto'))
print(palindromo('victor'))
