import random
starters = ["Bread and Extra Virgin Olive Oil (Optional Balsamic)", "Buratta", "Bruschetta"]
mains = ["(Award Winning) Pasta", "Pizza", "Prawns"]
desserts = ["Tiramisu", "Gelato", "Crêpes Suzettes"]

customername = input("Please enter your name:\t")
print(f"Hello {customername}, I will choose a random meal for you!")

starterschoice  = random.randint(0,len(starters)-1)
mainschoice  = random.randint(0,len(mains)-1)
dessertschoice  = random.randint(0,len(desserts)-1)

print(f"You will have {starters[starterschoice]} for your starter, {mains[mainschoice]} for your main and {desserts[dessertschoice]} for your desserts")
