class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class MyHashSet:
    size=1000
    def hashi(self,val):
        return val%MyHashSet.size


    def __init__(self):
        self.buckets=[None]*MyHashSet.size


    def add(self, key: int) -> None:
        index=self.hashi(key)
        if self.buckets[index] is None:
            self.buckets[index]=Node(key)
        else:
            current=self.buckets[index]
            if current.value==key:
                return
            while current.next is not None:
                if current.next.value==key:
                    return
                current=current.next
            current.next=Node(key)



    def remove(self, key: int) -> None:
        index=self.hashi(key)
        if self.buckets[index] is None:
            return
        if self.buckets[index].value==key:
            self.buckets[index]=self.buckets[index].next
            return
        current=self.buckets[index]
        while current.next is not None:
            if current.next.value==key:
                current.next=current.next.next
                return
            current=current.next
        


        

    def contains(self, key: int) -> bool:
        index=self.hashi(key)
        current=self.buckets[index]
        while current is not None:
            if current.value==key:
                return True
            current=current.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
