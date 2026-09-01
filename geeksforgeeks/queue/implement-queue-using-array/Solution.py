class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.limit = n
        self.queue = []

    
    def isEmpty(self):
        # Check if queue is empty
        return len(self.queue) == 0

    
    def isFull(self):
        # Check if queue is full
        return len(self.queue) >= self.limit

    
    def enqueue(self, x):
        # Enqueue
        if( len(self.queue) >= self.limit ):
            return False
        self.queue.append(x)
        return True

    
    def dequeue(self):
        # Dequeue
        if(len(self.queue) <= 0):
            return -1
        
        return self.queue.remove(self.queue[0])

    
    def getFront(self):
        # Get front element
        if( len(self.queue) <= 0 ): return -1
        return self.queue[0]
       
    
    def getRear(self):
        # Get rear element 
        if( len(self.queue) <= 0 ): return -1
        return self.queue[-1]
        