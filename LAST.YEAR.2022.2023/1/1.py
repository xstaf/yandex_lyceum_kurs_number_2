message = input()
words = message.split()
secret_words = words[2::3]
secret_message = ' '.join(secret_words)
print(secret_message)