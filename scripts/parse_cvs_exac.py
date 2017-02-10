#! /usr/bin/env python


#This Python file uses the following encoding: utf-8
import os
import sys
import argparse
import math
import pandas

def load_exac (exac_file): 
   annotations = {}
   with open(exac_file,'r') as fp: 
     for line in fp:
        line = line.strip('\n')
        line = line.split(',')
        annotations[line[1]] = line[9]
   return annotations     


def load_aip(aib_db):
    import pandas as pd

    xlsx = pd.ExcelFile(aib_db)

    sheet1 = xlsx.parse(0)
    col = sheet1.icol(0).real

    #row = sheet1.irow(0).real
    for i in col: 
        print (i)

def load_aip_db (aip_db):  
    i = 0
    regions = {} 
    dnsp = {} 
    heterozygosity = {}
    with open (aip_db, 'r') as fp: 
       for line in fp:
          line = line.strip ('\n') 
          line = line.split(",+",line) 
          print (line)
          #regions[line[1]] = line[0] 
          #dnsp[line[1]] = line[2] 
          i += 1
     print (i)
    return regions, dnsp  
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('aip') 
    parser.add_argument('exac')
    parser.add_argument('outfile')

    args = parser.parse_args()
    fp = open(args.outfile, 'w') 
    load_aip(args.aip)
    annotations = {}
    annotations = load_exac(args.exac) 
    #regions, dnsp = load_aip_db(args.aip) 
    #for i in annotations: 
     #   print (fp, i, annotations[i], regions[i], dnsp[i]) 
    
    
    
if __name__ == '__main__':
    main()
