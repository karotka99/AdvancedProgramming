def readfile(path: str):
    f = open(path, encoding='UTF-8')
    data = f.read()
    f.close()
    return data


#print(readfile(r'C:\Users\Karolina\PycharmProjects\lab_7\data\movies.csv' ))
