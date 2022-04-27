# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class QProgressThread(QThread):
    _signal = pyqtSignal(ProgressInfo)

    def __init__(self, runner):
        super(QProgressThread, self).__init__()
        self.runner = runner

    def run(self):
        # TODO(You): 请在此实现运行代码
        def emit_progress(progress, msg):
            info = ProgressInfo(progress, msg)
            self._signal.emit(info)
        self.runner(emit_progress)

    def connect(self, on_signal):
        # TODO(You): 请在此实现绑定信号事件代码
        self._signal.connect(on_signal)

    def __del__(self):
        self.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    def on_run(emit_progress):
        for i in range(0, 5):
            msg = f"Hello PyQT world:{i/5}!"
            emit_progress(i, msg)

    p = QProgressThread(on_run)

    def on_signal(info):
        print("accept info from signal:", info.msg)
        QApplication.quit()
    p.connect(on_signal)

    p.start()
    sys.exit(app.exec_())