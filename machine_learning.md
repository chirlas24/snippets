# Machine Learning Snippets

## Validation of the dataset

### train_test_split
```python
# Load the library
from sklearn.model_selection import train_test_split
# Split the datset
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=p #Value between 0-1 as percentage,
                                                    random_state=xx #In case of seed needed)
```

### CrossValidation
```python
# Load the library
from sklearn.model_selection import cross_val_score
# Execute cross validation
cross_val_score(model(),
                X,
                y,
                cv=n, #Number of splits
                scoring="metric_to_be_used" #the metric to calculate
                                     )
# Evaluate the uniformity of the dataset with histogram

# Get the mean value with .mean()
```

## Selecting Hyperparameter 

### GridSearch
```python
# Load the library
from sklearn.model_selection import GridSearchCV
# For metrics
import sklearn.metrics
# Create an instance of the model
GridModel = GridSearchCV(model(),
                         param_grid={"hyperparameter_1":[vaules],
                                     "hyperparameter_2":[vaules],
                                     ...},
                         cv=n, #In case of cross validation
                         scoring="metric_to_be_used" #the metric in order to evaluate
                                     )
# Fit will test all of the combinations
GridModel.fit(X,y)

#Get the values
GridModel.best_params_ #Shows the best hyperparameters
GridModel.best_score_  #Shows the best score achived
GridModel.best_estimator_ #Returns the best model
```
### RandomizeSearch
```python
# Load the library
from sklearn.model_selection import RandomizedSearchCV
# For metrics
import sklearn.metrics
# Create an instance of the model
RandomizedModel = RandomizedSearchCV(model(),
                                     param_distributions={"hyperparameter_1":[vaules],
                                                          "hyperparameter_2":[vaules],
                                                           ...},
                                     cv=n, #In case of cross validation
                                     scoring="metric_to_be_used", #the metric in order to evaluate
                                     n_iter=n #Number of iterations
                                     )
# Fit will test all of the combinations
RandomizedModel.fit(X,y)

#Get the values
RandomizedModel.best_params_ #Shows the best hyperparameters
RandomizedModel.best_score_  #Shows the best score achived
RandomizedModel.best_estimator_ #Returns the best model
```

## Regression

### Linear Regression
```python
# Load the library
from sklearn.linear_model import LinearRegression
# Create an instance of the model
reg = LinearRegression()
# Fit the regressor
reg.fit(X,y)
# Do predictions
reg.predict([[2540],[3500],[4000]])
```

### k nearest neighbor
* parameters: n_neighbors
```python
# Load the library
from sklearn.neighbors import KNeighborsRegressor
# Create an instance
regk = KNeighborsRegressor(n_neighbors=2)
# Fit the data
regk.fit(X,y)
```
### Decision Tree
* Max_depth: Number of Splits
* Min_samples_leaf: Minimum number of observations per leaf
```python
# Load the library
from sklearn.tree import DecisionTreeRegressor
# Create an instance
regd = DecisionTreeRegressor(max_depth=3)
# Fit the data
regd.fit(X,y)
```
## Classification

### Logisitc Regression
```python
# Load the library
from sklearn.linear_model import LogisticRegression
# Create an instance of the classifier
clf=LogisticRegression()
# Fit the data
clf.fit(X,y)
```
### Support Vector Machine
Parameters:
* C: Sum of Error Margins
* kernel:
 * linear: line of separation
 * rbf: circle of separation
    * Additional param gamma: Inverse of the radius
 * poly: curved line of separation
    * Additional param degree: Degree of the polynome
```python
# Load the library
from sklearn.svm import SVC
# Create an instance of the classifier
clf = SVC(kernel="linear",C=10)
# Fit the data
clf.fit(X,y)
```
### k nearest neighbor
Parameters: 
* n_neighbors
```python
# Load the library
from sklearn.neighbors import KNeighborsClassifier
# Create an instance
regk = KNeighborsClassifier(n_neighbors=2)
# Fit the data
regk.fit(X,y)
```
### Decision Tree
Parameters:
* Max_depth: Number of Splits
* Min_samples_leaf: Minimum number of observations per leaf
```python
# Import Library
from sklearn.tree import DecisionTreeClassifier
# Create instance
clf = DecisionTreeClassifier(min_samples_leaf=20,max_depth=3)
# Fit
clf.fit(X,y)
```


## Ensemble models

### Random Forest
Parameters:
* N_estimators: Number of trees
* Max_depth: Number of Splits
* Min_samples_leaf: Minimum number of observations per leaf
```python
#Load the library
from sklearn.ensemble import RandomForestClassifier
# Create an instance
clf = RandomForestClassifier(max_depth=4)
# Fit the data
clf.fit(X,y)
```

### Gradient Boosted in Sklearn
Parameters:
* N_estimators: Number of trees
* learning_rate: Learning Rate of the Boosted Tree
* Max_depth: Number of Splits
* Min_samples_leaf: Minimum number of observations per leaf
```python
# Load the library
from sklearn.ensemble import GradientBoostingClassifier
# Create an instance
clf = GradientBoostingClassifier(max_depth=4)
# Fit the data
clf.fit(X,y)
```
