import time

if __name__ == '__main__':
    mylist = (x * x for x in range(3))
    for i in mylist:
        print(i)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(2)
    for i in mylist:
        print(i)
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
