from tkinter import Tk, BOTH, W, E, Canvas
from tkinter.ttk import Frame, Button, Label, Entry
from AStar import AStar


class Example(Frame):
    wh = 700
    def way(self):
        for i in range(0,10):
            for j in range(0,10):
                a1=self.wh * 0.1
                x=i*a1
                y=(10-j)*a1
                self.canvas.create_polygon(x+a1, y, x, y-a1, x, y, fill="#80CBC4", outline="#004D40", width=2)
                self.canvas.create_polygon(x+a1, y, x, y-a1, x+a1, y-a1, fill="#80CBC4", outline="#004D40", width=2)
        self.s = str(int(self.input_X1.get())) + " " + str(int(self.input_Y1.get())) + " " + self.input_index_1.get()
        self.t = str(int(self.input_X2.get())) + " " + str(int(self.input_Y2.get())) + " " + self.input_index_2.get()
        AStar(self.s, self.t).Draw(canvas=self.canvas)
    
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        padding = 5

        # Название окна
        self.master.title("Проект визуализация графа")
        self.pack(fill=BOTH, expand=True)

        # Это тебе не надо
        self.columnconfigure(1, weight=2)
        self.columnconfigure(1, pad=7)
        self.rowconfigure(12, weight=1)

        # Надпись сверху для красоты
        lbl = Label(self, text="Визуализация графа")
        lbl.grid(sticky=W, pady=4, padx=5)

        # Холст
        self.canvas = Canvas(self, bg="white", width=self.wh, height=self.wh)
        for i in range(0,10):
            for j in range(0,10):
                a1=self.wh * 0.1
                x=i*a1
                y=(10-j)*a1
                self.canvas.create_polygon(x+a1, y, x, y-a1, x, y, fill="#80CBC4", outline="#004D40", width=2)
                self.canvas.create_polygon(x+a1, y, x, y-a1, x+a1, y-a1, fill="#80CBC4", outline="#004D40", width=2)
        self.canvas.grid(row=1, column=0, columnspan=2, rowspan=13, padx=padding)

        # Первые координаты
        coord_X1 = Label(self, text="X1:")  # Координата х1
        coord_X1.grid(row=1, column=3, sticky=W, padx=padding)

        self.input_X1 = Entry(self, width=8)  # Поле ввода координаты
        self.input_X1.grid(row=1, column=3, sticky=E, padx=padding)

        coord_Y1 = Label(self, text="Y1:")  # Координата у1
        coord_Y1.grid(row=2, column=3, sticky=W, padx=padding)

        self.input_Y1 = Entry(self, width=8)  # Поле ввода координаты
        self.input_Y1.grid(row=2, column=3, sticky=E, padx=padding)

        index_1 = Label(self, text="index1:")  # Индекс 1
        index_1.grid(row=3, column=3, sticky=W, padx=padding)

        self.input_index_1 = Entry(self, width=8)  # Поле ввода индекса 1
        self.input_index_1.grid(row=3, column=3, sticky=E, padx=padding)

        # Разделитель для красоты
        Label(self, text="").grid(row=4, column=3)

        # Вторые координаты
        coord_X2 = Label(self, text="X2:")  # Координата х2
        coord_X2.grid(row=5, column=3, sticky=W, padx=padding)

        self.input_X2 = Entry(self, width=8)  # Поле ввода координаты
        self.input_X2.grid(row=5, column=3, sticky=E, padx=padding)

        coord_Y2 = Label(self, text="Y2:")  # Координата у2
        coord_Y2.grid(row=6, column=3, sticky=W, padx=padding)

        self.input_Y2 = Entry(self, width=8)  # Поле ввода координаты
        self.input_Y2.grid(row=6, column=3, sticky=E, padx=padding)

        index_2 = Label(self, text="index2:")  # Индекс 2
        index_2.grid(row=7, column=3, sticky=W, padx=padding)

        self.input_index_2 = Entry(self, width=8)  # Поле ввода индекса 2
        self.input_index_2.grid(row=7, column=3, sticky=E, padx=padding)

        # Разделитель для красоты
        Label(self, text="").grid(row=9, column=3)

        # Построить граф
        cbtn = Button(self, text="Построить граф", command=self.way)  # Кнопка построения графика
        cbtn.grid(row=10, column=3, padx=padding)

        # Очистить поле
        # Button(self, text="Очистить поле", command=AStar(s=self.s, t=self.t).clear_field(canvas=self.canvas)).grid(row=11, column=3, padx=padding)

        # Работа с алгоритмом поиска пути



def main():
    root = Tk()
    root.geometry("900x800+300+300")
    Example()
    root.mainloop()


if __name__ == '__main__':
    main()
