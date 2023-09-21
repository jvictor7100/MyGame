import configparser

import functions as fc

class CreateNewMode:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('commands.ini')
		self.cfg = self.config['creator']
		self.path = 'MyGame\CreateNewMode>'
		self.path_name = fr'{self.path}\name>'
		self.path_max_number = f'{self.path}\max_number>'
		self.help_message = 'Type "name" for set the mode name and type "max" for set the maximum number.'
		self.invalid_command_message = '"{}" is not recognized as a valid command.'
		self.name = 'custom'
		self.max_number = 0
		self.run = True
	
	@property
	def get_informations(self):
		name = self.name
		max_number = self.max_number
		
		return name, max_number
	
	def create_new_mode(self):
		while self.run:
			user_input = input(f'\n{self.path}').lower()
			
			if user_input == self.cfg['EXIT_THE_GAME']:
				return False

			elif user_input == self.cfg['RETURN_ONE_INPUT_AGO']:
				if self.max_number > 1:
					return self.get_informations
				else:
					self.run = False
			
			elif user_input == self.cfg['SEE_A_HELP_MESSAGE']:
				print(self.help_message)
			
			elif user_input == self.cfg['SET_NEW_MODE_NAME']:
				name = self.set_name()
				if name == False:
					return False

			elif user_input == self.cfg['SET_NEW_MODE_MAXIMUM_NUMBER']:
				max_number = self.set_max_number()
				if max_number == False:
					return False
			
			elif user_input == self.cfg['CLEAR_TERMINAL']:
				fc.clear_terminal()

			else:
				print(self.invalid_command_message.format(user_input))

	
	def set_name(self):
		run = True
		
		while run:
			user_input = input(f'\n{self.path_name}')
			
			self.name = user_input
			
			run = False
		
	def set_max_number(self):
		run = True
		
		while run:
			try:
				user_input = input(f'\n{self.path_max_number}')
				
				self.max_number = int(user_input)
				
				run = False
			except ValueError:
				print('Type only numbers.')


if __name__ == '__main__':
	print('Run the main.py file.')
