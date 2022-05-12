from flask import Flask, render_template, request
from nltk_functions import text_to_tokens, text_to_count_vector
import tensorflow as tf
import numpy as np
import nltk
import json
import joblib

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def predict_spam():
    # getting the message
    message_file = request.form['text']
    message_fid = open(message_file, 'r')
    message = message_fid.read()

    # loading the tensorflow model
    # loading the tokenizer
    fid1 = open('tf_tokenizer.json', 'r')
    tf_tokenizer = json.load(fid1)
    tf_tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(
        tf_tokenizer)
    fid1.close()
    # loading the model
    tf_model = tf.keras.models.load_model('tf_model.h5')
    # loading the params
    fid2 = open('tf_params.json', 'r')
    tf_params = json.load(fid2)
    fid2.close()
    # predicting the result
    sequences = tf_tokenizer.texts_to_sequences([message])
    padded = tf.keras.preprocessing.sequence.pad_sequences(
        sequences,
        maxlen=tf_params['max_length'],
        padding=tf_params['padding_type'],
        truncating=tf_params['trunc_type']
    )
    tf_result = tf_model.predict(padded)

    # loading the nltk model
    # loading the model
    nltk_model = joblib.load('nltk_model.joblib')
    # loading parameters and processing functions
    fid3 = open('nltk_features.json', 'r')
    nltk_features = json.load(fid3)
    fid3.close()
    # setting the nltk parameters
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    lemmatizer = nltk.WordNetLemmatizer()
    stop_words = nltk.corpus.stopwords.words('english')
    # tokenizing the message
    message_vector = text_to_count_vector(
        message, nltk_features, tokenizer, lemmatizer, stop_words, np)
    nltk_probas = nltk_model.predict_proba([message_vector])
    nltk_result = nltk_probas[0][np.argmax(nltk_probas)]

    return render_template('result.html', data=(tf_result[0][0] + nltk_result)/2)


if __name__ == '__main__':
    app.run(debug=True)
