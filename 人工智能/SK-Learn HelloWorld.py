from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import random


def plot_result(data, cluster_res, cluster_num, algorithm='None'):
    nPoints = len(data)
    scatter_colors = ['blue', 'green', 'yellow',
                      'red', 'purple', 'orange', 'brown']
    for i in range(cluster_num):
        color = scatter_colors[i % len(scatter_colors)]
        x1 = []
        y1 = []
        for j in range(nPoints):
            if cluster_res[j] == i:
                x1.append(data[j, 0])
                y1.append(data[j, 1])
        plt.scatter(x1, y1, c=color, alpha=1, marker='o')
        plt.plot(marksize=10)
    plt.savefig('/tmp/' + algorithm + '-' +
                str(random.randint(10, 100)) + str(cluster_num) + '.png')
    plt.show()


def kmeans(sentences, num_of_class):
    # tfidf 向量化
    vertorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.46)
    transformer = TfidfTransformer()
    freq_words_matrix = vertorizer.fit_transform(sentences)

    # 获取词袋
    words = vertorizer.get_feature_names()
    tfidf = transformer.fit_transform(freq_words_matrix)
    weight = freq_words_matrix.toarray()
    trainingData = weight

    # K-Means 聚类
    clf = KMeans(
        n_clusters=num_of_class,
        max_iter=10000,
        init="k-means++",
        tol=1e-6
    )
    result = clf.fit(trainingData)
    source = list(clf.predict(trainingData))
    labels = clf.labels_

    # # 显示聚类结果
    plot_result(trainingData, source, num_of_class)


if __name__ == "__main__":
    sentences = [
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

    kmeans(sentences, 3)