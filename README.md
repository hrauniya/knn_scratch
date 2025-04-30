Harsha Rauniyar

knn.py contains implementation of the K-nearest neighbor algorithm.
Run the program in the command line as follows:
It should take as input five parameters:

a. The path to a file containing a data set
b. The name of the distance function to use, from the set {H, E} (where H stands for
Hamming and E stands for Euclidian)
c. The value of k to use in the k-Nearest Neighbors algorithm
d. The percentage of instances to use for a training set
e. An integer to use as a random seed

For example,
python knn mnist_100.csv E 1 0.75 12345
which will perform 1-Nearest Neighbors on mnist_100.csv using the Euclidian distance
function and a random seed of 12345, where 75% of the data will be used for training
(and the remaining 25% will be used for testing)

Output should be a confusion matrix(Predicted Labels vs Actual Labels)

Research Questions

Please use your program to answer these research questions and record your answers in a
README.md file:
1) Pick a single random seed and a single training set percentage (document both in your
README) and run k-Nearest Neighbors with a k = 1 on each of the four data sets. What
is the accuracy you observed on each data set?

2) Using the accuracies from Question 1, calculate a 95% confidence interval around the
accuracy on each data set.

3) How did your accuracy compare between the mnist_100 and mnist_1000 data sets?
Which had the higher average? Why do you think you observed this result? Did their
confidence intervals overlap? What conclusion can we draw based on their confidence
intervals?

4) Pick one data set and three different values of k (document both in your README). Run
the program with each value of k on that data set and compare the accuracy values
observed. Did changing the value of k have much of an effect on your results? Speculate
as to why or why not that observation occurred?


Answers
1)
By calculating the sum of the diagonals and dividing it by sum of all cell, we can find the accuracy of each data-set. Here is 
the list of accuracy I found for each dataset. 

penguins.csv
accuracy=0.88

monks1.csv
accuracy=0.64

mnist_100.csv
accuracy=0.90

mnist_1000.csv
accuracy=0.94

2)
We can calculate the 95% confidence intervals using the accuracy above for each dataset. Here is the list of 95% confidence intervals I found for each dataset.

penguins.csv
[0.811,0.949]

monks1.csv
[0.549,0.731]

mnist_100.csv
[0.863,0.937]

mnist_1000.csv
[0.931,0.949]

3)
The accuracy for mnist_100.csv and mnist_1000.csv were very similar. mnist_100.csv had an accuracy of 90% while mnist_1000.csv had an accuracy of 94% differing by 4%. The accuracy for mnist_1000.csv was higher than mnist_100.csv. I think this is because we had 10 times more instances in the mnist_1000.csv file, which also means a larger training set than the one in mnist_100.csv. Intuitively it makes sense that mnist_1000.csv had a higher accuracy because the model had a larger dataset to learn from than the mnist_100.csv dataset, and the predictions would also be better has the model has more data to refer to.

The confidence intervals for the mnist_100.csv, and the mnist_1000.csv do slightly overlap. The lower bound of mnist_1000.csv which is 0.931 is less than the upper bound of mnist_100.csv which is 0.937. Since, the confidence intervals for the two datasets overlap, we cannot conclude that the performance of using the 1000 instance dataset outperforms the one of 100 instances. There would be no statistically significant differences in their performance.

4)
For the mnist_100.csv file with k=1,2,3. I observed:

k=1 had an accuracy of 0.90
k=2 had an accuracy of 0.90 with the same sum of diagonals, and the same count across diagonals.
k=3 had an accuracy of 0.92 

When changing from k=1 to k=2 the accuracy and the sum of diagonals stayed the same. I think this is because there only 2 points that need to be compared. Either both of those are the same label--in this case we would proceed with that label. On the other hand, there are two different labels. In this case, according to the KNN algorithm we could pick any label as our prediction, so the algorithm is just picking the prediction when k=1. This depends on how we are finding out about the most frequent label up until k.

The accuracy increases from k=2 to k=3. I think this is because now there are more datapoints to be compared in a particular sub-region, or distance from the test point to accurately predict the label of the data point. However, we cannot imply that increasing k would increase accuracy because eventually we will cover the whole graph, and the most labels in the graph will get predicted.

README

2)I enjoyed implementing the knn algorithm from scratch. Implementing it from scratch gave me a more clear idea on its workings. I, however, want to learn more about how to decrease the complexity of this algorithm by using something like KD-trees.

3)I spent around 6-7 hours working on this assignment. 

4)I have adhered to the Honor Code in this assignment.
