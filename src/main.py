'''
Created on Feb 24, 2017

@author: chenzeng
'''
import urllib.request
import argparse
from itertools import groupby
import re


#read the input from terminal
def read_file(filename):
    req = urllib.request.urlopen(filename)
    buffer = req.read().decode('utf-8')
    #rewrite the buffer into a local file
    f = open('assign3.txt','w')
    f.write(buffer)
    #print the http
    print("read from:", filename)
    #return the local file
    return f

#print the length of the file
def readline():
    with open('assign3.txt','r') as fh:
        num=0
        for line in fh.readlines():
            num+=1
        return num
               
    
#get the true values in a2d list after loop.
def count():
    with open('assign3.txt','r') as fh:
        num = int(fh.readline())
        # set the a2d list all elements for false
        a = [[False]* num for _ in range(num)]
        #read each line into one list
        for line in fh:
            line = line.replace(","," ")
            values = line.strip().split(' ')
            l=re.findall(r'[+-]?\d+', line)
            list=[]
            for i in range(0,len(l)):
                if int(l[i]) <0:
                    l[i]=0
                if int(l[i]) > num:
                    l[i]=num-1
                else:
                    l[i]=int(l[i])
                list.append(l[i])
            #extract the x1,y1,x2,y2 and command line
            x1 = list[0]
            y1 = list[1]
            x2 = list[2]
            y2 = list[3]
            if values[0] =='turn':
                #command line is turn on, changing the false into true
                if values[1] == 'on':
                    for i in range(x1,x2+1):
                        for j in range(y1,y2+1):
                            a[i][j]=True
                #when command line is turn off, the element in a2d list do nothing
                if values[1] == 'off':
                    for i in range(x1,x2+1):
                        for j in range(y1,y2+1):
                            a[i][j]=False
            #when command line is switch, the false become true, otherwise.
            if values[0] == 'switch':
                for i in range(x1,x2+1):
                        for j in range(y1,y2+1):
                            if a[i][j]==True:
                                a[i][j]=False
                            else:
                                a[i][j]=True
            else:
                continue
#count the number of true in a, which is the number of lights lighting                         
    lightOn = 0
    for i in range(num):
        # get the total true values 
        lightOn += sum(a[i])
    return lightOn
                    
        
def start():
    #parsing the arguments and print the result
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help = 'input help', default=False)
    args = parser.parse_args()
    filename = args.input
    read_file(filename);
    readline();
    print("count:", count());   
if __name__ == '__main__':
    start()

