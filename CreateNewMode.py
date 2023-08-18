from Settings import Settings

class CreateNewMode:
	def __init__(self):
		self.path = 'MyGame - 2.1\CreateNewMode>'
		self.path_name = r'MyGame - 2.1\CreateNewMode\name>'
		self.path_max_number = 'MyGame - 2.1\CreateNewMode\max_number>'
		self.cfg = Settings().creator_commands
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
			
			if user_input == self.cfg['COMMAND_EXIT']:
				return False

			elif user_input == self.cfg['COMMAND_RETURN']:
				if self.max_number > 1:
					return self.get_informations
				else:
					self.run = False
			
			elif user_input == self.cfg['COMMAND_HELP']:
				print(self.help_message)
			
			elif user_input == self.cfg['COMMAND_SET_NAME']:
				name = self.set_name()
				if name == False:
					return False

			elif user_input == self.cfg['COMMAND_SET_MAX_NUMBER']:
				max_number = self.set_max_number()
				if max_number == False:
					return False

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
