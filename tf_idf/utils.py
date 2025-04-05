from io import BytesIO
from typing import TypeAlias
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


WordList: TypeAlias = list[str]
TfIdfMatrix: TypeAlias = list[list[float]]


def compute_tf_idf(
    corpus: list[BytesIO]
) -> tuple[WordList, TfIdfMatrix]:

    vectorizer = CountVectorizer(input='file')
    X = vectorizer.fit_transform(corpus)

    count_array = X.toarray()
    tf_array = np.round(count_array / count_array.sum(axis=1).reshape(-1, 1), 3)

    num_files = tf_array.shape[0]
    idf = np.log(num_files / np.count_nonzero(tf_array, axis=0))
    idf = np.round(idf, 3)
    tf_idf_array = np.vstack((tf_array, idf)).T

    sort_idx = tf_idf_array[:, -1].argsort()

    tf_idf_array = tf_idf_array[sort_idx]
    words = vectorizer.get_feature_names_out()[sort_idx]

    return words.tolist(), tf_idf_array.tolist()

def trunc_str(line, width=10, placeholder='...'):
    return f'{line[:width-3]}...' if len(line) > width else line


if __name__ == '__main__':
    pass
