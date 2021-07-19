import requests
import hashlib
import sys


def request_api_server(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'The status is {res.status_code} try again')
	return res 

def get_password_leaks_and_counts(hashed_tails,my_tail):
	hashed_tails = (line.split(':') for line in hashed_tails.text.splitlines())
	for h, count in hashed_tails:
		if h == my_tail:
			return count 
	return 0


def pwned_api_check(password):
	sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	head, tails = sha1pass[:5],sha1pass[5:]
	response_from_api = request_api_server(head)
	return get_password_leaks_and_counts(response_from_api,tails)


def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'The password {password} was hacked {count} times! You may consider changing your password!')
		else:
			print(f'The password {password} was not hacked.This is great, dont forget your password!')
	return 'Awesome!'



if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))