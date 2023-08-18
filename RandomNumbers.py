from random import randint
import os

import functions as fc


class RandomNumbers:
	mapping_max_number = {
		'baby': 'max_baby_number',
		'easy': 'max_easy_number',
		'medium': 'max_medium_number',
		'hard': 'max_hard_number',
		'insane': 'max_insane_number'
	}
	mode_mapping = {
		'baby': 'get_baby_number',
		'easy': 'get_easy_number',
		'medium': 'get_medium_number',
		'hard': 'get_hard_number',
		'insane': 'get_insane_number'
	}

	def __init__(self, game_mode):
		self.game_mode = game_mode
		self.mim_number = 1
		self.max_baby_number = 10
		self.max_easy_number = 50
		self.max_medium_number = 500
		self.max_hard_number = 5_000
		self.max_insane_number = 50_000
		self.max_custom_number = None
		self.add_new_mode()
		
	def add_new_mode(self):
		file_name = 'personalized.json'
		
		if os.path.exists(file_name):
			new_mode = fc.get_new_mode_informatins()
			name = new_mode['name']
			self.max_custom_number = new_mode['max_number']
		
			self.mapping_max_number[name] = 'max_custom_number'
		
			self.mode_mapping[name] = 'get_custom_number'
		else:
			pass
	
	def get_max_number(self):
		if self.game_mode:
			max_number = getattr(self, self.mapping_max_number[self.game_mode])
		
			return max_number
	
	def get_random_number(self):
		if self.game_mode:
			random_number = getattr(self, self.mode_mapping[self.game_mode])
		
			return random_number
	
	@property
	def get_custom_number(self):
		random_number = randint(self.mim_number, self.max_custom_number)
		return random_number
	
	@property
	def get_baby_number(self):
		random_number = randint(self.mim_number, self.max_baby_number)
		return random_number

	@property
	def get_easy_number(self):
		random_number = randint(self.mim_number, self.max_easy_number)
		return random_number

	@property
	def get_medium_number(self):
		random_number = randint(self.mim_number, self.max_medium_number)
		return random_number

	@property
	def get_hard_number(self):
		random_number = randint(self.mim_number, self.max_hard_number)
		return random_number

	@property
	def get_insane_number(self):
		random_number = randint(self.mim_number, self.max_insane_number)
		return random_number

if __name__ == '__main__':
	print('Run the main.py file.')
