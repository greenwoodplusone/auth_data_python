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

while True:
    Menu.menu(True, False, False, Menu.menuNotAuthData, Menu.menuAuthData, Menu.menuAdminData, 1)