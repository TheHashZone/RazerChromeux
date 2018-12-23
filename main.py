import os
from termcolor import colored

colours = {
    'red': '"\\xFF\\x00\\x00"', 'white': '"\\xFF\\xFF\\xFF"',
    'blue': '"\\x00\\x00\\xFF"', 'green': '"\\x00\\xFF\\x00"',
    'yellow': '"\\xFF\\xFF\\x00"', 'pink': '"\\xFF\\x14\\x93"'
}

class start:
	
	os.system("clear")

	end = " > /sys/bus/hid/drivers/razerkbd/0003:1532:0203.0006/matrix_effect_static"

	banner = '''\n
	8b,dPPYba, ,adPPYYba, 888888888  ,adPPYba, 8b,dPPYba,  
	88P'   "Y8 ""     `Y8      a8P" a8P_____88 88P'   "Y8  
	88         ,adPPPPP88   ,d8P'   8PP""""""" 88          
	88         88,    ,88 ,d8"      "8b,   ,aa 88          
	88         `"8bbdP"Y8 888888888  `"Ybbd8"' 88'''	
	print(colored(banner, 'green'), colored('Crack', 'red'), colored('v2', 'white'))	
	
	print("\n\nChoose a colour:")
	choice = """
	* red           * white
	* green         * yellow
	* blue          * pink
	\n"""

	print(choice)

class check:

	def dirCheck():
		try:
			os.chdir("/sys/bus/hid/drivers/razerkbd/0003:1532:0203.0006")

		except FileNotFoundError:
			start.end = " > /sys/bus/hid/drivers/razerkbd/0003:1532:0203.0003/matrix_effect_static"

		return start.end

class program:
	def main():

		end = check.dirCheck()

		userIn = input(">> ")

		try:
			colours[userIn]
			os.system(f"sudo echo -n -e {colours[userIn]} {end}")

		except KeyError:
			print("Not a valid colour!")


	if __name__ == "__main__":
	    main() 