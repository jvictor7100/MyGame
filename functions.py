import os
import json


personalized_file = 'personalized.json'
records_file = 'records.json'

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

def save_new_mode_informations(info: tuple):
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
		with open(personalized_file, 'w') as file_obj:
			json.dump(new_mode, file_obj)

def get_new_mode_informations():
	with open(personalized_file, 'r') as file_obj:
		new_mode = json.load(file_obj)
	
	return new_mode

def update_attempts_record(game_mode: str, new_record: int):
	if os.path.exists(records_file):
		with open(records_file, 'r') as file_obj:
			records = json.load(file_obj)
			
		for key, value in records.items():
			if key == game_mode:
				records[key] = new_record
				break
		else:
			records[game_mode] = new_record
		
		with open(records_file, 'w') as file_obj:
			json.dump(records, file_obj)
	else:
		record = {
			game_mode: new_record
		}
			
		with open(records_file, 'w') as file_obj:
			json.dump(record, file_obj)

def get_attempts_record(game_mode, attempts, all_records=False):
	if all_records:
		try:
			with open(records_file, 'r') as file_obj:
				records = json.load(file_obj)
			
			return records
		except FileNotFoundError:
			return None
	else:
		try:
			with open(records_file, 'r') as file_obj:
				records = json.load(file_obj)
					
			for key, value in records.items():
				if key == game_mode:
					if value > attempts:
						update_attempts_record(game_mode, attempts)
						
						return attempts
						break
					elif value <= attempts:
						return value
						break
			else:
				update_attempts_record(game_mode, attempts)
				
				return attempts
		except FileNotFoundError:
			update_attempts_record(game_mode, attempts)
			
			return attempts

if __name__ == '__main__':
	print('Run the main.py file')
