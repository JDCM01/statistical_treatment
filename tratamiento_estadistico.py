import threading

#mean = suma de los datos / numero de datos
#median = dato del medio
#mode = dato que mas se repite

class my_thread(threading.Thread):
    def __init__(self, data: list, frequency: dict = {}):
        super(my_thread, self).__init__()
        self.data = data
        self.result = 0
        self.frequency = frequency

    def adder(self):
        result = 0
        for i in self.data:
            result += i
        self.result = result
    
    def mode(self):
        for item in self.data:
            if item in self.frequency:
                self.frequency[item] += 1
            else:
                self.frequency[item] = 1
        self.statistical_mode = max(self.frequency, key=self.frequency.get)

    def run(self):
        self.adder()
        self.mode()
        
def median(data: list):
    data.sort()
    if len(data) % 2 == 1:
        return data[len(data) // 2]
    else:
        return (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
    
if __name__ == "__main__":
    threads = []
        
    for t in threads:
        t.join()
        
def main():
    data = [1, 2, 2, 3, 4, 5, 5, 5, 1, 2, 3, 4, 5, 3, 3, 4, 5, 2, 1, 4]
    ordered_data = sorted(data)
    number_of_data = len(data)
    number_of_threads = 10
    load_per_thread = number_of_data // number_of_threads
    i = 0
    j = 0
    threads = []
    mode_count = {}
    while j < number_of_threads:
        t = my_thread(ordered_data[i:i + load_per_thread], mode_count)
        threads.append(t)
        t.start()
        mode_count = t.frequency
        i += load_per_thread
        j += 1
        
    statistical_median = median(data)
    
    for t in threads:
        t.join()
        
    total_sum = 0
        
    for t in threads:
        total_sum += t.result
    
    if t.statistical_mode in mode_count:
        mode_count[t.statistical_mode] += 1
    else:
        mode_count[t.statistical_mode] = 1
    
    mean = total_sum / number_of_data
    statistical_mode = max(mode_count, key=mode_count.get)
    print(f"Mean: {mean}")
    print(f"Median: {statistical_median}")
    print(f"Mode: {statistical_mode}")

main()