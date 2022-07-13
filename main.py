# Contact book
print("A SIMPLE CONTACT BOOK")

# Create lists
names = []
ph_nos = []
emails = []

# Check for error
try:
    rows = int(input("How many contact do you want to add? "))
    
    for i in range(rows):
        name = input("Enter name: ")
        ph_no = input("Enter phone number: ")
        e_mail = input("Enter email: ")

        names.append(name)
        ph_nos.append(ph_no)
        emails.append(e_mail)


    for i in range(rows):
        print("\n***************** ", i + 1, " ************************")
        print("Name: ", names[i], "\nPhone Number: ", ph_nos[i], "\nEmail: ", emails[i])

except:
    print("Input is not a number")

print("\nThanks for using our contact book app")
