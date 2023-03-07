import pandas as pd
import numpy as np
from collections import Counter
import itertools
from itertools import combinations
d=pd.read_csv("C:/Users/akhil/OneDrive/Desktop/DataMining/transactionaldataset.csv")
d


#creating candidates
def createCandidates(L1,c):
    # when the combinations are in string, then it means we have to make combinations
    # of 2, for that, we used the if -else statement
    for i in L1.keys():
        if isinstance(i,str):
            combinations_2 = list(itertools.combinations(L1.keys(), 2))
            combb=counterFind(combinations_2)
            return combb
            break
        else:    
            items = set(itertools.chain.from_iterable(L1.keys()))
            # get combinations of three items
            combinations = list(itertools.combinations(items, c))
            return list(combinations)


# Function for finding the Comparison w.r.t minimum count = 2
def findL(counter):
    ccc={}
    for i,j in counter.items():
        if j>=2:
            ccc[i]=j
    return ccc

#Arranging the counters
def counterFind(aa):
    counter={}
    for t in aa:
        counter[t]=0
    for transaction in dataset.values():
        for j in aa:
            if all(items in transaction for items in j):
                counter[j]+=1
    return counter


#Main Function of combining
def splitting(cc,c):
    while len(cc)!=0:
        aa=createCandidates(cc,c) 
        counter=counterFind(aa)  
        cc=findL(counter)
        c+=1
        Main.append(cc)
        splitting(cc,c)

    return Main[-3]




''' Dataset to dictionary'''
dataset={}
Main=[]  # Saving all classes
min_support =2   # Minimum support =2
for i in d.values.tolist():
    dataset[i[0]]=i[1].split(',')


''' First Class'''
c=2  # Each Combination times starting from 2
c1,t=[],[]
Main=[]
for i in dataset.values():
    for j in i:
        t.append(j)
c1=dict(Counter(t))
L={}
for i,j in c1.items():
    if j>=min_support:
        L[i]=j
Main.append(L)   # L1
ans=splitting(L,c)
print('Frequent Items ',ans)
