import src.password_generator as pg

def main():
    choosed = int(input("Press a number for the type of password generation (0 - Random Password), (1 - Memorable Password), (2 - PIN): "))
    if 0 <= choosed <= 2: 
        generator = pg.PasswordGenerator(choosed_type=choosed)
        type = generator.get_type()
        if type == 'random_password':
            limit = int(input('Enter a specified password length (Enter nothing but default is 8): '))
            generator.choose_type(limit)
        elif type == 'memorable_password':
            ...
        elif type == 'pin':
            ...
    else:
        print('Invalid! choose only between (0 - Random Password), (1 - Memorable Password), (2 - PIN)')


if __name__ == "__main__":
    main()