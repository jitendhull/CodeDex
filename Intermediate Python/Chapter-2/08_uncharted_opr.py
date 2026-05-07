sent_message = "Hey there! I just wanted to share a cool Python project I'm working on. It's a music recommendation system that uses machine learning to suggest songs based on your listening habits. I've been having a lot of fun coding it and learning new things along the way. If you're interested, I can share more details about how it works and the technologies I'm using!"

# Write the Sent Message to a File

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

# Uncharted Operation: Unsetting the Sent Message

with open('sent_message.txt', 'r+') as file:
    original_message = file.read()
    file.seek(0)
    unsent_message = 'This message has been unset'
    file.truncate(0)
    file.write(unsent_message)

# Print Logic

print("Original Message:", original_message)
print("Unsent Message:", unsent_message)