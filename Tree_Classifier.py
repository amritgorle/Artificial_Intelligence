import random
import math
import csv

def read_file(filename):
    global CLASS_idx
    global header
    csvFile = open(filename, 'r')
    read = csv.reader(csvFile)
    DS = []
    for row in read:
        DS.append(row)
    header = DS.pop(0)
    header.pop(0)
    CLASS_idx = len(header)-1
    return DS
def remove_questions(data):
    no_questions = []
    for i in data:
        if '?' not in i:
            no_questions.append(i)
    return no_questions
def get_column(data, column):
    #print(column)
    c = []
    for i in data:
        #print(i)
        c.append(i[column])
    return c
def extract(data, column, value):
    return [i for i in data if i[column]==value]
def outcomes(newDS):
    end = get_column(newDS, CLASS_idx)
    #print("END: {}".format(end))
    yn = end.pop()
    for i in end:
        if i != yn:
            return (False, "")
    return (True, yn)
def get_values_from_column(DS, col):
    column = get_column(DS, col)
    values = []
    for i in column:
        if i not in values:
            values.append(i)
    return values
def dist_helper(DS):
    lastColumn = get_column(DS, CLASS_idx)
    distData = []
    for i in lastColumn:
        if i not in distData:
            distData.append(i)
    return distData
def get_distribution(DS, col):
    values = get_values_from_column(DS, col) # list
    distData = dist_helper(DS) # list
    #print("Dist Data: {}".format(distData))
    #print(distData)
    dist = []
    for val in values:
        #print("Val: {}".format(val))
        rows = extract(DS, col, val)
        #print(rows)
        lastCol = get_column(rows, CLASS_idx)
        options = [] #[yes, no, maybe, ...]
        for i in distData:
            options.append(lastCol.count(i))
        #print(options)
        dist.append(options)
        #print(dist)
    return dist
def entropy(vars):
    parts = []
    total = sum(vars)
    for i in vars:
        if i !=0:
            frac = i/total
            log = math.log2(frac)
            parts.append(frac * log)
    sums = sum(parts)
    return -1*sums
def avg_entropy(variables):
    total = 0
    pieces = []
    for i in variables:
        sums = sum(i)
        total = total + sums
        pieces.append((sums, entropy(i)))
    avjE = 0
    for j,k in pieces:
        #print("J: {}".format(j))
        #print("K: {}".format(k))
        avjE = avjE + ((j/total)*k)
    return avjE
def info_gained(variables):
    a = 1-avg_entropy(variables)
    return a
def best_column(DS):
    columns = []
    hVals = []
    for i in range(0,len(DS[0])):
        dis = get_distribution(DS, i)
        columns.append(dis)
        hVals.append(info_gained(dis))
    hVals.pop()
    best = hVals.index(max(hVals))
    return best
def make_tree(DS, level=1):
    best = best_column(DS) # number (0,1,2,3)
    for val in get_values_from_column(DS, best):
        new_DS = extract(DS, best, val)
        print("---" * level, header[best] + "?")
        #display(new_DS)
        TF, outcome = outcomes(new_DS)
        if (TF):
            print("---"*level + ">",val, outcome)
        else:
            print("---" * level + ">", val, "...")
            make_tree(new_DS, level+1)
"""
class Node:
    def init(self, col, DS):
        self.col = col
        self.question = DS[0][col]
        self.DataS = DS
        self.children = {}
    def get_question(self):
        return self.question
"""

Information = read_file("house-votes-84.csv")
Info = remove_questions(Information)
for i in Info:
    i = i.pop(0)
make_tree(Info, 1)

print("ENTROPY: {}".format(entropy([500, 500])))