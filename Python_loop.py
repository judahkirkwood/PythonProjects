

i = 0
for i in range(10):
    print ("{} iteration through the loop.".format(i))
    i += 1







i = 0
while i < 10:
    print ("{} iteration through the loop.".format(i))
    i += 1






i = 0
while i < 10:
        print ("{} iteration through the loop.".format(i))
        i += 1
        if i == 5:
            break




i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print("{} iteration through the loop.".format(i))
    i += 1
