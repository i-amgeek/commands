from os import system as sy
numberlist = list(map(str, [1000000*i for i in range(1000)]))
sy('yowsup-cli demos -c ~/Desktop/config -s {} "message"'.format(','.join(numberlist)))
