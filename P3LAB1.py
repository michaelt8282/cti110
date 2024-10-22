# CTI 110
# P3LAB1
# michaelt
# 10/22/24

def main():
    print("Choose Your Own Adventure")
    go_home()

def go_home():
    print("You decide to go home.")
    print("But should you get some food?")
    print("1. Order pizza")
    print("2. Get Chinese")
    choice = int(input())
    if choice == 1:
        get_pizza()
    elif choice == 2:
        get_chinese()

def get_pizza():
print("The pizza is great."):
print("GOOD ENDING")

def get_chinese():
    print("BAD ENDING")


# start the program
main()
