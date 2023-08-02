from os import system, name 


def clear_terminal():
	system('cls' if name == 'nt' else 'clear')

def check_input(user_input: int, random_number: int) -> str:
	if user_input == random_number:
		return 'right'
	else:
		if user_input < random_number:
			return 'more'
		elif user_input > random_number:
			return 'less'

def user_view(original_function):
	def wrapper_function(*args, **kwargs):
		clear_terminal()
		
		func = original_function(*args, **kwargs)
		
		clear_terminal()
		
		return func
	return wrapper_function

if __name__ == '__main__':
	'''testing'''
	print(check_input(5, 5))
