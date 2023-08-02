from functions import user_view
import classes as cls


class Main:
	def __init__(self):
		self.path = 'MyGame - 2.1>'
		self.commands = {
			'cmd': 'See all of the commands',
			'mode': 'Select the game mode',
			'help': 'A help message',
			'..': 'Return one input ago or finish the game',
			'exit': 'Exit the game'
		}
		self.init_message = 'Welcome to MyGame - 2.1! (type "cmd" to see the opnions)'
		self.help_message = 'Type "cmd" to see all of the commands'
		self.invalid_command_message = '"{}" is not recognized as a valid command.'
		self.run = True
	
	def see_commands(self):
		commands_info = ''
		
		for key, value in self.commands.items():
			commands_info += f'"{key}": {value}\n'
		
		return commands_info.strip()
	
	def random_number(self, mode):
		rn = cls.RandomNumbers(mode)
		random_number = rn.get_random_number()
		
		return random_number
	
	def max_number(self, mode):
		rn = cls.RandomNumbers(mode)
		max_number = rn.get_max_number()
		
		return max_number
	
	def run_game(self, return_mode_selector):
		if return_mode_selector:
			random_number = self.random_number(return_mode_selector)
			max_number = self.max_number(return_mode_selector)
						
			cls.RunGame(random_number, max_number)
		elif return_mode_selector == False:
			self.run = False
	
	@user_view
	def main(self):
		print(self.init_message)
		
		while self.run:
			user_input = input(f'\n{self.path}').lower()
			
			match user_input:
				case 'exit':
					self.run = False
				case '..':
					continue
				case 'help':
					print(self.help_message)
				case 'cmd':
					print(self.see_commands())
				case 'mode':
					return_mode_selector = cls.SelectMode().select_mode()
					self.run_game(return_mode_selector)
				case _:
					print(self.invalid_command_message.format(user_input))
						

if __name__ == '__main__':
	main = Main()
	main.main()
