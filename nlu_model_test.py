from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter
import warnings


def run_nlu():
	print("--------------------Intent Classification-----------------------")
	interpreter = Interpreter.load('./models/nlu/default/weathernlu', RasaNLUConfig('config_spacy.json'))
	#print(interpreter.parse("I am planning my holiday to Lithuania. I wonder what is the weather out there."))
	while(True):
		UserInput = input("Enter your Query")
		if (UserInput == "Stop"):
			break
		print(interpreter.parse("{}".format(UserInput)))

if __name__ == '__main__':
	#train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()
	warnings.filterwarnings("ignore")
