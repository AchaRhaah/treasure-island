print("Welcome to treasure island! Your mission is to find the treasure")
route=input("left or right:")
if route =="R":
  print("game over")
elif route =="L":
  choice=input("swim or wait:")
  if choice == "swim":
    print("game over") 
  elif choice == "wait":
    door=input("which door do you want to go through? red,yellow, or blue:")
    if door == "red":
      print("Game over")
    elif door == "yellow":
      print("you win!!!!!")
    else:
      print("game over") 

