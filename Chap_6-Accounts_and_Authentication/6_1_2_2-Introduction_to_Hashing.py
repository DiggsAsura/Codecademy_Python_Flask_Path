# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 2. Introduction to Hashing

'''
An important rule of application development is to never store sensitive user
data as plain text. Plain text data is a security risk, as a data breach or hack
would allow sensitive data to fall into the wrong hands.

How can we store sensitive user data, such as passwords, in a more secure format?
Step in hashing! Hashing is the process of taking text input and creating a new
sequence of characters out of it that cannot be easily reverse-engineered.

When we hash user passwords, we can store the hashed format rather than the original
play text passwords. If a hack were to occur, the hackers would not be able to 
exploit the stolen information without knowing the hashing function that was used
to encrypt the data.

We can add hashing functionality to a Flask application using the security module
of the Werkzeug package.

To hash a password:


hashed_password = generated_password_hash("noONEwillEVERguessTHIS")


- generate_password_hash() takes a string as an argument and returns a hash of the
  string
  
We can also check a user-entered password against our hashed password to check for
a match:


hash_match = check_password_hash(hashed_password, "IloveTHEcolorPURPLE123")
print(hash_match) # will print False
hash_match = check_password_hash("noONEwillEVERguessTHIS")
print(hash_match) # will print True


- check_password_hash() takes two arguments: the hashed string and a new string which
  we are checking the hash against. It returns a boolean indicating if the string was
  a match to the hash.

While we are hardcoding our passwords here, in later exercises we will see how to 
collect this information using a Form.
'''

from werkzeug.security import generate_password_hash, check_password_hash

hardcoded_password_string = '123456789_bad_password'

# generate a hash of hardcoded_password_string here:
hashed_password = generate_password_hash(hardcoded_password_string)

password_attempt_one = "abcdefghij_123456789"
# check password_attmpt_one aginast hashed_password here:
hash_match_one = check_password_hash(hashed_password, password_attempt_one)

password_attempt_two = "123456789_bad_password"
hash_match_two = check_password_hash(hashed_password, password_attempt_two)

print(hash_match_one)
print(hash_match_two)