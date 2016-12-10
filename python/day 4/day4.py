from collections import Counter

alph = 'abcdefghijklmnopqrstuvwxyz'

def get_index(char, sectorID):
	permutation = sectorID % 26
	if permutation + alph.index(char) < len(alph):
		return permutation + alph.index(char)
	else:
		return permutation - (len(alph) - alph.index(char))

def decode(room):
	sectorID = int(room.split('-')[-1].split('[')[0])
	decoded = []
	for char in room:
		if char.isalpha():
			decoded.append(alph[get_index(char, sectorID)])
		else:
			decoded.append(char)

	return ''.join(decoded)


def get_sum(rooms):
	room_sum = 0
	
	for room in rooms:
		print decode(room)

		letters = ''.join(room.split('-')[:-1])
		d = {}
		for letter in letters:
			d[letter] = letters.count(letter)
		sorted_letters = []
		letter_counts = set([d[k] for k in d])
		for count in letter_counts:
			sorted_letters.append((''.join(sorted([k for k in d if d[k] == count])), count))
		sorted_letters.sort(key=lambda x: x[1], reverse=True)

		if ''.join(x[0] for x in sorted_letters)[0:5] == room.split('-')[-1].split('[')[-1].strip(']'):
			room_sum = room_sum + int(room.split('-')[-1].split('[')[0])

	return room_sum

		
if __name__ == '__main__':
	with open('input', 'r') as f:
		rooms = [line.strip('\n').strip() for line in  f.readlines()]

	room_sum = get_sum(rooms)
	print room_sum