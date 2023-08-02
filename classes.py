from random import randint
from getpass import getpass

from functions import *


class SelectMode:
	def __init__(self):
		self.path = 'MyGame - 2.1\SelectMode>'
		self.modes = ['baby', 'easy', 'medium', 'hard', 'insane']
		self.help_message = 'Type "see" to see all of the modes.'
		self.invalid_command_message = '"{}" is not recognized as a valid command.'
	
	def see(self):
		available_modes = ', '.join(self.modes)
		return f'Available modes: {available_modes}.\nnote: Type one to play it.'
		
	def select_mode(self):
		while True:
			user_input = input(f'\n{self.path}').lower()
			
			match user_input:
				case 'see':
					print(self.see())
				case '..':
					return None
				case 'help':
					print(self.help_message)
				case 'exit':
					return False
				case _:
					if user_input in self.modes:
						return user_input
					else:
						print(self.invalid_command_message.format(user_input))


class RunGame:
	def __init__(self, random_number, max_number):
		self.random_number = random_number
		self.max_number = max_number
		self.win_message = 'Congradulations!'
		self.defeat_message = 'Good look next time!'
		self.except_message = 'Type only numbers.'
		self.attempts = 0
		self.run = True
		self.game()
	
	def results(self, win: bool):
		match win:
			case True:
				print(f'{self.win_message}\nAttempts: {self.attempts}')
			case False:
				print(f'{self.defeat_message}\nAttempts: {self.attempts}')
		
		getpass('\nPress Enter to continue...')
	
	@user_view
	def game(self):
		print(f'A number between 1 and {self.max_number:,} was selected. Discover it!')
		
		while self.run:	
			user_input = input('\n>>> ')
			
			if user_input == '..':
				self.results(win=False)
				self.run = False
			else:
				try:
					output = check_input(int(user_input), self.random_number)
					self.attempts += 1
					
					match output:
						case 'right':
							self.results(win=True)
							self.run = False
						case _:
							print(f'Output: {output}')
				except ValueError:
					print(self.except_message)


class RandomNumbers:
	def __init__(self, game_mode):
		self.game_mode = game_mode
		self.mim_number = 1
		self.max_baby_number = 10
		self.max_easy_number = 50
		self.max_medium_number = 500
		self.max_hard_number = 5_000
		self.max_insane_number = 50_000
	
	def get_max_number(self):
		mapping_max_number = {
			'baby': self.max_baby_number,
			'easy': self.max_easy_number,
			'medium': self.max_medium_number,
			'hard': self.max_hard_number,
			'insane': self.max_insane_number
		}
		max_number = mapping_max_number.get(self.game_mode)
		
		return max_number
	
	def get_random_number(self):
		mode_mapping = {
			'baby': self.baby_mode_number(),
			'easy': self.easy_mode_number(),
			'medium': self.medium_mode_number(),
			'hard': self.hard_mode_number(),
			'insane': self.insane_mode_number()
		}
		random_number = mode_mapping.get(self.game_mode)
		
		return random_number

	def baby_mode_number(self):
		random_number = randint(self.mim_number, self.max_baby_number)
		return random_number

	def easy_mode_number(self):
		random_number = randint(self.mim_number, self.max_easy_number)
		return random_number

	def medium_mode_number(self):
		random_number = randint(self.mim_number, self.max_medium_number)
		return random_number

	def hard_mode_number(self):
		random_number = randint(self.mim_number, self.max_hard_number)
		return random_number

	def insane_mode_number(self):
		random_number = randint(self.mim_number, self.max_insane_number)
		return random_number

