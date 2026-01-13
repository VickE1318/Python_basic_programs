#function to sum the items
def add_items(perfList):
 sum=0
 for i in perfList:
    sum+=i
 return sum

#user input validation
while True:
    userInput = input("Enter numbers (with spaces in between): ")
    if all(part.isdigit() for part in userInput.split()):
        break
    else:
        print("Invalid input! Please enter only numbers separated by spaces.")

#Data processing
userList = list(map(int,userInput.split()))
print("The entered list is: ",userList )
print("Sum of entered items: ",add_items(userList))
