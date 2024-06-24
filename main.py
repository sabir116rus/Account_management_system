class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    # Get методы
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Set методы
    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:
            self.__access_level = access_level
        else:
            raise ValueError("Неверный уровень доступа")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users = []

    # Переопределение метода get_access_level для возврата admin
    def get_access_level(self):
        return self.__access_level

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
        else:
            raise ValueError("Можно добавлять только экземпляры класса User")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                break  # Прерываем цикл после удаления, т.к. ID уникальны

    def get_users(self):
        return self.__users


# Пример использования
# Создание пользователей
user1 = User(1, "Петя Петров")
user2 = User(2, "Семен Семенов")
admin = Admin(3, "Альберт Сабиров")

# Проверка методов get
print(f"User1 ID: {user1.get_user_id()}, Имя: {user1.get_name()}, Уровень доступа: {user1.get_access_level()}")
print(f"Admin ID: {admin.get_user_id()}, Имя: {admin.get_name()}, Уровень доступа: {admin.get_access_level()}")

# Изменение имени и уровня доступа у пользователя
user1.set_name("Петр Петров")
user1.set_access_level("admin")
print(f"Измененный User1 ID: {user1.get_user_id()}, Имя: {user1.get_name()}, Уровень доступа: {user1.get_access_level()}")

# Добавление пользователей через администратора
admin.add_user(user1)
admin.add_user(user2)

# Вывод списка пользователей
print("\nСписок пользователей после добавления:")
for user in admin.get_users():
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Удаление пользователя
admin.remove_user(1)

# Вывод списка пользователей после удаления
print("\nСписок пользователей после удаления:")
for user in admin.get_users():
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Попытка добавления неверного объекта
try:
    admin.add_user("Неверный объект")
except ValueError as e:
    print(f"\nОшибка добавления пользователя: {e}")

# Попытка установки неверного уровня доступа
try:
    user2.set_access_level("неверный уровень")
except ValueError as e:
    print(f"\nОшибка установки уровня доступа: {e}")
