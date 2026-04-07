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
# for the centeral tendency 
    def get_mean(self):
        return sum(self.data) / self.n
    
    def get_median(self):
        sorted_data = sorted(self.data)
        mid = self.n // 2
        if self.n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
        
    def get_mode(self):
        freq = {}
        for x in self.data:
            freq[x] =freq.get(x, 0) + 1

        max_freq = max(freq.values())

        if max_freq == 1:
            return "No mode "
        
        modes = [k for k, v in freq.items() if v == max_freq]
        return modes
    