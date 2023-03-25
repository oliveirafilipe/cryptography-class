from frequency import letterFrequency

# https://www.digitalocean.com/community/tutorials/read-large-text-files-in-python
file_name = "./samples/portuguese.txt"

txt_file = open(file_name)
cipherFrequency = {}
cipherLength = 0

for line in txt_file:
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
