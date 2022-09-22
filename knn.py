"""
@author:Harsha Rauniyar
implementing the knn algorithm
"""

import sys
import random
import math

#handling command line arguments to be entered in the terminal
file_path= sys.argv[1]
distance_function=sys.argv[2]
k=sys.argv[3]
percent_for_training= sys.argv[4]
random_seed= sys.argv[5]

#2d matrix to store list of instances

matrix=[]


#function to calculate euclidean distance
def euclidean(test,training):
    distance=0
    for i in range(1,len(test)):
        # print(test[i])
        # print(training[i])
        distance=distance+(test[i]-training[i])**2
    
    return distance


#function to calculate hamming distance

def hamming(test,training):
    count=0
    for i in range(1,len(test)):
        # print(test[i])
        # print(training[i])
        if test[i]!=training[i]:
            count+=1
    
    return count


# function to check if a str is float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#reading in csv file, and storing all the instances
file=open(file_path,"r")
line=file.readline()
line=file.readline()


label_count={}
while line:
    
    line=line.strip()
    instance_list=line.split(",")
    instance=[]
    for elem in instance_list:
        if elem.isdigit():
            instance.append(int(elem))
        elif isfloat(elem)==True:
            instance.append(float(elem))
        
        else:
            instance.append(elem)
    
    if instance[0] in label_count:
        label_count[instance[0]]+=1
    else:
        label_count[instance[0]]=1
    matrix.append(instance)
    
    
    line=file.readline()




#create list of labels
labels=[]
for x,v in label_count.items():
    labels.append(x)


# tracking index of labels by keeping them in a dictionary
label_index={}
for i in range(0,len(labels)):
    label_index[labels[i]]=i

#suffling the 2d matrix
random.seed(random_seed)
random.shuffle(matrix)

#spliting the dataset to training, and test depending on the percentage given by the user
matrix_len=len(matrix)
training_set_length=float(percent_for_training)*matrix_len
training_set=matrix[0:round(training_set_length)+1]
test_set=matrix[round(training_set_length)+1:]

#initializing the confusion matrix
labellen=len(labels)
confusion_matrix = [ [0] * (labellen+1) for _ in range(labellen+1)]
for i in range(0,labellen):
    confusion_matrix[0][i]=labels[i]

confusion_matrix[0][labellen]=""

for i in range(1,labellen+1):
    confusion_matrix[i][labellen]=labels[i-1]




#knn algorithm 
for test_instance in test_set:
    dist_label=[]
    count_dict={}
    
    for training_instance in training_set:
        
        if distance_function=="H":

            hamming_distance=hamming(test_instance,training_instance)
            dist_label.append([hamming_distance,training_instance[0]])

        elif distance_function=="E":
            euclidean_distance=euclidean(test_instance,training_instance)
            dist_label.append([euclidean_distance,training_instance[0]])
            
        
    dist_label=sorted(dist_label)
    
    
    for i in range(0,int(k)):
        if dist_label[i][1] not in count_dict:
            count_dict[dist_label[i][1]]=1
        else:
            count_dict[dist_label[i][1]]+=1
    
    # print(count_dict)
    prediction=max(count_dict, key=count_dict.get)
    actual=test_instance[0]
    confusion_matrix[label_index[actual]+1][label_index[prediction]]+=1

#outputing the confusion matrix to a file
result_file="results"+'_'+file_path+"_"+k+"_"+random_seed+".csv"
with open(result_file,"w") as f:
    for row in range(0,len(confusion_matrix)):
        for col in range(0,len(confusion_matrix)):
            f.write(str(confusion_matrix[row][col]))
            if col<len(confusion_matrix)-1:
                f.write(",")
        
        f.write("\n")
f.close()















