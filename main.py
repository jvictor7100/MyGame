import configparser

import functions as fc
from SelectMode import SelectMode
from CreateNewMode import CreateNewMode
from RandomNumbers import RandomNumbers
from RunGame import RunGame


version_string = '2.3'

class Main:
	def __init__(self):
		self.config = configparser.ConfigParser()
		self.config.read('commands.ini')
		self.cfg = self.config['main']
		self.path = f'MyGame>'
		self.main_commands = {
			self.cfg['SELECT_THE_GAME_MODE']: 'Select the game mode',
			self.cfg['SET_A_NEW_GAME_MODE']: 'Create your mode',
			self.cfg['SEE_AVAILABLE_COMMANDS']: 'See all of the commands',
			self.cfg['SEE_USER_RECORDS']: 'See your records'
		}
		self.standard_commands = {
			self.cfg['SEE_A_HELP_MESSAGE']: 'A help message',
			self.cfg['RETURN_ONE_INPUT_AGO']: 'Return one input ago or finish the game',
			self.cfg['EXIT_THE_GAME']: 'Exit the game',
			self.cfg['CLEAR_TERMINAL']: 'Clear the terminal'
		}
		self.init_message = f'Welcome to MyGame - {version_string}! (type "help" for help)'
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
	
	@property
	def see_records(self):
		records = fc.get_attempts_record(game_mode=None, attempts=None, all_records=True)
		
		if records:
			records_string = 'Your attempts records:\n'
			
			for key, value in records.items():
				records_string += f'{key} mode: {value}\n'

			return records_string.strip()
		else:
			return "You don't have records yet."
	
	def get_random_number(self, game_mode: str):
		if game_mode:
			rn = RandomNumbers(game_mode)
			random_number = rn.get_random_number()
			
			return random_number
	
	def get_max_number(self, game_mode: str):
		if game_mode:
			rn = RandomNumbers(game_mode)
			max_number = rn.get_max_number()
			
			return max_number
	
	def run_game(self, game_mode: str):
		if game_mode:
			random_number = self.get_random_number(game_mode)
			max_number = self.get_max_number(game_mode)
							
			RunGame(random_number, max_number, game_mode)
	
	def check_validity(self, info):
		if info == False:
			self.run = False
			
			return None
		else:
			return True
	
	@fc.user_view
	def main(self):
		print(self.init_message)
		
		while self.run:
			user_input = input(f'\n{self.path}').lower()
			
			if user_input == self.cfg['EXIT_THE_GAME']:
				self.run = False
				
			elif user_input == self.cfg['RETURN_ONE_INPUT_AGO']:
				continue
				
			elif user_input == self.cfg['SEE_A_HELP_MESSAGE']:
				print(self.help_message)
				
			elif user_input == self.cfg['SEE_AVAILABLE_COMMANDS']:
				print(self.see_commands)
				
			elif user_input == self.cfg['SELECT_THE_GAME_MODE']:
				info = SelectMode().select_mode()
				check = self.check_validity(info)
				if check:
					self.run_game(info)
				
			elif user_input == self.cfg['SET_A_NEW_GAME_MODE']:
				info = CreateNewMode().create_new_mode()
				check = self.check_validity(info)
				if check:
					fc.save_new_mode_informations(info)
			
			elif user_input == self.cfg['SEE_USER_RECORDS']:
				print(self.see_records)
			
			elif user_input == self.cfg['CLEAR_TERMINAL']:
				fc.clear_terminal()

			else:
				print(self.invalid_command_message.format(user_input))

if __name__ == '__main__':
	main = Main()
	main.main()
