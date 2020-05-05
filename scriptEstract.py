import  numpy
import os

path="out_spacy_Interview.csv"
data=""

with open(path,"r") as f:
    data=f.readlines()

#data=data.split("\n")

for k in range(500000):
    l=data[k]
    with open("Dataset_Interview.csv","a") as f:
        f.write(l)

print("le travaille est finis")        
