f = open('C:/Users/admin\Desktop\KeNan001_998.txt', 'r')
g = open('C:/Users/admin\Desktop\Detective Conan.txt', 'a+')
for i in f.readlines():
    if 'playUrl' in i:
        url = i.split(' ')[-1][1:-3]
        g.write(url + '\n')
        print(url)