'''
Домашнее задание 10. «Работа с классами на примере API VK»
Вам предстоит решить задачу поиска общих друзей у пользователей VK.
Ссылка на документацию VK/dev. Токен для запросов: 10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c

Задача №1
Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.

Задача №2
Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей пользователей user1 и user2, в этом списке должны быть экземпляры классов.

Задача №3
Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK
'''

import requests

TOKEN = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'  # токен нетологии


class UserVK():
	
	def __init__(self, user_id):
		self.user_id = user_id
		self.empty_list = []
	
	def get_friends(self):
		options = {'access_token': TOKEN, 'v': 5.21, 'user_id': self.user_id}
		response = requests.get('https://api.vk.com/method/friends.get', params=options)
		self.user_friends = response.json()['response']['items']  # получаем список друзей в list
		return set(self.user_friends)  # возвращаем список друзей и конвертируем list в set
	
	def __and__(self, other):
		if len(
			self.get_friends() & other.get_friends()) == 0:  # проверяем - если длина set равна 0, то возвращаем пустой список
			return self.empty_list
		
		common_friends_ids = self.get_friends() & other.get_friends()  # получаем список общих друзей с помощью метода get_friends
		
		common_friends = []
		for id in common_friends_ids:
			common_friends.append(UserVK(id))  # в пустой список добавляем id друзей как экземпляр класса UserVK
		return common_friends
	
	def __str__(self):
		return f'http://vk.com/id{self.user_id}'
	
	def __repr__(self):
		return f'http://vk.com/id{self.user_id}'


user1 = UserVK()
user2 = UserVK()
# print(user1)
mutual_friends = user1 & user2
# print(mutual_friends)

for friends in mutual_friends:
	assert isinstance(friends, UserVK)
	print(friends)

