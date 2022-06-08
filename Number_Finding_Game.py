
n = 18
print("You have 8 turns to find the number that the computer has set for you.\n\tLets Start the Game!")
for i in range(1,8):
    inp = int(input("Enter your choice here : "))
    if inp == n:
        print("CONGRATS!!! you have find a number. The number was : ", n)
        break
    elif inp > n:
        print("Number is smaller than your input.")
        print("Remaining turns are : ", 8-i)
    else:
        print("Number is greater than your input")
        print("Remaining turns are : ", 8 - i)