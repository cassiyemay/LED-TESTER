'''
Created on Feb 24, 2017

@author: chenzeng
'''
import urllib.request
import argparse
import itertools


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
    
#get the each file size.               
def size():
    with open('assign3.txt','r') as fh:
        #read the first line number and get the size
        size= int(fh.readline())  
        return size
    
#get the true values in a2d list after loop.
def count():
    num = size()
    # set the a2d list all elements for false
    a = [[False]* num for _ in range(num)]
    #read each line into one list
    with open('assign3.txt','r') as fh:
        for line in fh:
            line = line.replace(","," ")
            values = line.strip().split(' ')
            #extract the x1,y1,x2,y2 and command line
            if values[0] =='turn':
                x1 = int("".join(values[2].split()))
                y1 = int("".join(values[3].split()))
                x2 = int("".join(values[5].split()))
                y2 = int("".join(values[6].split()))
                # set if the x1 is negative, x1 is zero
                #if x2 is greater than size, x2 is equal to (size-1)
                if  x1 <0:
                    x1=0
                if x2 > num:
                    x2=num-1
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
            else:
                continue
        return a
#count the number of true in a, which is the number of lights lighting
def lightOn():                           
    lightOn = 0
    num =size()
    a=count()
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
    size();
    count();
    print("Count:",lightOn());   
if __name__ == '__main__':
    start()

