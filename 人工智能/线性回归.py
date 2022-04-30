import os
import joblib
import numpy as np


class Dataset:
    def __init__(self, data=None) -> None:
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None
        if data:
            self.x_train = data['x_train']
            self.y_train = data['y_train']
            self.x_test = data['x_test']
            self.y_test = data['y_test']

    @staticmethod
    def load_data(dataset_file):
        data = joblib.load(dataset_file)
        return Dataset(data)

    def generate(self):
        x = np.random.rand(100, 1)
        y = 3 + 6 * x + .1 * np.random.randn(100, 1)

        # split
        order = np.random.permutation(len(x))
        portion = 20
        x_train, y_train = x[order[portion:]], y[order[portion:]]
        x_test, y_test = x[order[:portion]], y[order[:portion]]

        self.data = {
            'x_train': x_train,
            'y_train': y_train,
            'x_test': x_test,
            'y_test': y_test
        }

    def save(self, dataset_file):
        joblib.dump(self.data, dataset_file)


class Model:
    def __init__(self, w0=None, w1=None) -> None:
        self.w0 = w0
        self.w1 = w1

    def fit(self, x_train, y_train, epoch_count=100):
        np.random.seed(42)
        w0 = np.random.randn(1)
        w1 = np.random.randn(1)

        learning_rate = 1e-1
        for epoch in range(epoch_count):
            y_new = w0 + w1 * x_train
            error = (y_train - y_new)

            w1_grad = -2 * error.mean()
            w2_grad = -2 * (x_train * error).mean()

            w0 -= learning_rate * w1_grad
            w1 -= learning_rate * w2_grad

        self.w0 = w0
        self.w1 = w1

    def predict(self, x):
        return self.w0+self.w1*x

    def save(self, model_file):
        joblib.dump({"w0": self.w0, "w1": self.w1}, model_file)

    @staticmethod
    def load_model(model_file):
        model_obj = joblib.load(model_file)
        return Model(model_obj['w0'], model_obj['w1'])


if __name__ == "__main__":
    # load dataset
    dataset_file = '/tmp/np_linear_regression.dataset'

    if os.path.exists(dataset_file):
        dataset = Dataset.load_data(dataset_file)
    else:
        dataset = Dataset()
        dataset.generate()
        dataset.save(dataset_file)

    # load model
    model_file = '/tmp/np_linear_regression.model'
    if os.path.exists(model_file):
        print(model_file)
        model = Model.load_model(model_file)
    else:
        model = Model()
        model.fit(dataset.x_train, dataset.y_train)
        model.save(model_file)

    # predict
    y_predict = model.predict(dataset.x_test)

    # compare
    print(y_predict)
    print(dataset.y_test)