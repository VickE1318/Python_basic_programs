''''''

def length_finder(string):
    count = 0
    for x in string:
        count+=1
    return count
    
userString = input("Enter the string: ")
print("The length of the string you entered:",length_finder(userString))

#check program

i=1
while (i>0):
 reVerify=input("Do you want to reverify (Yes/No): ")
 if reVerify == 'Yes':
   length = len(userString)
   print("The length of the string you entered:",length)
   break
 elif reVerify == 'No':
   print("Thanks for using!")
   break
 else: 
   print("Entered input is not valid! Enter again")



 