import pandas as pd
import numpy as np
import itertools
from collections import Counter
from itertools import combinations
from mlxtend.frequent_patterns import association_rules
d=pd.read_csv("C:/Users/akhil/OneDrive/Desktop/DataMining/transactionaldataset.csv")
min_support =2 #GIVEN DATA
  
d


#SEPERATING THE LIST_OF_ITEM ELEMENTS
dataset={}
for i in d.values.tolist():
    dataset[i[0]]=i[1].split(',')
dataset1=pd.DataFrame(dataset.items(),columns=['TID','List_of_items'])
dataset1



t=[]
L={}  # Comparison L for Candidates
for i in dataset.values():
    for j in i:
        t.append(j)
candidate1=dict(Counter(t))  #Candidate 1 have the single set data

for i,j in candidate1.items():
    if j>=min_support:
        L[i]=j
        
L1=pd.DataFrame(L.items(),columns=['TID','List_Of_Items'])
L1

def createCandidateComparison(c1,c):
    #Here, on the first pass, the data will be in strings and rest on tuples.
    #So the method is different for both.
    for i in c1.keys():
        if isinstance(i,str):  #checking if it is string
            comb=list(itertools.combinations(c1.keys(),2))
            return counterFind(comb)  # Here we are finding the number of times it exist directly
        else:  # For the c>2
            comb=set(itertools.chain.from_iterable(c1.keys()))
            comb=list(itertools.combinations(comb,c)) # Now finding combinations
            return list(comb)

def CounterFind(aa):
    counter={} # Result
    for i in aa:
        counter[i]=0 #setting the counter to 0 at first
    for transaction in dataset.values():   # Dataset is the main dataset with the values
        for j in aa: # taking each element from aa
            if all(items in transaction for items in j): #if all items exist in transaction
                counter[j]+=1   #adding that elements to dictionary and counting.
    return counter

def findLComparison(candidate_i):
    Lii={}
    for i,j in candidate_i.items():
        if j>=2:
            Lii[i]=j
    return Lii

def splitting(c1,c,a):  #c1 as candidate 1 on first pass, c is the combination
    while len(c1)!=0:
        aa=createCandidateComparison(c1,c)  # Comparison creator function
        candidate_i=CounterFind(aa)   #This function is to find the number of occurance of elements and result is got back as dictionary
        c1=findLComparison(candidate_i)  # Now comparison has to be done with respect to that candidate
        c+=1   # for next recurssion, the combination should be done with c+=1
        finalPatterns=pd.DataFrame(c1.items(),columns=['TID','List_Of_Items'])
        if finalPatterns.empty:
            return a #returning the last dataframe
            break
        else:
            a=finalPatterns
            #print(finalPatterns)   #Can print this to see all the Patterns
        
        if flag==1:
            return finalPatterns
        splitting(c1,c,a)  #Recurssion for the next combination

c=2
a=pd.DataFrame()  # EMpty one
frequent_items=splitting(L,c,a)
print('frequent Itemset=\n\n',frequent_items)



r,rules={},[]
#Associate 1
for i in frequent_items['TID']:
    for j in i:
        r[j]=round(((min_support/candidate1[j])*100),2)
    rules.append(r)
    r={}

#Associate 2
comb=[]
for i in frequent_items['TID']:
    comb.append(list(itertools.combinations(i,2)))
for i in comb:
    s=CounterFind(i)  #counter find of each of them
    for i,j in s.items():
        r[i]=round(((min_support/j)*100),2)
    rules.append(r)
    r={}
    
'''
# PRINTING RULES FOR BOTH ASSOCIATIONS
for i in rules:
    print(i)
'''

count,count1=0,0
print('Rules\n_________\n\n')
for i in range(len(rules)):
    if i==0 or i%2==0:
        for k in rules[i].values():
            if k>=100:
                count+=1  #Number of 100 in first set
    else:
        for k in rules[i].values():
            if k>=100:
                count1+=1  #Number of 100 in second set

if count:
    print('Most effective frequent element =',frequent_items.iloc[0]['TID'])
else:
    print('Most effective frequent element =',frequent_items.iloc[1]['TID'])
