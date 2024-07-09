class User:
    # Конструктор класса User
    def __init__(self, user_id, account, name, unit):
        self._user_id = user_id  # Защищенный атрибут идентификатора пользователя
        self._account = account  # Защищенный атрибут аккаунта пользователя
        self._name = name  # Защищенный атрибут имени пользователя
        self._unit = unit  # Защищенный атрибут подразделения пользователя
        self._access_level = 'user'  # Уровень доступа по умолчанию для обычного пользователя

    # Метод для получения идентификатора пользователя
    def get_user_id(self):
        return self._user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self._name

    # Метод для получения аккаунта пользователя
    def get_account(self):
        return self._account

    # Метод для получения подразделения пользователя
    def get_unit(self):
        return self._unit

    # Метод для получения уровня доступа пользователя
    def get_access_level(self):
        return self._access_level

    # Метод для изменения данных аккаунта пользователя
    def set_account(self, account, name, unit):
        self._account = account
        self._name = name
        self._unit = unit


class Admin(User):
    # Конструктор класса Admin
    def __init__(self, user_id, account, name, unit):
        super().__init__(user_id, account, name, unit)  # Вызов конструктора родительского класса User
        self._access_level = 'admin'  # Уровень доступа для администратора

    # Метод для добавления пользователя в список
    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Аккаунт пользователя "
              f"{user.get_account()} ({user.get_name()}, {user.get_unit()}) добавлен.")

    # Метод для удаления пользователя из списка
    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Аккаунт пользователя "
                      f"{user.get_account()} ({user.get_name()}, {user.get_unit()}) удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")
    def update_user(self, user_list, user_id, account, name, unit):
        for user in user_list:
            if user.get_user_id() == user_id:
                user.set_account(account, name, unit)
                print(f"Данные аккаунта пользователя "
                      f"{user.get_account()} ({user.get_name()}, {user.get_unit()}) изменены.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

# Пример использования системы управления учетными записями

# Создание списка пользователей
user_list = []

# Создание обычных пользователей
user1 = User(1, "I.Ivanov","Иван Иванов", "Бухгалтерия")
user2 = User(2, "I.Petrov","Петр Петров", "Управление делами")
user3 = User(3, "M.Sidorova","Мария Сидорова", "Плановый отдел")
user4 = User(4, "G.Astafieva","Галина Астафьева", "Отдел маркетинга")
user5 = User(5, "G.Shiriaeva","Гаянэ Ширяева", "Плановый отдел")
user6 = User(6, "K.Mbappe","Килиан Мбаппе", "Отдел развития футбола")

# Создание администратора""
admin = Admin(0, "Admin", "Администратор", "Отдел ИТ")

# Добавление пользователей в систему с помощью администратора
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
admin.add_user(user_list, user3)
admin.add_user(user_list, user4)
admin.add_user(user_list, user5)
admin.add_user(user_list, user6)

# Вывод списка пользователей
print("\nСписок пользователей:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Аккаунт: {user.get_account()}, Имя: {user.get_name()}, "
          f"Подразделение: {user.get_unit()}, Уровень доступа: {user.get_access_level()}")

# Удаление пользователя из системы с помощью администратора
admin.remove_user(user_list, 1)
admin.remove_user(user_list, 5)

# Вывод обновленного списка пользователей
print("\nОбновленный список пользователей:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Аккаунт: {user.get_account()}, Имя: {user.get_name()}, "
          f"Подразделение: {user.get_unit()}, Уровень доступа: {user.get_access_level()}")

# Создание обычных пользователей под номерами 1 и 5 (удаленных ранее)
user1 = User(1, "I.Ivanov2","Иван Иванов2", "Бухгалтерия2")
user5 = User(5, "G.Shiriaeva2","Гаянэ Ширяева2", "Плановый отдел2")

# Добавление пользователей 1 и 5 в систему с помощью администратора
admin.add_user(user_list, user1)
admin.add_user(user_list, user5)

# Вывод списка пользователей
print("\nСписок пользователей после добавления двух:")
for user in user_list:
    print(f"ID: {user.get_user_id()}, Аккаунт: {user.get_account()}, Имя: {user.get_name()}, "
          f"Подразделение: {user.get_unit()}, Уровень доступа: {user.get_access_level()}")

# Изменение данных пользователя в системе с помощью администратора
admin.update_user(user_list, 1, "Ivan.Ivanov","Иван Петрович Иванов", "Централизованная бухгалтерия")
admin.update_user(user_list, 5, "Gayane.Shiriaeva","Гаянэ Бронтозавровна Ширяева", "Планово-экономический отдел")

# Сортируем список
new_user_list = sorted(user_list, key=lambda x: x.get_user_id())

# Вывод обновленного списка пользователей
print("\nОбновленный список пользователей (после добавления, изменения и сортировки):")
for user in new_user_list:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, "
          f"Подразделение: {user.get_unit()}, Уровень доступа: {user.get_access_level()}")