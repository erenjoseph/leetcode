from collections import defaultdict

class TimeMap:
    def __init__(self):
        # defaultdict prevents KeyErrors if a key doesn't exist yet
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Appending keeps it sorted because timestamps naturally increase
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # Safe fetch: grab the list, or an empty list if it doesn't exist
        arr = self.dic.get(key, [])
        
        left, right = 0, len(arr) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid][0] == timestamp:
                # Exact match found
                return arr[mid][1]
                
            elif arr[mid][0] < timestamp:
                # Valid past timestamp found! Save it, but keep searching right
                res = arr[mid][1]
                left = mid + 1
                
            else:
                # Invalid future timestamp. Search left.
                right = mid - 1
                
        return res
