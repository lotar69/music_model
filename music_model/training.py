from music_model.data import Data

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def tree_trainer():
    tree = DecisionTreeClassifier(random_state=10)
    data = Data()
    tree_model = tree.fit(data.X_train, data.y_train)
    return tree_model

def log_trainer():
    logreg = LogisticRegression()
    data = Data()
    train_model = logreg.fit(data.X_train, data.y_train)
    return train_model