import threading
from estadistica_descriptiva import obtain_data

class my_thread(threading.Thread):
    
    def __init__(self, data_x:list, data_y:list):
        threading.Thread.__init__(self)
        self.data_x = data_x
        self.data_y = data_y
        self.xi = 0
        self.yi = 0
        self.xixi = 0
        self.xiyi = 0
    
    def calculate_xi(self):
        for i in self.data_x:
            self.xi += i
    
    def calculate_yi(self):
        for i in self.data_y:
            self.yi += i
        
    def calculate_xixi(self):
        for i in self.data_x:
            self.xixi += i * i
    
    def calculate_xiyi(self):
        for i in range(len(self.data_x)):
            self.xiyi += self.data_x[i] * self.data_y[i]
    
    def run(self):
        self.calculate_xi()
        self.calculate_yi()
        self.calculate_xixi()
        self.calculate_xiyi()

def linear_regression():
    df = obtain_data()
    if df is not None:
        data_x = df["area_sembrada"].tolist()
        data_y = df["area_cosechada"].tolist()
        i = 0
        xi = 0
        yi = 0
        xixi = 0
        xiyi = 0
        threads = []
        while i <= 300:
            thread = my_thread(data_x[i:i+30], data_y[i:i+30])
            threads.append(thread)
            thread.start()
            i += 30
        for thread in threads:
            xi += thread.xi
            yi += thread.yi
            xixi += thread.xixi
            xiyi += thread.xiyi
            thread.join()
        print("xi: ", xi, " yi: ", yi, " xixi: ", xixi, " xiyi: ", xiyi)
        

linear_regression()
        