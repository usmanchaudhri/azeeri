"""
- Neural networks can easily represent many interesting mathematical functions; that’s one of the reasons they can have very high accuracy.
- A Neural network learning algorithm takes the discrepancies between desired and actual outputs and adjusts each
layer’s weights to reduce the output error in the future.
- Activation functions have an impact on a neural network’s ability to perform predictions and on how quickly it learns; the activation functions control when and how much the incoming signal to a neuron is propagated throughout to the output connections.
- Backpropogation - The most commonly used learning algorithm for neural networks.
- A typical development workflow for an ML task involves these steps:
	1. Choosing and gathering data to be used as the training set
	2. Keeping some portions of the training set apart for evaluation and tuning ⬆ (test and cross-validation sets)
	3. Training a few ML models according to algorithms (feed-forward neural networks, support vector machines, and so on) and
		hyperparameters (for example, the number of layers and the number of neurons in each layer for neural networks)
	4. Evaluating and tuning the model over test and cross-validation sets.
	5. Choosing the best-performing model and using it to solve the desired task.
- online learning - not require retraining.
- Neural networks can be used to generate word vectors that capture word semantics so that words with similar meanings
	will have word vectors close to one another.
- Deep neural networks can learn image representations that give surprisingly good results in image search. Simple similarity measures like cosine distance can be applied to DL-generated representations of
	data to capture semantically similar words, sentences, paragraphs, and so on; this has a number of applications, such as in the text analysis phase and in recommending similar documents.
- improve search engine by better capture user intent by expanding synonyms, generating alternative representations of a query,
	and giving smarter suggestions while the user is searching. A query can be expanded, adapted, and transformed before matching with the terms
	stored in the inverted indexes is performed.
- These matching documents, also known as search results, are sorted according to how closely they’re predicted to match the input query. This task of sorting the results is known as ranking or scoring.
- common ranking functions -
- information retreival models -
- how a search engine decides which results to show first
- how to improve search engine ranking functions by using dense vector representations of text (words, sentences, documents, and so on).
	Also known as embeddings, these vector representations of text can help your ranking functions to do a better job matching and scoring
	documents according to the user’s intent.

"""