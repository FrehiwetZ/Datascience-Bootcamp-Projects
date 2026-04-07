class StatEngine:
    def __init__(self,data):
        if not data:
            raise ValueError("Data cannot be empty")
        
        cleaned=[]
        for x in data:
            if isinstance(x,(int, float)):
                cleaned.append(x)
            else:
                raise TypeError(f"Invalid data type: {x}")
            
        self.data=cleaned
        self.n = len(cleaned)

    def get_mean(self):
        return sum(self.data) / self.n
    
    def get_median(self):
        sorted_data = sorted(self.data)
        mid = self.n // 2
        if self.n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
        
    