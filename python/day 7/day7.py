def has_ABBA(section):
	for i in range(len(section), 3, -1):
		word = section[i-4:i]
		if word[0] == word[-1] and word[1] == word[2] and word[0] != word[1]:
			return True

	return False

def has_ABA_and_BAB(outside_brackets, inside_brackets):
	for s_in in inside_brackets:
		for i in range(len(s_in), 2, -1):
			word_in = s_in[i-3:i]
			if word_in[0] == word_in[2] and word_in[0] != word_in[1]:
				for s_out in outside_brackets:
					for i in range(len(s_out), 2, -1):
						word_out = s_out[i-3:i]
						if (word_out[0] == word_out[2] and word_out[0] != word_out[1]) and (word_out[0] == word_in[1] and word_out[1] == word_in[0]):
							return True

	return False


def split_input(ip):
	outside_brackets = []
	inside_brackets = []

	for s in ip.split('['):
		if ']' not in s:
			outside_brackets.append(s)
		else:
			inside_brackets.append(s.split(']')[0])
			outside_brackets.append(s.split(']')[-1])

	return outside_brackets, inside_brackets

def supports_TLS(ip):
	outside_brackets, inside_brackets = split_input(ip)

	if sum(has_ABBA(s_out) for s_out in outside_brackets) >=1 and sum(has_ABBA(s_in) for s_in in inside_brackets) == 0:
		return True

	return False

def supports_SSL(ip):
	outside_brackets, inside_brackets = split_input(ip)

	if has_ABA_and_BAB(outside_brackets, inside_brackets):
		return True

	return False

def count_IPs(ips, supports):
	if supports == 'TLS':
		return sum(supports_TLS(ip) for ip in ips)
	elif supports == 'SSL':
		return sum(supports_SSL(ip) for ip in ips)


if __name__ == '__main__':
	with open('input', 'r') as f:
		ips = [line.strip('\n') for line in  f.readlines()]

	IPs_with_TLS = count_IPs(ips, supports='TLS')
	print IPs_with_TLS
	IPs_with_SSL = count_IPs(ips, supports='SSL')
	print IPs_with_SSL