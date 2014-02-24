import RPi.GPIO as GPIO
import cmd

class CalcShell(cmd.Cmd):
	intro = 'CalcShell y00r, y00r, y00r\n'
	prompt = '(calc.y00r): '
	gpios = [18, 23, 24, 25, 22, 27, 17, 4]

	def preloop(self):			
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)

		# 2^0
		GPIO.setup(self.gpios[0], GPIO.OUT, initial=False)

		# 2^1
		GPIO.setup(self.gpios[1], GPIO.OUT, initial=False)

		# 2^2
		GPIO.setup(self.gpios[2], GPIO.OUT, initial=False)

		# 2^3
		GPIO.setup(self.gpios[3], GPIO.OUT, initial=False)

		# 2^4
		GPIO.setup(self.gpios[4], GPIO.OUT, initial=False)

		# 2^5
		GPIO.setup(self.gpios[5], GPIO.OUT, initial=False)

		# 2^6
		GPIO.setup(self.gpios[6], GPIO.OUT, initial=False)

		# 2^7
		GPIO.setup(self.gpios[7], GPIO.OUT, initial=False)


	def do_calc(self, arg):
		# summanden parsen
		first, operator, second = arg.partition('+');

		# summanden in integer casten
		try:
			first = int(first)
			second = int(second)
		except ValueError:
			print('Usage: <Zahl> + <Zahl>\n')
			return

		# summanden addieren
		sum = first + second;

		# summe in bin formatieren und umdrehen
		bin = "{0:b}".format(sum).rjust(8, '0')[::-1]
		
		# jeder stelle an entsprechenden gpio uebergeben
		for i in range(8):
			# gpio ermitteln
			gpio = self.gpios[i]

			# wert zum schreiben ermitteln
			value = False
			if bin[i] == '1':
				value = True

			# gpio dingsel
			GPIO.output(gpio, value)


if __name__ == '__main__':
    CalcShell().cmdloop()