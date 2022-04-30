import jieba
import numpy as np

import os
import jieba
import numpy as np
import joblib
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Dataset:
    def __init__(self, dataset_file) -> None:
        self.dataset_file = dataset_file
        self.train_sentences = None
        self.test_sentences = None

    def generate(self):
        return [
            '今天 天气 很 好',
            '今天很 好',
            '今天 天气 很 好',
            '今天 天气 很 好',
            '今天 天',
            '今天 天气 很 好',
            '今天 天气 很 好',
            '今天 天气 很 好',
            '今天 天气 很 好',
            '今天 天',
            '今天 天气 很 好',
            '气 很 好',
            '今天 天气 很 差',
            '不错',
            '还行'
        ]

    def load(self):
        if os.path.exists(self.dataset_file):
            with open(self.dataset_file, 'r') as f:
                ret = json.loads(f.read())
                self.train_sentences = ret['train']
                self.test_sentences = ret['test']
        else:
            sentences = self.generate()
            with open(self.dataset_file, 'w') as f:
                cut = len(sentences)-5
                ret = {
                    'train': sentences[:cut],
                    'test': sentences[cut:],
                }
                f.write(json.dumps(ret))


class TFIDFSimilar:
    def __init__(self, tfidf_vectorizer=None, tfidf_matrix=None) -> None:
        self.tfidf_vectorizer = tfidf_vectorizer
        self.tfidf_matrix = tfidf_matrix

    def __train_model(self, sentences):
        for s in sentences:
            if s.strip() != '':
                vec = [" ".join(jieba.cut(str(s), cut_all=False))]
        self.tfidf_vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(vec)

    @staticmethod
    def load_model(model_file):
        model_obj = joblib.load(model_file)
        return TFIDFSimilar(model_obj['vec'], model_obj['matrix'])

    def save(self, model_file):
        model_obj = {
            'vec': self.tfidf_vectorizer,
            'matrix': self.tfidf_matrix
        }
        joblib.dump(model_obj, model_file)

    def fit(self, sentences):
        self.__train_model(sentences)

    def predict(self, sentence, topk):
        v = ' '.join(jieba.cut(sentence, cut_all=False))
        v_q = self.tfidf_vectorizer.transform([v])
        cosine_similarities = cosine_similarity(
            v_q, self.tfidf_matrix).flatten()

        extend_top_k = min(3*topk, len(cosine_similarities))
        topk_idx = cosine_similarities.argsort()[:-extend_top_k-1:-1]
        return topk_idx


if __name__ == "__main__":
    # 准备数据集
    dataset_file = '/tmp/nlp_tfidf.dataset'
    dataset = Dataset(dataset_file)
    dataset.load()

    # 训练模型
    model_file = '/tmp/nlp_tfidf.model'
    if os.path.exists(model_file):
        model = TFIDFSimilar.load_model(model_file)
    else:
        print(dataset.train_sentences)
        model = TFIDFSimilar()
        model.fit(dataset.train_sentences)
        model.save(model_file)

    # 预测
    print("目标句子：", dataset.test_sentences[1])
    topk = 2
    topk_idx = model.predict(dataset.test_sentences[2], topk)
    for idx in topk_idx:
        print(dataset.train_sentences[idx])