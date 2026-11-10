
class Game:
	def category():
		return "Компьютерная игра"

	category = "Компьютерная игра"

	def __init__(self, title, genre, rating):
		self.title = title
		self.__genre = genre
		self.__rating = rating
		print("Object created", self.title)

	@property
	def genre(self):
		return self.__genre

	@property
	def rating(self):
		return self.__rating

	@rating.setter
	def rating(self, value):
		if 0 <= value <= 10:
			self.__rating = value
		else:
			raise ValueError("Рейтинг должен быть от 0 до 10")

	def update_rating(self, new_rating):
		self.rating = new_rating
		print(f"Рейтинг обновлен: {self.rating}")

	def display_info(self):
		info = (f"Название - {self.title}\n"
			f"Жанр - {self.genre}\n"
			f"Рейтинг - {self.rating}\n")
		print(info)

	def __del__(self):
		print(f"Игра {self.title} удалена с сервера")


class OnlineGame(Game):
	def __init__(self, title, genre, rating, players_online):
		super().__init__(title, genre, rating)
		self.players_online = players_online

	def display_info(self):
		super().display_info()
		print(f"Игроков онлайн: {self.players_online}")


def main():
	# 1. Создание объектов
	print("\n1. Создание объектов")

	minecraft = Game("Minecraft", "Строительство", 9)
	gta5 = OnlineGame("GTA V", "Экшен", 8, 15000)

	# 2. Определение типа объекта
	print("\n2. Определение типа объекта")

	print("Тип minecraft:", type(minecraft))
	print("Тип gta5:", type(gta5))

	# 3. Просмотр атрибутов и методов
	print("\n3. Просмотр атрибутов и методов")

	game_dir = [x for x in dir(minecraft) if not x.startswith("__")]
	online_dir = [x for x in dir(gta5) if not x.startswith("__")]

	print("Атрибуты и методы Game:")
	print(game_dir)

	print("\nАтрибуты и методы OnlineGame:")
	print(online_dir)

	# 4. Анализ словаря экземпляра
	print("\n4. Анализ словаря экземпляра")

	print("minecraft.__dict__:", minecraft.__dict__)
	print("gta5.__dict__:", gta5.__dict__)

	print("\nПроверка атрибутов класса:")
	print("Game.category:", hasattr(minecraft, "category"))
	print("OnlineGame.category:", hasattr(gta5, "category"))

	# 5. Проверка наличия атрибутов
	print("\n5. Проверка наличия атрибутов")

	print("minecraft.title:", hasattr(minecraft, "title"))
	print("minecraft.display_info:", hasattr(minecraft, "display_info"))
	print("minecraft._Game__genre:", hasattr(minecraft, "_Game__genre"))
	print("minecraft._Game__rating:", hasattr(minecraft, "_Game__rating"))

	print("\ngta5.players_online:", hasattr(gta5, "players_online"))
	print("gta5.display_info:", hasattr(gta5, "display_info"))
	print("gta5._Game__genre:", hasattr(gta5, "_Game__genre"))

	# 6. Получение значений атрибутов
	print("\n6. Получение значений атрибутов")

	print("Название:", getattr(minecraft, "title"))
	print("Жанр:", getattr(minecraft, "genre"))
	print("Приватный рейтинг:", getattr(minecraft, "_Game__rating"))
	print("Несуществующий атрибут:",
		getattr(minecraft, "nonexistent", "Атрибут отсутствует"))

	print("\nПолучение и вызов метода через getattr:")

	method = getattr(minecraft, "display_info")
	method()

	# 7. Динамическое добавление атрибута
	print("\n7. Динамическое добавление атрибута")

	minecraft.new_attr = 123

	print("minecraft.__dict__:", minecraft.__dict__)
	print("Наличие new_attr:", hasattr(minecraft, "new_attr"))
	print("Значение new_attr:", getattr(minecraft, "new_attr"))

	print("\nПроверка через dir():")
	print("new_attr" in dir(minecraft))

	# 8. Попытка прямого доступа к приватному атрибуту
	print("\n8. Попытка прямого доступа к приватному атрибуту")

	try:
		print(minecraft.__rating)
	except AttributeError as e:
		print("Ошибка:", e)

	print("\nКорректный доступ через искаженное имя:")
	print("Рейтинг:", getattr(minecraft, "_Game__rating"))

	# 9. Вывод
	print("\n9. Вывод")

	print("Интроспекция позволяет исследовать объекты,")
	print("получать информацию об их атрибутах и методах,")
	print("проверять наличие свойств и получать их значения.")
	print("Также можно динамически добавлять атрибуты")
	print("и анализировать структуру классов.")

	del minecraft
	del gta5


if __name__ == "__main__":
	main()
