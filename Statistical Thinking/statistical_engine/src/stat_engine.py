import math

class StatEngine:
    # For error handling and data cleaning
    def __init__(self, data):
        if not data:
            raise ValueError("Data cannot be empty")
        
        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(x)
            else:
                raise TypeError(f"Invalid data type: {x}")
            
        self.data = cleaned
        self.n = len(cleaned)

    # Central tendency
    def get_mean(self):
        return sum(self.data) / self.n

    def get_median(self):
        sorted_data = sorted(self.data)
        mid = self.n // 2
        if self.n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2 #Bessel's correction
        else:
            return sorted_data[mid]

    def get_mode(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1

        max_freq = max(freq.values())
        if max_freq == 1:
            return "No mode"
        
        modes = [k for k, v in freq.items() if v == max_freq]
        return modes

    # Dispersion
    def get_variance(self, is_sample=False):
        
        mean = self.get_mean()
        sum_squared_diff = sum((x - mean) ** 2 for x in self.data)
        if is_sample:
            return sum_squared_diff / (self.n - 1)
        else:
            return sum_squared_diff / self.n

    def get_standard_deviation(self, is_sample=False):
        
        return math.sqrt(self.get_variance(is_sample))

    # Outliers
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()
        outliers = []
        for x in self.data:
            z_score = abs((x - mean) / std)
            if z_score > threshold:
                outliers.append(x)
        return outliers