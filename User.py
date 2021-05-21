class User:
    # база данных
    authData = []

    # Следующие данные нужны только для теста, удалить перед релизной сборкой
    authData.append([0, "adminadmin", "adminadmin", "admin@admin.com", "9998887766", true])
    authData.append([1, "useruser1", "useruser1", "user1@user.com", "1279478218", false])
    authData.append([2, "useruser2", "useruser2", "user2@user.com", "2279478218", false])
    authData.append([3, "useruser3", "useruser3", "user3@user.com", "3279478218", false])
    authData.append([4, "useruser4", "useruser4", "user4@user.com", "4279478218", false])
    authData.append([5, "useruser5", "useruser5", "user5@user.com", "5279478218", false])

    # количество зарегистрированных пользователей не считает администратора и начинается с 1
    # нужно всегда учитывать при любом переборе authData
    countUser = 5;

    # создание нового пользователя
    def __init__(self, userID, login, password, email, phoneNumber, adminRights=false):
        self.userID = userID
        self.login = login
        self.password = password
        self.email = email
        self.phoneNumber = phoneNumber
        self.adminRights = adminRights