import time
from tkinter import Canvas

class AStar:
    def __init__(self, s: str, t: str) -> None:
        self.s = s
        self.t = t

        self.create_graph()

    N = 11
    M = 11 #размер сетки квадратов

    def Potent(self, v: tuple, t: tuple): # v = (x,y,index)
        H = 0
        if v[2] == t[2]:
            H=0
        else:
            if v[2]=='l':
                if (v[0]+v[1]-t[0] <= t[1]):
                    H=1
                else:
                    H=-1
            else:
                if (v[0]+v[1]-t[0] <= t[1]):
                    H=-1
                else:
                    H=1
        return 2*(abs(t[1]-v[1])+abs(t[0]-v[0]))+H
    

    def Draw(self, canvas: Canvas):
        for i in self.path:
            wh=700
            a1=wh * 0.1
            x=(i[0]-1)*a1
            y=i[1]*a1
            self.col="#ffffff"
            if i == self.path[0]:
                self.col="#4b9ceb"
            elif i == self.path[-1]:
                self.col="#e82a63"
            if i[2]=="l":
                canvas.create_polygon(x+a1, y, x, y-a1, x, y, fill=self.col, outline="#004D40", width=2)
            else:
                canvas.create_polygon(x+a1, y, x, y-a1, x+a1, y-a1, fill=self.col, outline="#004D40", width=2)

    def clear_field(self, canvas: Canvas):
        for i in self.path:
            wh=700
            a1=wh * 0.1
            x=(i[0]-1)*a1
            y=i[1]*a1
            if i[2]=="l":
                canvas.create_polygon(x+a1, y, x, y-a1, x, y, fill="#80CBC4", outline="#004D40", width=2)
            else:
                canvas.create_polygon(x+a1, y, x, y-a1, x+a1, y-a1, fill="#80CBC4", outline="#004D40", width=2)


    COUNT = 2*N*M

    def create_graph(self):
        '''

        | 0 | 1 | 2 |...|N-1 |
        | N |N+1|N+2|...|2N-1|

        |  ... |   ...  |...|  ... |
        |N(M-1)|N(M-1)+1|...|NM - 1|

        Номера вершин (квадратов)
        '''
        #Построим списки смежности вершин. Т.е. вершина (N+1) соседствует с вершинами 1, N, N+2, 2N+1
        #for i in range(0,N):
            #for j in range(0,M):
                #Graph = [(i,j,'r'),(i-1,j,'r'),(i,j+1,'r')]
                #Graph = [(i,j,'l'),(i+1,j,'l'),(i,j-1,'l')]
        Graph = dict() #<--- Требуется использовать словарь
        #-------------------------------------СОСТАВЛЕНИЕ ГРАФА------------------------------------
        #-------------------ОБРАБОТКА УГЛОВ---------------------------------
        Graph[(0,0,'l')] = [] #Необходимо объявлять массив
        Graph[(0,0,'l')].append((0,0,'r'))
        Graph[(0,0,'l')].append((0,1,'r'))
        Graph[(0,0,'r')] = []
        Graph[(0,0,'r')].append((0,0,'l'))
        Graph[(0,0,'r')].append((1,0,'l'))

        Graph[(self.N-1,0,'l')] = []
        Graph[(self.N-1,0,'l')].append((self.N-1,0,'r'))
        Graph[(self.N-1,0,'l')].append((self.N-2,0,'r'))
        Graph[(self.N-1,0,'l')].append((self.N-1,1,'r'))
        Graph[(self.N-1,0,'r')] = []
        Graph[(self.N-1,0,'r')].append((self.N-1,0,'l'))

        Graph[(0,self.M-1,'l')] = []
        Graph[(0,self.M-1,'l')].append((0,self.M-1,'r'))
        Graph[(0,self.M-1,'r')] = []
        Graph[(0,self.M-1,'r')].append((0,self.M-1,'l'))
        Graph[(0,self.M-1,'r')].append((1,self.M-1,'l'))
        Graph[(0,self.M-1,'r')].append((0,self.M-2,'l'))

        Graph[(self.N-1,self.M-1,'l')] = []
        Graph[(self.N-1,self.M-1,'l')].append((self.N-1,self.M-1,'r'))
        Graph[(self.N-1,self.M-1,'l')].append((self.N-2,self.M-1,'r'))
        Graph[(self.N-1,self.M-1,'r')] = []
        Graph[(self.N-1,self.M-1,'r')].append((self.N-1,self.M-1,'l'))
        Graph[(self.N-1,self.M-1,'r')].append((self.N-1,self.M-2,'l'))
        #-------------------------------------------------------------------
        for i in range(1,self.N-1): #Верхняя и нижняя полосы
            Graph[(i,0,'l')] = []
            Graph[(i,0,'l')].append((i,0,'r'))
            Graph[(i,0,'l')].append((i,1,'r'))
            Graph[(i,0,'l')].append((i-1,0,'r'))
            
            Graph[(i,0,'r')] = []
            Graph[(i,0,'r')].append((i,0,'l'))
            Graph[(i,0,'r')].append((i+1,0,'l'))
            
            Graph[(i,self.M-1,'l')] = []
            Graph[(i,self.M-1,'l')].append((i,self.M-1,'r'))
            Graph[(i,self.M-1,'l')].append((i-1,self.M-1,'r'))
            
            Graph[(i,self.M-1,'r')] = []
            Graph[(i,self.M-1,'r')].append((i,self.M-1,'l'))
            Graph[(i,self.M-1,'r')].append((i,self.M-2,'l'))
            Graph[(i,self.M-1,'r')].append((i+1,self.M-1,'l'))
            
        for i in range(1,self.M-1): #Левая и правая полосы
            Graph[(0,i,'l')] = []
            Graph[(0,i,'l')].append((0,i,'r'))
            Graph[(0,i,'l')].append((0,i+1,'r'))
            
            Graph[(0,i,'r')] = []
            Graph[(0,i,'r')].append((0,i,'l'))
            Graph[(0,i,'r')].append((0,i-1,'l'))
            Graph[(0,i,'r')].append((1,i,'l'))
            
            Graph[(self.N-1,i,'l')] = []
            Graph[(self.N-1,i,'l')].append((self.N-1,i,'r'))
            Graph[(self.N-1,i,'l')].append((self.N-1,i+1,'r'))
            Graph[(self.N-1,i,'l')].append((self.N-2,i,'r'))
            
            Graph[(self.N-1,i,'r')] = []
            Graph[(self.N-1,i,'r')].append((self.N-1,i,'l'))
            Graph[(self.N-1,i,'r')].append((self.N-1,i-1,'l'))
            
        for i in range(1,self.N-1):
            for j in range(1,self.M-1): #Сердцевина
                Graph[(i,j,'l')] = []
                Graph[(i,j,'l')].append((i,j,'r')) 
                Graph[(i,j,'l')].append((i,j+1,'r')) 
                Graph[(i,j,'l')].append((i-1,j,'r'))
                
                Graph[(i,j,'r')] = []
                Graph[(i,j,'r')].append((i,j,'l'))
                Graph[(i,j,'r')].append((i,j-1,'l')) 
                Graph[(i,j,'r')].append((i+1,j,'l')) 
        #-------------------------------------КОНЕЦ СОСТАВЛЕНИя ГРАФА------------------------------------
        # s = input(f'Введите координаты стартовой вершины (x, y, index): ')
        # t = input(f'Введите координаты целевой вершины (x, y, index): ')
        buf = self.s.split()
        s = (int(buf[0]),int(buf[1]),buf[2])
        buf = self.t.split()
        t = (int(buf[0]),int(buf[1]),buf[2])
        #Wer = int(input(f'Введите индекс (l или r): '))
        start_time = time.time()
        '''
        if s < 0 or s >= COUNT or t < 0 or t >= COUNT:
            print('Некорректные номера вершин!')
            exit(-1)
        '''
        #Другие размеры массивов
        D = {} # текущая оценка длины от стартовой вершины до текущей
        F = {} #Финальная стоимость как D + Potent
        H = {} # множество родительских вершин (из какой вершины ведет кратчайший путь)
        X = set() # множество меток 0 - временная; 1 - постоянная
        D[s] = 0
        H[s] = -1
        X.add(s)
        p = s
        while p != t: # пока последняя постоянная метка не была присвоена целевой вершине
            for v in Graph[p]: #Обновляем информацию о кратчайших путях для соседних с текущей вершиной p
                if D.get(v,self.COUNT) > D[p] + 1: #Вместо 1 должен быть вес ребра, но мы считаем, что всякий переход между клетками равен 1
                    D[v] = D[p] + 1 #Если через вершину p путь до v короче, то обновляем его
                    F[v] = D[v] + self.Potent(v=v, t=t) # Применение потенциальной
                    H[v] = p #Запоминаем нового родителя
            newMin = self.COUNT
            newP = -1
            for i in F.keys(): #Необходимо найти следующую вершину, которая получит постоянную метку. Т.е. с текущим минимальным расстоянием до нее
                if i not in X and F[i] < newMin: #При этом нужно искать только среди вершин с временной меткой. (Здесь можно оптимизировать код)
                    newP = i
                    newMin = F[i] #Все F изменить на D для Дейкстры
            X.add(newP) #Обновляем метку у вершины с минимальным расстоянием
            p = newP #Делаем ее новой текущей вершиной
        # После окончания цикла мы найшли кратчайший путь
        # Найдем номера вершин входящие в него
        start_time = time.time()-start_time
        v = t
        self.path = []
        while v != -1:
            self.path.append(v)
            v = H[v] #переходим к родителю
        self.path = self.path[::-1]
        # print('Путь состоит из вершин', self.path, 'и его длина равна', D[t])
        # print(f'Время на нахождение пути {start_time}')