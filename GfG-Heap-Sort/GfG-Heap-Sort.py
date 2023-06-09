class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        largest = i
        left = 2 * i + 1  # Left child position
        right = 2 * i + 2  # Right child position
    
        # Check if left child of root exists and is greater than the root
        if left < n and arr[i] < arr[left]:
            largest = left
    
        # Check if right child of root exists and is greater than the largest so far
        if right < n and arr[largest] < arr[right]:
            largest = right
    
        # Swap the root with the largest element if necessary
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            self.heapify(arr, n, largest)

    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        n = len(arr)

        # Build a max heap starting from the last non-leaf node
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        n = len(arr)
    
        # Extract elements one by one from the heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            self.heapify(arr, i, 0)
