import src.password_generator as pg

def main():
    choosed = int(input("Press a number for the type of password generation (0 - Random Password), (1 - Memorable Password), (2 - PIN): "))
    if 0 <= choosed <= 2: 
        generator = pg.PasswordGenerator(choosed_type=choosed)
        type = generator.get_type()
        if type == 'random_password':
            limit = int(input('Enter a number of specified password length (Enter nothing but default is 8): '))
            symbols = input('Would you like to add symbols? (Enter y/N "y" for yes, "N" for no): ' ).lower()
            print(generator.choose_type(limit=limit, choice=(symbols == 'y')))
        elif type == 'memorable_password':
            words = int(input('Enter a number on how words do you want (Default is 3)? '))
            print(generator.choose_type(no_of_words=words))
        elif type == 'pin':
            limit = int(input('Enter a number of specified PIN code length (Enter nothing but default is 8): '))
            print(generator.choose_type(limit=limit))
    else:
        print('Invalid! choose only between (0 - Random Password), (1 - Memorable Password), (2 - PIN)')


if __name__ == "__main__":
    main()