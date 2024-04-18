def main():
    gender = input("Enter your gender (male/female): ").lower()
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))

    if gender == "female":
        if age > 20:
            married = input("Are you married? (yes/no): ").lower()
            if married == "yes":
                print("Mrs. {} {}".format(first_name, last_name))
            else:
                print("Ms. {} {}".format(first_name, last_name))
        else:
            print("{} {}".format(first_name, last_name))
    elif gender == "male":
        if age > 20:
            print("Mr. {} {}".format(first_name, last_name))
        else:
            print("{} {}".format(first_name, last_name))
    else:
        print("Invalid gender.")
if __name__ == "__main__":
    main()