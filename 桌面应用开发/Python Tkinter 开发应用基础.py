# -*- coding: UTF-8 -*-
from tkinter import Tk, Button, messagebox

class NumberRecorder:
    def __init__(self) -> None:
        self.numbers = []

    def render(self):
        self.main_window = Tk()
        show = Button(
            self.main_window,
            text=f"查看结果",
            command=self.on_show
        )
        show.pack()

        # TODO(You): 请在此组装1-9数字按钮
        for i in range(0, 9):
            number = Button(
                self.main_window,
                text=f"{i}",
                command=lambda: self.on_click(i)
            )
            number.pack()

        self.main_window.mainloop()

    def on_show(self):
        messagebox.showinfo("输入数字", f"{','.join(self.numbers)}")

    def on_click(self, i):
        self.numbers.append(i)

if __name__ == '__main__':
    app = NumberRecorder()
    app.render()