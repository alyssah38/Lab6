# Alyssa Hunt
def encode(password):
    encoded_password = []
    for i in range(0, len(password)):
        # keeps numbers from being double-digit after adding 3
        if password[i] == '7':
            encoded_password.append('0')
        elif password[i] == '8':
            encoded_password.append('1')
        elif password[i] == '9':
            encoded_password.append('2')
        else:
            encoded_password.append(int(password[i]) + 3)
        # interation
        i += 1
    encoded_password_string = ''
    # converts list back into a string
    for i in range(0, len(encoded_password)):
        encoded_password_string += str(encoded_password[i])
        i += 1
    return encoded_password_string


# decoder function that encodes user's input
def decode(password):
# for cole to fill in


def main():
     while True:
        print('Menu:')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        user_input = input('Please enter a option: ')
        if user_input == '1':
            # user's password input
            user_password = input('Please enter your password to encode: ')
            encoded_password = encode(user_password)
            print('Your password has been encoded and stored!')
        elif user_input == '2':
            print(f'The encoded password is {encoded_password}, and the original password is {user_password}.')
        else:
            break

if __name__ == "__main__":
    main()
