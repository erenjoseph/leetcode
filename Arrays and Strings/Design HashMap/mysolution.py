class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class MyHashMap:
    size=10000

    def __init__(self):
        self.buckets=[None]*MyHashMap.size
    def hashi(self,key):
        return key%MyHashMap.size

    def put(self, key: int, value: int) -> None:
        index=self.hashi(key)
        if self.buckets[index] is None:
            self.buckets[index]=Node(key,value)
            return
        else:
            current=self.buckets[index]
            while True:
                if current.key==key:
                    current.value=value
                    return
                if current.next is None:
                    current.next=Node(key,value)
                    return
                current=current.next
            

    def get(self, key: int) -> int:
        index=self.hashi(key)
        current=self.buckets[index]
        while current is not None:
            if current.key==key:
                return current.value
            current=current.next
        return -1

    def remove(self, key: int) -> None:
        index=self.hashi(key)
        current=self.buckets[index]
        if current is None:
            return
        if self.buckets[index].key==key:
            self.buckets[index]=self.buckets[index].next
            return
        while current.next is not None:
            if current.next.key==key:
                current.next=current.next.next
                return
            current=current.next
        
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
