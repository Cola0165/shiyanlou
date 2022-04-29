import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess


def test():
    # build a list MA parameters
    ma = [0.8 ** i for i in range(30)]

    # Simulate the MA(30) model
    ar = np.array([1])
    AR_object = ArmaProcess(ar, ma)
    simulated_data = AR_object.generate_sample(nsample=5000)

    # Plot the ACF
    plot_acf(simulated_data, lags=30)
    plt.savefig('/tmp/arma_acf.png')


if __name__ == '__main__':
    test()