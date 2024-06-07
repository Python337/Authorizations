BAZA = "BAZA.txt"


def begin() -> None:
    """
    Производится выбор действия с помощью цифр: 1 - регистрация,
    2 - авторизация, 3 - выход. Также проверяется на правильность
    введения определённого типа данных и символов, указанных в
    приветственном тексте переменной question_to_the_user.
    """
    try:
        question_to_the_user = int(
            input(
                " Если хотите зарегистрироваться - напишите 1,"
                " если хотите авторизоваться - 2, а если хотите выйти - 3: "
            )
        )
        if question_to_the_user == 1:
            registration()
        elif question_to_the_user == 2:
            authorization()
        elif question_to_the_user == 3:
            print("Досвидание!")
            exit()
        else:
            print("Введённое число должно быть в диапозоне от 1 до 3!")
            begin()
    except ValueError:
        print("Введены не цифры!")
        begin()


def check_login_and_password() -> tuple[str, str]:
    """
    Проверяем логин и пароль на допустимое количество символов. При успешной
    длине логина и пароля возвращаем их.
    """
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    while 3 > len(login) or len(login) > 20:
        if len(login) < 3:
            print(
                "Ваш логин слишком короткий!"
                " Он не должен быть менее 3 символов и не более 20."
            )
            login = input("Напишите верный логин: ")
        if len(login) > 20:
            print(
                "Ваш логин слишком длинный!"
                " Он не должен быть менее 3 символов и не более 20."
            )
            login = input("Напишите верный логин: ")
    print("Ваш логин по нашим стандартам написания верный.")
    while 4 > len(password) or len(password) > 32:
        if len(password) < 4:
            print(
                "Ваш пароль слишком короткий!"
                " Он не должен быть менее 4 символов и не более 32."
            )
            password = input("Напишите верный пароль: ")
        if len(password) > 32:
            print(
                "Ваш пароль слишком длинный!"
                " Он не должен быть менее 4 символов и не более 20."
            )
            password = input("Напишите верный пароль: ")
    print("Ваш пароль по нашим стандартам написания верный.")
    return login, password


def registration() -> None:
    """
    Действия при регистрации пользователя.

    Получаем  логин и пароль с функции check_login_and_password.
    Записываем данные в файл BAZA и пишем пользователю об успешной
    регистрации.
    """
    login, password = check_login_and_password()
    with open(BAZA, "a", encoding="utf-8") as file:
        file.write(f"{login} {password}\n")
        print("Ваши данные успешно записаны,"
              " теперь вы есть в нашей базе данных.")
        begin()


def authorization() -> None:
    """
    Действия при авторизации пользователя.

    Получаем  логин и пароль с функции check_login_and_password.
    Проверяем введёные данные пользователем при авторизации.
    Если пользователя нет в базе данных, ему предлагается зарегистрироваться,
    авторизоваться заново или выйти из программы.
    """
    login, password = check_login_and_password()
    with open(BAZA, "r", encoding="utf-8") as file:
        for i in file.read().split("\n"):
            user = i.split(" ")
            if login == user[0] and password == user[1]:
                print(f"Wellcome, {user[0]}")
                exit()

            if login != user[0] or password != user[1]:
                print("Вы не прошли авторизацию. Вас нет в нашей базе данных.")
                begin()


if __name__ == "__main__":
    begin()
