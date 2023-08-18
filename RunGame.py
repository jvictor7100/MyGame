from getpass import getpass

import functions as fc
from Settings import Settings


class RunGame:
	def __init__(self, random_number: int, max_number: int):
		self.random_number = random_number
		self.max_number = max_number
		self.cfg = Settings().executor_commands
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
	
	@fc.user_view
	def game(self):
		print(f'A number between 1 and {self.max_number:,} was selected. Discover it!')
		print('Remenber: if you want to give up type ".."')
		
		while self.run:	
			user_input = input('\n>>> ')
			
			if user_input == self.cfg['COMMAND_RETURN']:
				self.results(win=False)
				self.run = False
			else:
				try:
					output = fc.check_input(int(user_input), self.random_number)
				except ValueError:
					print(self.except_message)
					continue
				
				self.attempts += 1
					
				match output:
					case 'right':
						self.results(win=True)
						self.run = False
					case _:
						print(f'Output: {output}')


if __name__ == '__main__':
	print('Run the main.py file.')
