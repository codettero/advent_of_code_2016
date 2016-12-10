import hashlib

def get_code(p_input):
	passwd_chars = []
	num = 0
	hash_input = p_input

	while len(passwd_chars) < 8:
		m = hashlib.md5()
		m.update(hash_input)
		if m.hexdigest()[:5] == '00000':
			passwd_chars.append(m.hexdigest()[5])

		num +=1
		hash_input = p_input + str(num)

	return ''.join(passwd_chars)

def get_updated_code(p_input):
	passwd_chars = [None, None, None, None, None, None, None, None]
	num = 0
	hash_input = p_input

	while [x for x in passwd_chars if x is None]:
		m = hashlib.md5()
		m.update(hash_input)
		hash_ = m.hexdigest()
		if hash_[:5] == '00000' and hash_[5].isdigit() and int(hash_[5]) >=0 and int(hash_[5]) <= 7:
			print '{}: {}'.format(hash_input, m.hexdigest()) 
			if passwd_chars[int(hash_[5])] is None:
				passwd_chars[int(hash_[5])] = hash_[6]
			print passwd_chars

		num +=1
		hash_input = p_input + str(num)

	return ''.join(passwd_chars)

if __name__ == '__main__':
	p_input = 'cxdnnyjw'
	# code = get_code(p_input)
	# print code

	code = get_updated_code(p_input)
	print code