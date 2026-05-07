import bcrypt

password = input('Enter password to hash: ').encode('utf-8')


hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(f'\nHashed Password: {hashed.decode("utf-8")}')

print('-' * 20)

verify = input('Re-enter password to verify: ').encode('utf-8')

if bcrypt.checkpw(verify, hashed):
    print('✅ Password verified successfully!')
else:
    print('❌ Incorrect password.')
