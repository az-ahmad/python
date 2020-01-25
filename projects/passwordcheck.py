'''
Password Leak Checker
Using the HaveIBeenPwned API, check if your password appears in their list of leaked passwords
Usage in terminal: $python passwordcheck.py password1 password2 password3
Can accept multiple password inputs at once
'''


import requests
import hashlib
import sys

def request_data_from_api(first5Hashed): # Checks first 5 characters of hashed password against the API and returns object containing list of matches
    url = 'https://api.pwnedpasswords.com/range/' + first5Hashed
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error {res.status_code}, check connection to API')
    return res

def api_check(password): # Converts user input password into SHA1 hash output, sends first 5 chars to be checked, returns matches and remained of hashed pass to be checked
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1pass[:5], sha1pass[5:]
    response = request_data_from_api(head)
    return leakedCount(response,tail)

def leakedCount(hashes, hash_to_check): # Convert the matches into lists, matches to complete hashed password and returns how many times it occurs
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0 # No matches found

def main(args):
    for password in args:
        count = api_check(password)
        if count:
            print(f'Your password "{password}" was found {count} times online. Consider changing your password')
        else: 
            print(f'Your password "{password}" was not found online. Good news!')

if __name__ == '__main__':
    main(sys.argv[1:])