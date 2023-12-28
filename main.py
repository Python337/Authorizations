def login_and_password(): # Проверяем логин и пароль на допустимое количество символов.
    question_to_the_user = int(input(
        'Здравствуйте! Вы хотите зарегистрироваться или авторизоваться? Если хотите зарегистрироваться-напишите "1", а если хотите авторизоваться-напишите "2": '))
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    while 3 > len(login) or len(login) > 20:
        if len(login) < 3:
            print('Ваш логин слишком короткий! Он не должен быть менее 3 символов и не более 20.')
            login = input('Напишите верный логин: ')
        if len(login) > 20:
            print('Ваш логин слишком длинный! Он не должен быть менее 3 символов и не более 20.')
            login = input('Напишите верный логин: ')
    print('Ваш логин по нашим стандартам написания верный.')
    while 4 > len(password) or len(password) > 32:
        if len(password) < 4:
            print('Ваш пароль слишком короткий! Он не должен быть менее 4 символов и не более 32.')
            password = input('Напишите верный пароль: ')
        if len(password) > 32:
            print('Ваш пароль слишком длинный! Он не должен быть менее 4 символов и не более 20.')
            password = input('Напишите верный пароль: ')
    print('Ваш пароль по нашим стандартам написания верный.')
    return question_to_the_user, login, password


def saving_file(login, password): # Сохраняем логин и пароль, если пользователь регистрируется.
    with open('BAZA.txt', 'a', encoding="utf-8") as file:
        file.write(f'{login} {password}\n')
        print('Ваши данные успешно записаны, теперь вы есть в нашей базе данных.')
        exit()


def main(question_to_the_user, login, password): # Проверяем введёные данные пользователем при авторизации. Если пользователя нет в базе данных, ему предлагается зарегистрироваться или выйти из программы.
    with open('BAZA.txt', 'r', encoding='utf-8') as file:
        for i in file.read().split('\n'):
            user = i.split(' ')
            if question_to_the_user == 1:
                saving_file(login, password)
            if login == user[0] and password == user[1]:
                print(f'Wellcome, {user[0]}')
                exit()
            if question_to_the_user == 3:
                print('Досвидание!')
            if login != user[0] or password != user[1]:
                print('Вы не прошли авторизацию. Вас нет в нашей базе данных. Вы можете зарегистрироваться, нажав 1. Если же захотите выйти-нажмите 3.')
                question_to_the_user = int(input('Вводите: '))
                if question_to_the_user == 3:
                    print('Досвидание!')
                if question_to_the_user == 1:
                    saving_file(login, password)


question_to_the_user, login, password = login_and_password()
main(question_to_the_user, login, password)

if __name__ == "__main(question_to_the_user, login, password)__":
    main(question_to_the_user, login, password)


