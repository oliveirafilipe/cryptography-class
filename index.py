from frequency import letterFrequency
import functools

# https://www.youtube.com/watch?v=-v6AuD6U2lk
# https://www.digitalocean.com/community/tutorials/read-large-text-files-in-python
file_name = "./samples/portuguese.txt"

# ==================
ERROR_MARGIN = 0.015  # Units
MAX_SIZE = 10
# ==================


def getIndexOfCoincidence(line):
    cipherFrequency = {}
    cipherLength = len(line)

    for letter in line:
        # https://realpython.com/python-counter/
        cipherFrequency[letter] = cipherFrequency.get(letter, 0) + 1

    cipherFrequency = dict(
        sorted(cipherFrequency.items(), key=lambda item: item[1], reverse=True)
    )

    for key in cipherFrequency:
        cipherFrequency[key] = cipherFrequency[key] / cipherLength

    return functools.reduce(lambda x, y: x + (y * y), cipherFrequency.values(), 0)


print(
    f"Margem de Erro de {ERROR_MARGIN} = ({0.065 - ERROR_MARGIN}, {0.065 + ERROR_MARGIN})"
)
isSizeFound = False
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
        functools.reduce(lambda x, y: x + getIndexOfCoincidence(y), cipherParts, 0)
        / length
    )

    if avgIndex > 0.065 - ERROR_MARGIN and avgIndex < 0.065 + ERROR_MARGIN:
        isSizeFound = True
        print(f"O tamanho da chave é provavelmente {length} - {avgIndex}")

if not isSizeFound:
    print(
        f"A média de nenhum grupo ficou entre 0.065 +- {ERROR_MARGIN}(Margem de Erro), considere aumentar a Margem de Erro"
    )
