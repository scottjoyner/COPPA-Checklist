from nltk.corpus import wordnet
# syns = wordnet.synsets("program")

with open("./policies/PBS_Kids.txt", "r") as pbs:
  for x in pbs:
    print(x)
with open("./policies/gamebra.txt", "r") as gamebra:
  for x in gamebra:
    print(x)
with open("./policies/rvappstudios.txt", "r") as rv:
  for x in rv:
    print(x)
