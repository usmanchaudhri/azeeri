"""
- algorithm which is able to learn from data.
- machine learning can be classified into:
	classification: weather whales are fish or mammals.
	regression:
	clustering: finding patterns with-in the data i.e. fitting
	rule-extraction:
- input to the machine learning model is called the Feature Vector it is also called a test instance or prediction instance.
- output of the machine learning model is called the Label (predicted Label)
- Tradional ML based systems rely on experts to decide what features to pay attention to.
- Regression Models: Linear, Lasso, Ridge, SVR
- Classification Models: Naive Bayes, SVM, Decision trees, Boosted trees, Random Forest, Neural Networks.
- Representation ML-based systems figure out by themselves what features to pay attention to i.e Deep Learning models such as neural networks.
- Supervised Learning - labels associated with the training data feed to the model is used to correct the algorithm i.e. classification.
	Supervised machine learning is such that each input is provided with information about the expected output.
  Supervised machine learning algorithms seek to "learn" the function f that links the features and the labels => y = f(x)
	- X-VARIABLES:
	- the attributes that the ML algorithm focuses on are called features.
	- each data point is a list - of vector - of such feature
	- the input into an ML algorithm is a feature vector.
	- feature vectors are usually called the X variables.

	- Y-VARIBLES:
	- the attributes that the ML algorithm tries to predict are called labels.
	- types of labels - categorical (cases where output of the model is classification) or continuous (regression)

- Unsupervised Learning - no information about the correct output for each input is given, inorder to extract patterns and/or
	learn representations. The model has to be set up right to learn structure in the data.
- Overfitting
- Underfitting
- Precision vs Recall - Recall measures the quantity of relevant results returned by a search, while precision is the measure of the quality of the results returned. Recall is the ratio of relevant results
	returned to all relevant results. Precision is the number of relevant results returned to the total number of results returned.
	full-text-search search systems typically includes options like Stop Word to increase precision and stemming to increase recall.

"""