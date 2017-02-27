'''
Created on Feb 24, 2017

@author: chenzeng
'''
import urllib.request

import argparse
import itertools
from itertools import chain

parser = argparse.ArgumentParser()

parser.add_argument('--input', help = 'input help', default=False)
args = parser.parse_args()
filename = args.input

#read the file from input url in terminal
def read_file(filename):
    req = urllib.request.urlopen(filename)
    buffer = req.read().decode('utf-8')
    f = open('assign3.txt','w')
    f.write(buffer)
    print("read from:", filename)
    return f

#only retrieve the command and number
def readline():
    with open('assign3.txt','r') as fh:
        f1=open('assign.txt','w')
        for line in fh.readlines():
            values = line.strip().split(' ')
            if values[0]=='turn':
                a= values[0:2],values[2].split(','),values[-1].split(',')
                list= a[0][0]+" "+a[0][1]
                l1= list, values[2].split(','),values[-1].split(',')
                f1.write(str(l1)+"\n")
            elif values[0] =="switch":
                c= values[0]
                l2 = c,values[1].split(','),values[-1].split(',')
                f1.write(str(l2)+"\n")
        return f1
#count the number of lights lighting                
def count():
    with open("assign.txt","r") as fh1:
        for line in fh1.readlines():
            print(line[:-1])
            
                        
                

               
        
        
               
                
                
                
                
            
         
                    
                
    
        
        
          
   
        
    
if __name__ == '__main__':
    read_file(filename);
    readline();
    count();

