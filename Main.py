from Menu import *

# проверки на аторизованность пользователя и хранение его ID
userAuth = False
authAdmin = False
userID = 0

# количество попыток вода данных
counterMax = 3

# указатель на счетчик пустых ячеек после удаления пользователя
# int* ptrCountDeleteUser = nullptr;

# bool valid;

# выбор разделов меню
while True:
    menuInput = Menu.menu(True, False, False, Menu.menuNotAuthData, Menu.menuAuthData, Menu.menuAdminData, 1)

    if authAdmin:
        if menuInput == 1:
            while True:
                print("# Введите логин пользователя которого вы хотите удалить\n# ", end="")
                login = input()
                if not deleteUser(authData, login, countUser, ptrCountDeleteUser):
                    valid = breakOrContinueForError()
                    if not valid:
                        break
                    continue
                break

        elif menuInput == 2:
            printAuthData(authData, countUser, ptrCountDeleteUser)
            break
        elif menuInput == 3:
            logoutUser(authAdmin)
            break
        elif menuInput == 4:
            print("\nВсего хорошего!")
            break
        else:
            print("\nОтсутствующий пункт меню!")

        print()

    elif userAuth:
        if menuInput == 1:
            editMyPass(authData, userID, counterMax)
            break
        elif menuInput == 2:
            editMyLogin(authData, userID, countUser)
            break
        elif menuInput == 3:
            editMyEmail(authData, userID, countUser)
            break
        elif menuInput == 4:
            editMyPhoneNumber(authData, userID, countUser)
            break
        elif menuInput == 5:
            deleteUser(authData, authData[userID].login, countUser, ptrCountDeleteUser)
            break
        elif menuInput == 6:
            logoutUser(userAuth)
            break
        elif menuInput == 7:
            print("\nВсего хорошего!")
            break
        else:
            print("\nОтсутствующий пункт меню!")

        print()

    else:
        if menuInput == 1:
            registerUser(authData, userAuth, userID, countUser, ptrCountDeleteUser)
            break
        elif menuInput == 2:
            authorization(authData, userAuth, authAdmin, userID, countUser, counterMax)
            break
        elif menuInput == 3:
            forgotLogin(authData, countUser)
            break
        elif menuInput == 4:
            editPass(authData, countUser, counterMax)
            break
        elif menuInput == 5:
            print("# Всего хорошего!")
            break
        else:
            print("# Отсутствующий пункт меню!")

        print()