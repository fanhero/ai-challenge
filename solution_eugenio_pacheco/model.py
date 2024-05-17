import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('all')
from joblib import dump

def preprocess_text(text):
    text = re.sub(r"https?://\S+|www\.\S+"," ",text)
    text = re.sub(r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});"," ",text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\w*\d\w*", " ", text)
    text = re.sub(r"[0-9]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

df = pd.read_csv('training.csv', encoding='ISO-8859-1', header=None)
df.columns = ['target', 'ids', 'date', 'flag', 'user', 'text']

sample_size_per_class = 10000
positive_sample = df[df['target'] == 4].sample(n=sample_size_per_class, random_state=23)
negative_sample = df[df['target'] == 0].sample(n=sample_size_per_class, random_state=23)
df = pd.concat([positive_sample, negative_sample])
df.loc[:, 'text'] = df['text'].apply(preprocess_text)

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['target'], test_size=0.3)
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
X_train_vectorized = X_train_vectorized.todense()
X_test_vectorized = X_test_vectorized.todense()
encoder = LabelEncoder()
y_train_encoded = to_categorical(encoder.fit_transform(y_train))
y_test_encoded = to_categorical(encoder.transform(y_test))
model = Sequential()
model.add(Dense(512, input_shape=(X_train_vectorized.shape[1],), activation='relu'))
model.add(Dense(2, activation='softmax')) 
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_vectorized, y_train_encoded, epochs=10, batch_size=128, validation_data=(X_test_vectorized, y_test_encoded), verbose=1)
model.save('model.keras')
dump(vectorizer, 'vectorizer.joblib')