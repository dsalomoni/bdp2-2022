# read and write files in a file system structure
f1 = open('/usr/share/dict/words', 'r')
f2 = open('some_words.txt', 'w')
for line in f1:
    if line.startswith('T'):
        print(line, end='')
        f2.write(line)
f1.close()  # you should always close files when done with them
f2.close()  # ditto

# a more pythonic version
with open('/usr/share/dict/words', 'r') as f1, open('some_words.txt', 'w') as f2:
    for line in f1:
        if line.startswith('T'):
            print(line, end='')
            f2.write(line)
