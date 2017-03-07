print("What do you want to get at the store? Hit enter when you're done.")
list = []



while True:
  a = input()
  if a == "":
    break
  list += [a]
print("Okay, here's your list:")
for x in range(len(list)):
  print(str(x+1) + ". " + list[x])
print("Do you want to remove anything? \ny or n")


def getout(z):
  while True:
    if z in list:
      list.remove(str(z))
      break
    if z not in list:
      print("That's not on the list! Seriously, what do you want to remove?")
      z = input()
      continue

while True:
  yorn = input() 
  if yorn == "y":
    print("What do you want to remove? Print 'nvm' if you've changed your mind.")
    z = input()
    if z == "nvm":
      break
    else:
      getout(z)
      break
  if yorn == "n":
    break
  else:
    print("That wasn't a y or n.")

def alphabet():
  list.sort(key=str.lower) #treats all letters as lowercase, since py is ASCIIbetical and not alphabetical
  
print("Do you want that alphabetized? y or n")
while True:
  a = input()
  if a == "y":
    alphabet()
    break
  if a == "n":
    print("I know, right? Why would you? Anyway, here's your list.")
    break
  else:
    print("That wasn't a y or n")
    continue
for i in range(len(list)):
  print(str(i+1) + ". " + list[i])















