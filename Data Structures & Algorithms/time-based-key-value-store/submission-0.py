class TimeMap:

    def __init__(self):
        self.map = {}       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key][0].append(value)
            self.map[key][1].append(timestamp)
        else:
            self.map[key] = [[value],[timestamp]]
    def bin_search(self,arr,time_stamp):
        idx = -1
        left = 0
        right = len(arr) - 1

        while left <= right :
            mid = (left + right)//2
            if arr[mid] == time_stamp:
                return mid
            elif arr[mid] > time_stamp:
                right = mid - 1
            else:
                idx = mid
                left = mid+1
        return idx
         
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        time_s = self.map[key][1]
        emotion = self.map[key][0]

        idx = self.bin_search(time_s,timestamp)

        if idx == -1:
            return ""
        else:
            return emotion[idx]

        
