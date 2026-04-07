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

        