from frequency import letterFrequency
import functools

# https://www.youtube.com/watch?v=-v6AuD6U2lk
# https://www.digitalocean.com/community/tutorials/read-large-text-files-in-python
file_name = "./samples/portuguese.txt"

# ==================
ERROR_MARGIN = 0.015  # Units
MAX_SIZE = 10
# ==================


def getLettersFrequency(line):
    letterFrequency = {}
    cipherLength = len(line)

    for letter in line:
        # https://realpython.com/python-counter/
        letterFrequency[letter] = letterFrequency.get(letter, 0) + 1

    letterFrequency = dict(
        sorted(letterFrequency.items(), key=lambda item: item[1], reverse=True)
    )

    for letter in letterFrequency:
        letterFrequency[letter] = letterFrequency[letter] / cipherLength

    return letterFrequency


def getIndexOfCoincidence(frequencies):
    return functools.reduce(lambda x, y: x + (y * y), frequencies.values(), 0)


print(
    f"Margem de Erro de {ERROR_MARGIN} = ({0.065 - ERROR_MARGIN}, {0.065 + ERROR_MARGIN})"
)
keySize = 0
cipherParts = []
for length in range(1, MAX_SIZE + 1):
    cipherParts = [[] for _ in range(length)]
    txt_file = open(file_name)
    for line in txt_file:
        idx = 0
        for letter in line:
            cipherParts[idx % length].append(letter)
            idx = idx + 1
    txt_file.close()
    avgIndex = (
        functools.reduce(
            lambda x, y: x + getIndexOfCoincidence(getLettersFrequency(y)),
            cipherParts,
            0,
        )
        / length
    )

    if avgIndex > 0.065 - ERROR_MARGIN and avgIndex < 0.065 + ERROR_MARGIN:
        keySize = length
        print(f"O tamanho da chave é provavelmente {length} - {avgIndex}")
        break

if keySize == 0:
    print(
        f"A média de nenhum grupo ficou entre 0.065 +- {ERROR_MARGIN}(Margem de Erro), considere aumentar a Margem de Erro"
    )
else:
    for i in range(0, keySize):
        print(
            f"Top 5 most frequent in Cipher Part {i+1} [{''.join(cipherParts[i][:length])}...]"
        )
        cipherFrequency = getLettersFrequency(cipherParts[i])
        for letter in list(cipherFrequency.keys())[:5]:
            print(f"{letter} - {(cipherFrequency[letter]*100):.2f}%")
