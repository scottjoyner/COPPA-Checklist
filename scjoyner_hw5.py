from nltk.corpus import wordnet
# syns = wordnet.synsets("program")
line = 0
with open("./policies/PBS_Kids.txt", "r") as pbs:
  line = 0
  for x in pbs:
    print(line)
    print(x)
    line += 1
with open("./policies/gamebra.txt", "r") as gamebra:
  line = 0
  for x in gamebra:
    print(line)
    print(x)
    line += 1
with open("./policies/rvappstudios.txt", "r") as rv:
  line = 0
  for x in rv:
    if x == "":
      print(0)
    print(line)
    print(x)
    line += 1
