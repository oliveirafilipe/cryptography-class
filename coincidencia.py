from frequency import letterFrequency

# comentado na aula explicando o trabalho, o tamanho da chave não ultrapassa de 20

file_name = "./samples/portuguese.txt"

txt_file = open(file_name)
cipherFrequency = {}
cipherLength = 0

for line in txt_file:
    line = line[::7]
    cipherLength = len(line)
    for letter in line:
        # https://realpython.com/python-counter/
        cipherFrequency[letter] = cipherFrequency.get(letter, 0) + 1
txt_file.close()

cipherFrequency = dict(
    sorted(cipherFrequency.items(), key=lambda item: item[1], reverse=True)
)

for key in cipherFrequency:
    cipherFrequency[key] = (cipherFrequency[key] / cipherLength) * 100

print("Top 5 most frequent in Portuguese")
for key in list(letterFrequency["portuguese"].keys())[:5]:
    print(f"{key} - {letterFrequency['portuguese'][key]:.2f}%")

print("Top 5 most frequent in Cipher")
for key in list(cipherFrequency.keys())[:5]:
    print(f"{key} - {cipherFrequency[key]:.2f}%")

# necessario substituir o texto para 12 posicoes a frente - % (letra + 12posicoes) % 26

