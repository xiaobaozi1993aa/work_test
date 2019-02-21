import re

b = re.search(r'\b302', err)
c = re.search(r'\b200', err)
d = re.search(r'\b404', err)

if len(err) > 195:
    if b or d or c != None:
        print('success', err)
    else:
        exit(1)
else:
    print('%s ,%s , %s ,失败' % (services, port[0], port[1]))
    exit(1)






