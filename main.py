# main function
def main():
    # intakes the user's input as a list
    user_password = list(input())

    # encoder function that encodes user's input
    def encoder(password):
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

    # prints new encoded password
    print(encoder(user_password))


if __name__ == "__main__":
    main()
