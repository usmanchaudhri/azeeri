"""
- using Neural search (deep artifical neural networks) helps to -
	- automate extraction of synonyms from searh engine data.
	- avoiding manual editing of synonym files.
	- good related context suggestions.
	- searching context in multiple languages and searching for images.
- difficult to define the boundaries of "enough data" in a generic way
- how to make machines "learn" using the deep neural network computing model.
- vector Space Model (VSM) is a classical retreival models. In VSM the document and query is represented as a vector.
	You can think of a vector as an arrow in a coordinate plane; each arrow in VSM can represent a query or a document.
	The closer two arrows are, the more similar they are each arrow’s direction is defined by the terms that compose the query/document.
- in VSM search results are ranked with respect to the query vector, so documents appear higher in the results list (get a higher rank/score)
	if they're closer to such query vector.
- precision vs recall - A standard way of measuring how well an information retreival system is doing is to calculate its precision and recall.
- precision is the fraction of retrieved documents that are relevant. If a system has high precision, users will mostly find results they’re looking
	for at the top of the list of search results.
- recall is the fraction of relevant documents that are retrieved. If a system has a good recall, users will find all results relevant for them in
	the search results, although they might not all be among the top results.
- measuring precision and recall requires someone to judge how relevant search results are.
- vector space models and probabilistic models.
- Deep Learning will help built smarter search engines.
- how can a computer tell whether an image represents a running lion, a refrigerator, a group of monkeys, and so on.
	Deep Learning can help solve this problem with the creation of a special type of deep neural network that could
	learn image representation incrementally.
- DL is a subfield of ML that focuses on learning deep representations of text, images, or data in general by learning successive
	abstractions of increasingly meaningful representations.
- A neural network is considered deep when it has at least two hidden layers
- word2vec to learn vector representation of words - how closely related they are.
- Skip-gram is another technique to extract words.
- It would be nice to have a retrieval model that relies on word and document vectors (also called embeddings)
	with these capabilities, so we could calculate and use document and word similarities efficiently by looking
	at the nearest neighbors
- One of the key ideas of neural search is to use such representations - represents words close to each other - to improve the effectiveness of search engines
- Deep learning vs Deep neural networks - Deep learning is mostly about learning representations of words, text, documents, and images by using deep neural networks.
	In addition to learning representations, deep neural networks can help solve a number of information retrieval tasks.


"""