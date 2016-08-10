import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB

def nb():
	clf = GaussianNB()
	clf.fit(X, Y)
	GaussianNB()
	return clf.predict([[-0.8, -1]])

#clf_pf = GaussianNB()
#clf_pf.partial_fit(X, Y, np.unique(Y))
#GaussianNB()
#rint(clf_pf.predict([[-0.8, -1]]))