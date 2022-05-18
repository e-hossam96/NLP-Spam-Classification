# NLP-Spam-Classification
End to End NLP Pipeline for Spam Emails Classification

## Introduction
Spam emails classification accounts for a a great deal of tasks in internet security. This raises the need for a perfect classifier to protect agents from malware attacks.<br>In this project we will be processing the email raw text and get insights about the key words that most spam emails share. For the sake of maximum security, we will use two frameworks to solve the problem, `TensorFlow` and `NLTK`, and average to combine the results.

## NLP Techniques

### NLTK Processes
#### Processing
In this section I have proceesed the data using the NLTK framework. First, I tokenized the messages using `RegexpTokenizer`. Then, I lemmatized them using `WordNetLemmatizer`. Lastly, I removed the stop words and produced the tokens in its useful form.
#### Feature Selection and Modeling
To select the most important tokens, I generated a token counter to count the frequencies of each token in the training dataset. Then, I kept only the tokens that was repeated more than *1000* times. Now that I have the features set, I defined a counts vector to store the frequencies of the features tokens in each message. Lastly, I trained a `RandomForestClassifier` and achieved 98% accuracy on the test set.<br><br>
This section is found in the [nltk_processing](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/nltk_processing.ipynb) notebook.

### TensorFlow Processes
#### Processing
The work is pretty much easier here. First, I fitted the `Keras.preprocessing.text.Tokenizer` on the training dataset and then padded the sequences using the `keras.preprocessing.sequence.pad_sequences` to produce inputs with equal lengths.
#### Modeling
I have constructed a simple *DNN* and fitted the it on the data. The model achieved 99% accuracy on the validation datset.<br><br>
This section is found in the [tensorflow_processing](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/tensorflow_processing.ipynb) notebook.

## Models Deployment
