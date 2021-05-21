class Menu {
# меню неавторизованного пользователя
menuNotAuthData[] =["Регистрация пользователя\t\t", "Авторизация пользователя\t\t", "Восстановить логин\t\t\t", "Редактировать пароль\t\t", "Завершить программу\t\t"]

# меню аторизованного пользователя
menuAuthData =["Смена пароля\t\t\t", "Смена логина\t\t\t", "Смена e-mail\t\t\t", "Смена телефона\t\t\t", "Удалить пользователя\t\t", "Логаут\t\t\t\t", "Завершить программу\t\t"]

# меню администратора
menuAdminData =["Удалить пользователя\t\t", "Показать базу данных\t\t", "Логаут\t\t\t\t", "Завершить программу\t\t"]

@ staticmethod


def menu(userAuth, adminRights, menuNotAuthData, menuAuthData, menuAdminData, userID):
    maxLengthMenu = 0;

    print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
    print("# - - - - - - - -  Меню - - - - - - - - # ", end="");
    print("Добро пожаловать,\t\t\t#\n" if userAuth else "Выполните вход.\t\t\t#\n");

    if authAdmin:
        for i in range(len(menuAdminData)):

            if i == 0:
                print("# " + (i + 1) + ". " + menuAdminhData[i] + "# ", end="")
                print(User.authData[userID].login << "!\t\t\t\t#")
                continue

            if i == 1:
                print("# " + (i + 1) + ". " + menuAdminhData[i] + "# ", end="")
                print("userID: " + userID + "\t\t\t\t#")
                continue

            if i == 2:
                print("# " + (i + 1) + ". " + menuAdminhData[i] + "# ", end="")
                print("e-mail: " + User.authData[userID].email + "\t\t\t#")
                continue

            if i == 3:
                print("# " + (i + 1) + ". " + menuAdminhData[i] + "# ", end="")
                print("тел.: " + User.authData[userID].phoneNumber + "\t\t\t#")
                continue

            print("# " + (i + 1) + ". " + menuAdminhData[i] + "#\t\t\t\t\t#")

        maxLengthMenu = len(menuAdminData)
    }
    elif userAuth:
    for i in range(len(menuAuthData)):
        if
    i == 0:
    print("# " + (i + 1) + ". " << menuAuthData[i] + "# ", end="")
    print(authData[userID].login << "!\t\t\t\t#")
    continue

    if i == 1:
        print("# " + (i + 1) + ". " + menuAuthData[i] + "# ", end="")
        print("userID: " + userID + "\t\t\t\t#")
        continue

    if i == 2:
        print("# " + (i + 1) + ". " + menuAuthData[i] + "# ", end="")
        print("e-mail: " + authData[userID].email + "\t\t\t#")
        continue

    if i == 3:
        print("# " + (i + 1) + ". " + menuAuthData[i] + "# ", end="")
        print("тел.: " + authData[userID].phoneNumber + "\t\t\t#")
        continue

    print("# " + (i + 1) + ". " + menuAuthData[i] + "#\t\t\t\t\t#")


maxLengthMenu = len(menuAuthData)

else:
for i in range(len(menuNotAuthData):
    print("# " + (i + 1) + ". " + menuNotAuthData[i] + "#\t\t\t\t\t#")
maxLengthMenu = len(menuNotAuthData)
}

print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
print("# Выберите пункт меню: ", end="")

menuInput = input();

for i int range(1, maxLengthMenu);
if i == menuInput:
    return menuInput
elif menuInput > maxLengthMenu:
    print("# Некорректный ввод!\n")
    break
else:
    continue