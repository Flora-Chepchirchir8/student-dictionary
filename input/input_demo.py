
# def personal_details():
#     name, age = "Agnes", 19
#     email = "aggieletty24"
#     favouriteMovie = "Bridgerton"
#     print("Name: {}\nAge: {}\nEmail: {}\nFavouriteMovie: {}".format(name, age,email,favouriteMovie))

# personal_details()

def main():
    #Empty dictionary to collect users
    responses={}
    
    #set flag condition to end or continue loop
    polling=True

    #while loop to fill responses
    def main():
    #Empty dictionary to collect users
         responses={}
    
    #set flag condition to end or continue loop
    polling=True

    #while loop to fill responses
    while polling:
        email=input("Enter email: ")
        name=input("Agnes")
        age=input("18")
        favouriteMovie=input("Merlin")
        responses[name]=email
        responses[name]=name
        responses[name]=age
        responses[name]=  favouriteMovie
        rep=input("Any more users y/n?")
        if rep=='n' or rep=='N':
            polling=False
    for info in responses.items():
        print("\nEmail: \t\t"+email+"\nName: \t\t"+name+"\nAge: \t\t"+age+ "\nFavouriteMovie: \t\t"+favouriteMovie )
main()


