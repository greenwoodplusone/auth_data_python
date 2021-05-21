class User:
    # база данных
    authData = []

    # количество зарегистрированных пользователей не считает администратора и начинается с 1
    # нужно всегда учитывать при любом переборе authData
    countUser = 5;

    # создание нового пользователя
    def __init__(self, userID, login, password, email, phoneNumber, adminRights=False):
        self.userID = userID
        self.login = login
        self.password = password
        self.email = email
        self.phoneNumber = phoneNumber
        self.adminRights = adminRights


# Следующие данные нужны только для теста, удалить перед релизной сборкой
newUser0 = User(0, "adminadmin", "adminadmin", "admin@admin.com", "9998887766", True)
User.authData.append(newUser0)
newUser1 = User(1, "useruser1", "useruser1", "user1@user.com", "1279478218", False)
User.authData.append(newUser1)
newUser2 = User(2, "useruser2", "useruser2", "user2@user.com", "2279478218", False)
User.authData.append(newUser2)
newUser3 = User(3, "useruser3", "useruser3", "user3@user.com", "3279478218", False)
User.authData.append(newUser3)
newUser4 = User(4, "useruser4", "useruser4", "user4@user.com", "4279478218", False)
User.authData.append(newUser4)
newUser5 = User(5, "useruser5", "useruser5", "user5@user.com", "5279478218", False)
User.authData.append(newUser5)