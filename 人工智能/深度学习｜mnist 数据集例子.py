import tensorflow as tf
from tensorflow.keras.datasets import mnist
import os


class Classifier:
    def __init__(self) -> None:
        self.x_train = None
        self.x_test = None
        self.model_file = '/tmp/tensor.keras.model'
        self.has_load = False
        self.has_model_load = False

    def load_or_train(self):
        if self.has_load:
            return {'err': 0}
        try:

            if os.path.exists(self.model_file):
                self.__load_model()
            else:
                self.__train_model()
            self.has_load = True
            return {'err': 0}
        except Exception as e:
            return {'err': 1, 'msg': str(e)}

    def __create_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        return model

    def __train_model(self):
        if self.has_model_load:
            return
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0
        self.model = self.__create_model()
        self.model.fit(x_train, y_train, epochs=5)
        self.model.evaluate(x_test,  y_test, verbose=2)
        self.model.save(self.model_file)
        self.has_model_load = True

    def __load_model(self):
        if self.has_model_load:
            return
        self.model = tf.keras.models.load_model(self.model_file)
        self.model.summary()
        self.has_model_load = True

    def predict(self, test_images):
        if not self.has_load:
            return {'err': 1, 'msg': "分类器还没加载"}
        result = self.model.predict(test_images)
        return {'err': 0, 'result': result}


if __name__ == "__main__":

    cl = Classifier()

    # 加载或训练模型
    ret = cl.load_or_train()
    if ret['err'] != 0:
        print(ret['msg'])
    else:
        # 测试数据
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
        test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

        # 预测
        ret = cl.predict(test_images)
        if ret['err'] == 0:
            print('预测结果：', ret['result'])
        else:
            print('预测失败:{}', ret['msg'])