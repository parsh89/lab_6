#this is my first GitHub addition
def encoder(password):
    encoded_string = ''

    for i in range(0, len(password)):
        if password[i] == '1':
            encoded_string += '4'
        if password[i] == '2':
            encoded_string += '5'
        if password[i] == '3':
            encoded_string += '6'
        if password[i] == '4':
            encoded_string += '7'
        if password[i] == '5':
            encoded_string += '8'
        if password[i] == '6':
            encoded_string += '9'
        if password[i] == '7':
            encoded_string += '0'
        if password[i] == '8':
            encoded_string += '1'
        if password[i] == '9':
            encoded_string += '2'

    return encoded_string

def main():
    while True:
        print('Menu')
        print('-' * 13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        user_select = int(input('Please enter an option:'))
        password_select = input('Please enter password to encode:')

        if user_select == 1:
            y = encoder(password_select)
            print(y)
            print('Your password has been stored and encoded!')
        elif user_select == 2:
            decoded_password = decode_password(password_select)
            print(decoded_password)
        elif user_select == 3:
            break

def decode_password(password):
    decode_password = ""
    for digit in password:
        if digit.isdigit():
            new_digit = str((int(digit) - 3) % 10)
            decode_password += new_digit
        else:
            decode_password += digit

    return decode_password

if __name__ == '__main__':
    main()
