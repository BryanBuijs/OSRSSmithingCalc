import csv

def main():
  
  current_xp = get_current_xp()
  ore_amounts = get_ore_amounts()
  has_gauntlet = get_has_gauntlet()
  
  new_xp = calculate_xp(current_xp, ore_amounts, has_gauntlet)
  new_level = get_level(new_xp)

  new_xp_format = "{:,}".format(new_xp)
  print("Your new xp is " + new_xp_format)
  #print("Your new xp is %.2f" % float(new_xp))

  #can also be if new level: IF get_level doesn't return 100 / returns none on line 30
  if new_level < 100:
    print("you new level will be " + str(new_level))
  else:
    print("Your level exceeds 99, congratulations on entering virtual levels!")
    
def get_level(exp_gotten):
  with open("ExpLevel.csv", 'r') as csv_file:
    next(csv_file)
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
      if exp_gotten < int(line[1]):
        return int(line[0])-1
  return 100

# ask for current_xp
def get_current_xp():
  while 1:
    try:
      input_xp = int(input("Enter your current XP: "))
    except ValueError: 
      print("It has to be a number, dumbass")
    else: 
      if input_xp < 1:
        print ("It's supposed to be at least 1, dumbass.")
      else:
        return input_xp

# ask for ore amounts
def get_ore_amounts():
  ore_types = ["Gold", "Mithril", "Adamantite", "Runite"]
  ore_amounts = []
  for ore_type in ore_types:
    while True:
      try:
        value = int(input("How much " + ore_type + " do you have? "))
        break
      except ValueError:
        print("It has to be a rounded number, dumbass.")
    ore_amounts.append(value)
  return ore_amounts

# ask if player has goldsmith gauntlets
def get_has_gauntlet():
  has_gauntlet_input = input("Do you have Goldsmith Gauntlets? y/n ")
  return has_gauntlet_input.lower() in ["y", "yes"]

# calculate the new total xp
def calculate_xp(xp, amounts, has_gauntlet):
  ore_xps = [22.5, 30.0, 37.5, 50.0]
  if has_gauntlet:
    ore_xps[0] = 56.2

  new_xp = xp
  for amount, ore_xp in zip(amounts, ore_xps):
    new_xp += float(amount) * ore_xp
  return new_xp


if __name__== "__main__":
  main()

