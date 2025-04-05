import re, string

pattern2 = fr'{string.punctuation}'
pattern1 = r'[\w’-]+'

regex = fr'(?<!{pattern2})\b{pattern1}\b(?!{pattern2})'

re.findall(regex, 's')

#########

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

features = vectorizer.get_feature_names_out()

mat = X.toarray()
tf_mat = np.round(mat / mat.sum(axis=1).reshape(-1, 1), 2)

# tf_mat
# array([[0.  , 0.2 , 0.2 , 0.2 , 0.  , 0.  , 0.2 , 0.  , 0.2 ],
#        [0.  , 0.33, 0.  , 0.17, 0.  , 0.17, 0.17, 0.  , 0.17],
#        [0.17, 0.  , 0.  , 0.17, 0.17, 0.  , 0.17, 0.17, 0.17],
#        [0.  , 0.2 , 0.2 , 0.2 , 0.  , 0.  , 0.2 , 0.  , 0.2 ]])

D = tf_mat.shape[0]
idf = np.log(D / np.count_nonzero(tf_mat, axis=0))
tf_idf = np.vstack((tf_mat, idf)).T

sort_idx = tf_idf[:, -1].argsort()
result = tf_idf[sort_idx]
features = features[sort_idx]

# array([[0.2       , 0.17      , 0.17      , 0.2       , 0.        ],
#        [0.2       , 0.17      , 0.17      , 0.2       , 0.        ],
#        [0.2       , 0.17      , 0.17      , 0.2       , 0.        ],
#        [0.2       , 0.33      , 0.        , 0.2       , 0.28768207],
#        [0.2       , 0.        , 0.        , 0.2       , 0.69314718],
#        [0.        , 0.        , 0.17      , 0.        , 1.38629436],
#        [0.        , 0.17      , 0.        , 0.        , 1.38629436],
#        [0.        , 0.        , 0.17      , 0.        , 1.38629436],
#        [0.        , 0.        , 0.17      , 0.        , 1.38629436]])