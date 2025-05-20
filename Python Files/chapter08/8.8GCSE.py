party_list = []
x=1
for i in range(5):
  nameandfood = []
  name = input(f"What is the name of your friend #{x}?\n>>> ").capitalize()
  x=x+1
  nameandfood.append(name)
  food = input("What will they bring?\n>>> ")
  nameandfood.append(food)
  party_list.append(nameandfood)

print(f"\n{party_list}\n")
for m in range (5):
  print(f"So {party_list[m][0]} will bring {party_list[m][1]}")