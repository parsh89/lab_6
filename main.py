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
            encoded_string == '9'
        if password[i] == '7':
            encoded_string += '0'
        if password[i] == '8':
            encoded_string += '1'
        if password[i] == '9':
            encoded_string += '2'

    return encoded_string




def main():
    print('Menu')
    print('-' * 13)
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    user_select = int(input('Please enter an option:'))
    password_select = int(input('Please enter password to encode:'))
    if user_select == 1:
        y = encoder(password_select)
        print(y)
    print('Your password has been stored and encoded!')


#encoded_string += str(int(password[i]) + 3)