class Settings:
	def __init__(self):
		self.cmds = self.standard_commands
	
	@property
	def standard_commands(self):
		COMMAND_EXIT = 'exit'
		COMMAND_RETURN = '..'
		COMMAND_HELP = 'help'
		commands = {
			'COMMAND_EXIT': COMMAND_EXIT,
			'COMMAND_RETURN': COMMAND_RETURN,
			'COMMAND_HELP': COMMAND_HELP
		}
		
		return commands
	
	@property
	def main_commands(self):
		COMMAND_SELECT_MODE = 'mode'
		COMMAND_NEW_MODE = 'new'
		COMMAND_CMD = 'cmd'
		commands = {
			'COMMAND_SELECT_MODE': COMMAND_SELECT_MODE,
			'COMMAND_NEW_MODE': COMMAND_NEW_MODE,
			'COMMAND_CMD': COMMAND_CMD,
			'COMMAND_HELP': self.cmds['COMMAND_HELP'],
			'COMMAND_RETURN': self.cmds['COMMAND_RETURN'],
			'COMMAND_EXIT': self.cmds['COMMAND_EXIT']
		}
		
		return commands
	
	@property
	def selector_commands(self):
		COMMAND_SEE_MODES = 'see'
		commands = {
			'COMMAND_SEE_MODES': COMMAND_SEE_MODES,
			'COMMAND_HELP': self.cmds['COMMAND_HELP'],
			'COMMAND_RETURN': self.cmds['COMMAND_RETURN'],
			'COMMAND_EXIT': self.cmds['COMMAND_EXIT']
		}
		
		return commands
	
	@property
	def creator_commands(self):
		COMMAND_SET_NAME = 'name'
		COMMAND_SET_MAX_NUMBER = 'max'
		commands = {
			'COMMAND_SET_NAME': COMMAND_SET_NAME,
			'COMMAND_SET_MAX_NUMBER': COMMAND_SET_MAX_NUMBER,
			'COMMAND_HELP': self.cmds['COMMAND_HELP'],
			'COMMAND_RETURN': self.cmds['COMMAND_RETURN'],
			'COMMAND_EXIT': self.cmds['COMMAND_EXIT']
		}
		
		return commands
	
	@property
	def executor_commands(self):
		commands = {
			'COMMAND_RETURN': self.cmds['COMMAND_RETURN'],
		}
		
		return commands
	

if __name__ == '__main__':
	print('Run the main.py file.')
