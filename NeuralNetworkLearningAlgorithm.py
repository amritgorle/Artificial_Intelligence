import numpy as np
import random
import math

def sigmoid(x,t=0,k=1):
    val = 1/(1+math.e**(-k*x+t))
    return val
def mini(inp1,inp2,w1,w2,t):
    x = inp1 * w1 + inp2 * w2
    return sigmoid(x,t)
def get_Output(vector, input):
    output = np.array([-1.,-1.,-1.,-1.])
    for i in range(len(input)):
        output[i] = (mini(mini(input[i][0],input[i][1],vector[0],vector[1],vector[4]),mini(input[i][0],input[i][1],vector[2],vector[3],vector[5]),vector[6],vector[7],vector[8]))
    return output
def error(vector):
    output = get_Output(vector, [(0,0),(0,1),(1,0),(1,1)])
    #print(output)
    actual = np.array([0.,1.,1.,0.])
    err = sum([abs(output[i]-actual[i]) for i in range(len(actual))])
    return err

weight_vector = np.array([random.uniform(-1,1) for i in range(9)]) #[w1, w2, w3, w4, w5(t1), w6(t2), w7, w8, w9(t3)]
#print(weight_vector)
#print(weight_vector-delta)
input = [(0,0),(0,1),(1,0),(1,1)]
#weight_vector = np.array([1.,-1.,-1.,1.,0.5,0.5,1.,1.,0.5])
#print(get_Output(weight_vector,[(0,0),(0,1),(1,0),(1,1)]))
checker = []
while(True):
    if(error(weight_vector)<0.01):
        break
    delta = np.array([random.uniform(-1, 1) for j in range(9)])
    if(error(weight_vector+delta)<error(weight_vector)):
        weight_vector = weight_vector + delta
    #print(weight_vector)
    checker.append(weight_vector)
    #print(checker)
    list_checker = [list(i) for i in checker]
    if list_checker.count(list_checker[len(list_checker)-1])>100:
        weight_vector = np.array([random.uniform(-1, 1) for i in range(9)])
        list_checker = []
        checker = []
    print(error(weight_vector))
print(weight_vector)