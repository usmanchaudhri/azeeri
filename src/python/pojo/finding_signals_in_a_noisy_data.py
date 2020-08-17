"""
Find signals in a noisy poorly understood data.

- Collecting more data:
	The simplest way to handle noisy data is to collect more data. The more data you collect, the better will you be
	able to identify the underlying phenomenon that is generating the data. This will eventually help in reducing the
	effect of noise. Think about it – when survey companies conduct surveys, they do it on a mass scale. This is
	because a handful of survey responses might not be good for generalizing because humans tend to be moody and so,
	some may answer the survey negatively because of a possibly bad mood (noisy data). This may not reflect the actual
	 behavior of the masses unless the survey is conducted on a really large scale.

	As a rule of thumb – the larger the sample size, the better will you be able to uncover the actual behavior of
	the population.

- Cross Validation:
	Cross-validation is a technique that helps in tackling with noisy data by preventing overfitting. This is just like
	overfitting. In cross-validation, the dataset is broken into 3 sets (rather than 2):

	Training data
	Cross validation data
	Testing data
	The algorithm is trained using the training data. However, the hyper-parameters are tuned using the
	cross-validation data which is separate from the training data. This makes sure that the algorithm is able to
	avoid learning the noise present in the training data and rather generalize by a cross-validation procedure.
	Finally, the fresh, test data can be used to evaluate how well the algorithm was able to generalize.

	It is important for all data scientists to understand the impact the noise can create on the data and so, every
	data scientist must take appropriate measures to design algorithms accordingly. This way, the generalizing
	capabilities of the algorithm on new data will be far better.
"""
