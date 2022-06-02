import logging

def hello_world(name: str) -> None:
	''' First init example hello_world '''
	message = f'Hello {name}!'
	logging.getLogger(__name__).info(message)
	return mesage
