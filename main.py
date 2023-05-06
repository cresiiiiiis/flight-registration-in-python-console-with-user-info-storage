print("Welcome to the Flight Registration App\n")

# Ask for user's personal information
name = input("Please enter your name: ")
age = input("Please enter your age: ")
gender = input("Please enter your gender: ")
nationality = input("Please enter your nationality: ")

# Ask for flight details
departure_city = input("Please enter your departure city: ")
destination_city = input("Please enter your destination city: ")
departure_date = input("Please enter your departure date (DD/MM/YYYY): ")
return_date = input("Please enter your return date (DD/MM/YYYY): ")
class_type = input("Please enter your class type (e.g. Economy, Business, First): ")

# Confirm the user's information
print("\nThank you, {}! Please confirm your details:".format(name))
print("Age: {}".format(age))
print("Gender: {}".format(gender))
print("Nationality: {}".format(nationality))
print("Departure City: {}".format(departure_city))
print("Destination City: {}".format(destination_city))
print("Departure Date: {}".format(departure_date))
print("Return Date: {}".format(return_date))
print("Class Type: {}".format(class_type))

# Write user's information to file
with open("facecopyusers.txt", "a") as file:
    file.write("Name: {}\n".format(name))
    file.write("Age: {}\n".format(age))
    file.write("Gender: {}\n".format(gender))
    file.write("Nationality: {}\n".format(nationality))
    file.write("Departure City: {}\n".format(departure_city))
    file.write("Destination City: {}\n".format(destination_city))
    file.write("Departure Date: {}\n".format(departure_date))
    file.write("Return Date: {}\n".format(return_date))
    file.write("Class Type: {}\n".format(class_type))
    file.write("\n")