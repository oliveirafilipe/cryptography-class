from frequency import letterFrequency
import functools

# https://www.youtube.com/watch?v=-v6AuD6U2lk
# https://www.digitalocean.com/community/tutorials/read-large-text-files-in-python
file_name = "./samples/english.txt"
cleantext = ""

# ==================
ERROR_MARGIN = 0.002  # Units
ENGLISH_IOC = 0.067
PORTUGUESE_IOC = 0.075
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


def getKeyLetter(offset, letter):
    return chr(abs(ord(offset) - ord(letter)) + ord("a"))


print(
    f"Margem de Erro de {ERROR_MARGIN} = ({0.065 - ERROR_MARGIN}, {0.065 + ERROR_MARGIN})"
)
keySize = 0
language = ""
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
    if avgIndex > ENGLISH_IOC - ERROR_MARGIN and avgIndex < ENGLISH_IOC + ERROR_MARGIN:
        keySize = length
        language = "en"
        break
    if (
            avgIndex > PORTUGUESE_IOC - ERROR_MARGIN
            and avgIndex < PORTUGUESE_IOC + ERROR_MARGIN
    ):
        keySize = length
        language = "pt"
        break

if keySize == 0:
    print(
        f"A média de nenhum grupo ficou entre 0.065 +- {ERROR_MARGIN}(Margem de Erro), considere aumentar a Margem de Erro"
    )
else:
    print(f"O tamanho da chave é provavelmente {length} - {avgIndex}")
    key = []
    offset = "a" if language == "pt" else "e"
    print(f"O texto está em {'Português' if language == 'pt' else 'Inglês'}")
    print("\nPossíveis letras para cada posição da chave:\n   ", end="")
    for i in range(0, keySize):
        letterFrequency = getLettersFrequency(cipherParts[i])
        listLetterFrequency = [
            list(letterFrequency.keys()),
            list(letterFrequency.values()),
        ]
        # ========================
        print(f"({getKeyLetter(offset, listLetterFrequency[0][0])}", end="")
        if listLetterFrequency[1][0] - listLetterFrequency[1][1] < 0.025:
            print(
                f"|{getKeyLetter(offset, listLetterFrequency[0][1])}",
                end="",
            )
        print(")/", end="")
        # ========================
        key.append(getKeyLetter(offset, listLetterFrequency[0][0]))
    print(f"\nChave Assumida: {''.join(key)}")

txt_file = open(file_name)
count = 0

for line in txt_file:
    for letter in line:
        char = letter
        pos = ord(key[count % len(key)].lower()) - 97
        cleantext += chr((ord(char) - pos - 97) % 26 + 97)
        count += 1

with open("./samples/decipher.txt", 'w') as ret:
    ret.write(cleantext)
