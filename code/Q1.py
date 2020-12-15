# coding: utf-8

def main():
    l = []
    for i in range(2000, 3201):
        if i%7 ==0 and i%5 !=0:
            l.append(str(i))
    print(','.join(l))

def main1():
    l = [str(x) for x in range(2000, 3201) if x%7 ==0 and x%5 !=0]
    print(','.join(l))

if __name__ == '__main__':
    main()
    # main1()