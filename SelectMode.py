import os
import configparser

import functions as fc


class SelectMode:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('commands.ini')
		self.cfg = self.config['selector']
		self.path = f'MyGame\SelectMode>'
		self.help_message = 'Type "see" to see the available modes.'
		self.invalid_command_message = '"{}" is not recognized as a valid command.'
		self.modes = ['baby', 'easy', 'medium', 'hard', 'insane']
		self.add_new_mode()
		self.run = True
	
	def add_new_mode(self):
		file_name = 'personalized.json'
		
		if os.path.exists(file_name):
			new_mode = fc.get_new_mode_informations()
			name = new_mode['name']
			self.modes.append(name)
		else:
			pass
	
	@property
	def see(self):
		available_modes = ', '.join(self.modes)
		note = '\nnote: Type one to play it.'
		
		return f'Available modes: {available_modes}.{note}'
			
	def select_mode(self):		
		while self.run:
			user_input = input(f'\n{self.path}').lower()
			
			if user_input == self.cfg['EXIT_THE_GAME']:
				return False
				
			elif user_input == self.cfg['RETURN_ONE_INPUT_AGO']:
				self.run = False
				
			elif user_input == self.cfg['SEE_A_HELP_MESSAGE']:
				print(self.help_message)
				
			elif user_input == self.cfg['SEE_AVAILABLE_MODES']:
				print(self.see)
			
			elif user_input == self.cfg['CLEAR_TERMINAL']:
				fc.clear_terminal()
				
			else:
				if user_input in self.modes:
					return user_input
				else:
					print(self.invalid_command_message.format(user_input))


if __name__ == '__main__':
	print('Run the main.py file.')
