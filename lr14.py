class Game:
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
			raise ValueError("Error: Рейтинг должен быть от 0 до 10")
			
	def update_rating(self, new_rating):
		self.rating = new_rating
		print(f"Рейтинг обновлен {self.rating}")
		
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
	minecraft = Game("Minecraft", "Cтроительство", 9)
	gta5 = Game("GTA V", "Gang/Bang", 8)
	
	minecraft.display_info()
	gta5.display_info()
	
	print("текущий рейтинг minecraft:", minecraft.rating)
	minecraft.rating = 10
	print("новый рейтинг minecraft:", minecraft.rating)
	 
	print("\nПоптыемся изменить рейтинг игры на 15")
	try:
		minecraft.rating = 15
	except ValueError as e:
		print(e)
	
	print("\nменяем рейтинг гта на 6 через update_rating(6)")
	gta5.update_rating(6)
	
	print("\nпопытка изменить жанр игры")
	try:
		gta5.genre = "гонки"
	except AttributeError as e:
		print("Error:", e)
	
	print("\nпопытка изменить приватный рейтинг игры")
	try:
		print(gta5.__rating)
	except AttributeError as e:
		print("Error:", e)
	
	print("\nполиморфизм")
	games = [minecraft, gta5]
	
	for game in games:
		game.display_info()
		print()
	 	
	del minecraft
	del gta5
	
if __name__ == "__main__":
	main()
