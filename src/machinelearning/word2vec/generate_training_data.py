import re
import numpy as np

def tokenize(text: str):
    # obtains tokens with atleast 1 alphabet
    pattern = re.compile(r'[A-Za-z]+[\w^\']*|[\w^\']*[A-Za-z]+[\w^\']*')
    return pattern.findall(text.lower())

def mapping(tokens):
    word_to_id = dict()
    id_to_word = dict()

    for i, token in enumerate(set(tokens)):
        word_to_id[token] = i
        id_to_word[i] = token

    return word_to_id, id_to_word

def generate_training_data(tokens, word_to_id, window_size):
    N = len(tokens)
    X, Y = [], []
    for i in range(N):
        # generate ranges left and right of the current token
        # range(i-window_size, i-1) && range(i+1, i+window_size)
        nbr_inds = list(range(max(0, i - window_size), i)) + list(range(i+1, min(N, i+window_size+1)))
        for j in nbr_inds:
            X.append(word_to_id[tokens[i]])
            Y.append(word_to_id[tokens[j]])

    X = np.array(X)
    X = np.expand_dims(X, axis=0)
    Y = np.array(Y)
    Y = np.expand_dims(Y, axis=0)

    return X, Y

def initialize_wrd_embed(vocab_size, emb_size):
    """
    vocab_size: int. vocabulary size of your corpus or training data
    emb_size: int. word embedding size. How many dimensions to represent each vocabulary
    """
    WRD_EMB = np.random.randn(vocab_size, emb_size) * 0.01
    return WRD_EMB

def initialize_dense(input_size, output_size):
    """
    input_size: int. size of the input to the dense layer
    output_szie: int. size of the output out of the dense layer
    """
    W = np.random.randn(output_size, input_size) * 0.01
    return W

def initialize_parameters(vocab_size, emb_size):
    """
    initialize all the trianing parameters
    """
    WRD_EMB = initialize_wrd_embed(vocab_size, emb_size)
    W = initialize_dense(emb_size, vocab_size)

    parameters = {}
    parameters['WRD_EMB'] = WRD_EMB
    parameters['W'] = W

    return parameters


if __name__ == "__main__":
    tokens = tokenize("usman chaudhri likes to eat bbq lamb chops")
    word_to_id, id_to_word = mapping(tokens)
    X, Y = generate_training_data(tokens, word_to_id, 1)
    vocab_size = len(id_to_word)
    m = Y.shape[1]

    # turn Y into one hot encoding
    Y_one_hot = np.zeros((vocab_size, m))
    Y_one_hot[Y.flatten(), np.arange(m)] = 1
    print(Y_one_hot)




