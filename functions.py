import os
import json


def check_input(user_input: int, random_number: int) -> str:
	if user_input == random_number:
		return 'right'
	else:
		if user_input < random_number:
			return 'more'
		elif user_input > random_number:
			return 'less'

def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')

def user_view(original_function):
	def wrapper_function(*args, **kwargs):
		clear_terminal()
		
		func = original_function(*args, **kwargs)
		
		clear_terminal()
		
		return func
	return wrapper_function

file_name = 'personalized.json'

def save_new_mode_informatins(info):
	name = None
	max_number = None
	
	if isinstance(info, tuple):
		for item in info:
			if isinstance(item, str):
				name = item
			if isinstance(item, int):
				max_number = item
			if name is not None and max_number is not None:
				break
	
		new_mode = {
			'name': name,
			'max_number': max_number
		}
		with open(file_name, 'w') as file_obj:
			json.dump(new_mode, file_obj)

def get_new_mode_informatins():
	with open(file_name, 'r') as file_obj:
		content = file_obj.read()
		new_mode = json.loads(content)
	
	return new_mode

if __name__ == '__main__':
	print('Run the main.py file.')
