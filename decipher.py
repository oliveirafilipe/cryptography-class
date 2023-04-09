import string
# rot = numero de posicoes que ira alterar
# line[::7] pega todas as primeiras letras divididas em substrings 7 em 7

file_name = "./samples/portuguese.txt"

rot = 12
alphabet = string.ascii_lowercase
alphabet_length = len(alphabet)
txt_file = open(file_name)

result = []

for line in txt_file:
    line = line[::7]
    for letter in line:
        if letter.lower() in alphabet:
            unicode_point = ord("a") if letter.islower() else ord("A")
            start = ord(letter) - unicode_point
            offset = ((start + rot) % len(alphabet)) + unicode_point
            result.append(chr(offset))
        else:
            result.append(letter)


print(result)
