def main():

    user_password = list(input())

    def encoder(password):
        encoded_password = []
        for i in range(0, len(password)):
            if password[i] == '7':
                encoded_password.append('0')
            elif password[i] == '8':
                encoded_password.append('1')
            elif password[i] == '9':
                encoded_password.append('2')
            else:
                encoded_password.append(int(password[i]) + 3)
            i += 1
        encoded_password_string = ''
        for i in range(0, len(encoded_password)):
            encoded_password_string += str(encoded_password[i])
            i += 1
        return encoded_password_string

    print(encoder(user_password))

if __name__ == "__main__":
    main()
