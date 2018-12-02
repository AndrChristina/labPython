class Parni_el:
    def __init__(self, data):
        self._data = data           
        self._len = len(data)
        self._start = self._len % 2

    def __iter__(self):
        return self

    def __next__(self):
        if self._start == 0:        
            raise StopIteration     
        self._start = self._start - 1
        return self._data[self._start]


data = Parni_el([1, 2, 3, 4, 5])

for i in data:
    print(i)
 
