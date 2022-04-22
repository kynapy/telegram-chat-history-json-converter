import json
# import emoji  # requires installation of emoji library (pip install emoji)

# Opens chat
f = open('result.json', encoding = 'utf-8') # change name of file to ur file name
data = json.load(f)

# Creates an output file
output = open('output.txt', 'w')

# Parse through list
for message in data['messages']:
    if message['type'] == 'message':
        if 'text' in message:
            date = message['date'][:10] + ' '
            time = message['date'][11:] + ' '
            sender = message['from'][:8] + ': '
            text = message['text']
            
            print(date, end = '')
            print(time, end = '')
            print(sender, end = '')
            print(text)
        else:
            date = message['date'][:10] + ' '
            time = message['date'][11:] + ' '
            sender = message['from'][:8] + ': '
            if 'media_type' in message:
                text = message['media_type']
            if 'photo' in message:
                text = '[Photo]'
            
            data = date + time + sender + text
            print(data)

output.close()
