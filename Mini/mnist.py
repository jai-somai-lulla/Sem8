import pandas
#import sklearn.cross_validation
#from sklearn.model_selection import cross_val_score
#from sklearn import module_selection
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def accuracy(predictions):
    count = 0.0
    for i in range(len(predictions)):
        if predictions[i] == train["label"][i]:
            count = count + 1.0
            
    accuracy = count/len(predictions)
    print ("--- Accuracy value is " + str(accuracy))
    return accuracy

print 'MNIST'
data = pandas.read_csv("mnist_test.csv")
train, test = train_test_split(data, test_size=0.2)

predictors = []


for i in range(784):
	string = "pixel" + str(i)
	predictors.append(string)

alg = RandomForestClassifier(random_state=1, n_estimators=150, min_samples_split=2, min_samples_leaf=1)
print ("Using "+ str(alg))
print
scores = cross_val_score(alg, train[predictors], train["label"], cv=3)

# Take the mean of the scores (because we have one for each fold)
print (scores)
print("Cross validation scores = " + str(scores.mean()))


full_predictions = []

alg.fit(train[predictors], train["label"])
# Predict using the test dataset.  
predictions = alg.predict_proba(train[predictors]).astype(float)
predictions = predictions.argmax(axis=1)

submission = pandas.DataFrame({
        "true value": train["label"],
        "label": predictions
    })
accuracyV = accuracy(predictions)

filename = str('%0.5f' %accuracyV) + "_test_mnist.csv"
submission.to_csv(filename, index=False)

full_predictions = []
# Fit the algorithm using the full training data.
alg.fit(train[predictors], train["label"])
# Predict using the test dataset.  We have to convert all the columns to floats to avoid an error.
predictions = alg.predict_proba(test[predictors]).astype(float)

predictions = predictions.argmax(axis=1)
ImageId = []
for i in range(1, 28001):
    ImageId.append(i)

submission = pandas.DataFrame({
        "ImageId": ImageId,
        "Label": predictions
    })
    
submission.to_csv("kaggle_mnist.csv", index=False)

# Score on kaggle mnist competition = 0.96614
print ("End of program")

