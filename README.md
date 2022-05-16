# NLP-Spam-Classification
NLP Pipeline for Spam Emails Classification
## Introduction
Spam emails classification accounts for a a great deal of tasks in internet security. This raises the need for a perfect classifier to protect agents from malware attacks.<br>In this project we will be processing the email raw text and get insights about the key words that most spam emails share. For the sake of maximum security, we will use two frameworks to solve the problem, `TensorFlow` and `NLTK`, and use an `or` gate to combine the results.
## Repository Content
01. [Dataset](https://github.com/E-Hossam96/NLP-Spam-Classification/tree/main/dataset): Spam classification raw texts. This dataset is available on **Kaggle** through this [link](https://www.kaggle.com/datasets/chandramoulinaidu/spam-classification-for-basic-nlp).
02. [Static](https://github.com/E-Hossam96/NLP-Spam-Classification/tree/main/static): Styles of the webpages and sample photos for visualization.
03. [Templates](https://github.com/E-Hossam96/NLP-Spam-Classification/tree/main/templates): **HTML** webpages to be used by `Flask`.
04. [app.py](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/app.py): The running web application code using `Flask`.
05. [ensure_validity.ipynb](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/ensure_validity.ipynb): A notebook to check if the functions, parameters, and models are loaded properly.
06. [nltk_features.json](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/nltk_features.json): JSON file contained the selected features using the `NLTK` module.
07. [nltk_functions.py](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/nltk_functions.py): Processing functions for the `NLTK` model.
08. [nltk_model.joblib](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/nltk_model.joblib): The classical ML model to be loaded in the production environment.
09. [nltk_processing.ipynb](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/nltk_processing.ipynb): A notebook containing the modeling processes using the `NLTK` module.
10. [tensorflow_processing.ipynb](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/tensorflow_processing.ipynb): A notebook containing the modeling processes using the **`TensorFlow`** software.
11. [tf_model.h5](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/tf_model.h5): The *DNN* model weights and architecture to be loaded in the production environment.
12. [tf_params.json](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/tf_params.json): JSON file containing the setting paramerts of the **`TensorFlow`** sequence padding.
13. [tf_tokenizer.json](https://github.com/E-Hossam96/NLP-Spam-Classification/blob/main/tf_tokenizer.json): JSON file containing the **`TensorFlow`** tokenizer object.
