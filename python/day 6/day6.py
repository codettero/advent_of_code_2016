def get_message(signals, func):
	msg = []
	merged_letters = []
	for i in range(len(signals[0])):
		merged = ''.join(s[i] for s in signals)
		if func == 'max':
			max = 0
			for letter in merged:
				if merged.count(letter) > max:
					max = merged.count(letter)
					max_letter = letter
			msg.append(max_letter)
		elif func == 'min':
			min = 1000000
			for letter in merged:
				if merged.count(letter) < min:
					min = merged.count(letter)
					min_letter = letter
			msg.append(min_letter)

	return ''.join(msg)


if __name__ == '__main__':
	with open('input', 'r') as f:
		signals = [line.strip('\n').strip() for line in  f.readlines()]

	msg = get_message(signals, 'max')
	print msg
	msg = get_message(signals, 'min')
	print msg
