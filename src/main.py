'''
Created on Feb 24, 2017

@author: chenzeng
'''
import urllib.request

import argparse
import itertools


#read the file from input url in terminal
def read_file(filename):
    req = urllib.request.urlopen(filename)
    buffer = req.read().decode('utf-8')
    f = open('assign3.txt','w')
    f.write(buffer)
    print("read from:", filename)
    return f

#print the length of the file
def readline():
    with open('assign3.txt','r') as fh:
        num=0
        for line in fh.readlines():
            num+=1
        return num
                
    
#count the number of led lights lighting
def count():
    with open('assign3.txt','r') as fh:
        num = int(fh.readline())
        a = [[False]* num for _ in range(num)]
        for line in fh:
            line = line.replace(","," ")
            values = line.strip().split(' ')
            if values[0] =='turn':
                x1 = int("".join(values[2].split()))
                y1 = int("".join(values[3].split()))
                x2 = int("".join(values[5].split()))
                y2 = int("".join(values[6].split()))
                if  x1 <0:
                    x1=0
                if x2 > num:
                    x2=num-1
                if values[1] == 'on':
                    for i in range(x1,x2+1):
                        for j in range(y1,y2+1):
                            a[i][j]=True
                if values[1] == 'off':
                    for i in range(x1,x2+1):
                        for j in range(y1,y2+1):
                            a[i][j]=False
            if values[0] == 'switch':
                x1 = int("".join(values[1].split()))
                y1 = int("".join(values[2].split()))
                x2 = int("".join(values[4].split()))
                y2 = int("".join(values[5].split()))
                if  x1 <0:
                    x1=0
                if x2 > num:
                    x2=num-1
                for i in range(x1,x2+1):
                        for j in range(y1,y2+1):
                            if a[i][j]==True:
                                a[i][j]=False
                            else:
                                a[i][j]=True
    lightOn = 0
    for i in range(num):
        lightOn += sum(a[i])
    return lightOn
                    
        
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help = 'input help', default=False)
    args = parser.parse_args()
    filename = args.input
    read_file(filename);
    readline();
    print("Count:",count());

