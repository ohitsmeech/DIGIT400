from passlib.hash import sha256_crypt

pass1 = "password1"
pass2 = "password2"
salt = "password3"

saltpass1 = pass1 + salt
saltpass2 = pass2 + salt

newpass1 = sha256_crypt.encrypt(saltpass1)
newpass2 = sha256_crypt.encrypt(saltpass2)


print(newpass1)
print(newpass2)

print(sha256_crypt.verify("password1" +salt, newpass1)) #If these two don't match the boolean will be False


"""
import hashlib

user_password = "cookies"
salt = "chocolate"
new_password = user_password + salt

hashpass = hashlib.md5(new_password.encode())
print(hashpass.hexdigest())
"""