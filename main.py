import functions as fc
from Settings import Settings
from SelectMode import SelectMode
from CreateNewMode import CreateNewMode
from RandomNumbers import RandomNumbers
from RunGame import RunGame


class Main:
	def __init__(self):
		self.path = 'MyGame - 2.1>'
		self.cfg = Settings().main_commands
		self.main_commands = {
			self.cfg['COMMAND_SELECT_MODE']: 'Select the game mode',
			self.cfg['COMMAND_NEW_MODE']: 'Create your mode',
			self.cfg['COMMAND_CMD']: 'See all of the commands'
		}
		self.standard_commands = {
			self.cfg['COMMAND_HELP']: 'A help message',
			self.cfg['COMMAND_RETURN']: 'Return one input ago or finish the game',
			self.cfg['COMMAND_EXIT']: 'Exit the game'
		}
		self.init_message = 'Welcome to MyGame - 2.1! (type "help" for help)'
		self.help_message = 'Type "cmd" to see all of the commands.'
		self.invalid_command_message = '"{}" is not recognized as a valid command.'
		self.run = True
	
	@property
	def see_commands(self):
		main_commands = 'Commands in this path:\n'
		
		for key, value in self.main_commands.items():
			main_commands += f'"{key}": {value}\n'
		
		standard_commands = '\nStandard commands:\n'
		
		for key, value in self.standard_commands.items():
			standard_commands += f'"{key}": {value}\n'
			
		commands = main_commands + standard_commands
		
		return commands.strip()
	
	def get_random_number(self, mode):
		if mode:
			rn = RandomNumbers(mode)
			random_number = rn.get_random_number()
			
			return random_number
	
	def get_max_number(self, mode):
		if mode:
			rn = RandomNumbers(mode)
			max_number = rn.get_max_number()
			
			return max_number
	
	def run_game(self, mode):
		if mode:
			random_number = self.get_random_number(mode)
			max_number = self.get_max_number(mode)
							
			RunGame(random_number, max_number)
	
	def check_validity(self, info):
		if info is False:
			self.run = False
			
			return None
		else:
			return True
	
	@fc.user_view
	def main(self):
		print(self.init_message)
		
		while self.run:
			user_input = input(f'\n{self.path}').lower()
			
			if user_input == self.cfg['COMMAND_EXIT']:
				self.run = False
				
			elif user_input == self.cfg['COMMAND_RETURN']:
				continue
				
			elif user_input == self.cfg['COMMAND_HELP']:
				print(self.help_message)
				
			elif user_input == self.cfg['COMMAND_CMD']:
				print(self.see_commands)
				
			elif user_input == self.cfg['COMMAND_SELECT_MODE']:
				info = SelectMode().select_mode()
				check = self.check_validity(info)
				if check:
					self.run_game(info)
				
			elif user_input == self.cfg['COMMAND_NEW_MODE']:
				info = CreateNewMode().create_new_mode()
				check = self.check_validity(info)
				if check:
					fc.save_new_mode_informatins(info)
				
			else:
				print(self.invalid_command_message.format(user_input))

if __name__ == '__main__':
	main = Main()
	main.main()
