class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0]*self.capacity 
        self.is_ordered = True


    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        return_string = ""
        for index in range(self.size):
            if index == self.size-1:
                return_string += f"{self.arr[index]}"
            else:
                return_string += f"{self.arr[index]}, "
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value,0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index, ordered = False):
        if index >= self.size+1 or index < 0:
            #raise IndexOutOfBounds
            print("lala")
        if not ordered:
            self.is_ordered = False

        if self.size+1 == self.capacity:
            self.resize()
        
        for index in range(self.size,index-1, -1):
            self.arr[index+1] = self.arr[index] 
        self.arr[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value, ordered = False):
        self.insert(value, self.size, ordered)

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index > self.size-1 or index < 0:
            raise IndexOutOfBounds
        self.is_ordered = False
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index > self.size-1 or index < 0:
            raise IndexOutOfBounds
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty
        return self.arr[self.size-1]


    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        new_capacity = self.capacity*2
        new_arr = [0]*new_capacity
        for index in range(self.size):
            new_arr[index] = self.arr[index]

        self.arr = new_arr
        self.capacity = new_capacity
        

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index > self.size-1 or index < 0:
            raise IndexOutOfBounds

        for index in range(index,self.size-1):
            self.arr[index] = self.arr[index+1] 
        self.arr[self.size-1] = 0
            
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.arr = [0]*self.capacity 
        self.size = 0

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if not self.is_ordered:
            raise NotOrdered
        for index in range(self.size):
            if self.arr[index] > value:
                self.insert(value,index,ordered=True) 
                return
        self.append(value,ordered=True)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.is_ordered:
            index = binary_search_recur(self.arr[:self.size],value,0,self.size-1)
        else:
            index = search_recur(self.arr,value,self.size-1)
        
        if index == None:
            raise NotFound
        return index
        

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        try:
            ind = self.find(value)
            self.remove_at(ind)
        except NotFound:
            raise NotFound
        

def search_recur(lis,val,n):
    if n < 0:
        return None
    if lis[n] == val:
        return n
    else:
        return search_recur(lis,val,n-1) 

def binary_search_recur(lis,val,min,max):
    middle = (min+max) // 2
    if min > max:
        return None

    if val == lis[middle]:
        return middle
    elif val > lis[middle]:
        return binary_search_recur(lis,val,middle+1,max)
    else:
        return binary_search_recur(lis,val,min,middle-1)
        

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    # print(str(arr_lis))
    # arr_lis.insert_ordered(1)
    # arr_lis.insert_ordered(19)
    # arr_lis.insert_ordered(4)
    # arr_lis.insert_ordered(8)
    # arr_lis.insert_ordered(17)
    # arr_lis.insert_ordered(19)
    arr_lis.prepend(0)
    arr_lis.append(2)
    arr_lis.append(3)
    arr_lis.append("abc")
    arr_lis.append("lol")
    arr_lis.prepend(2)

    print(str(arr_lis))
    print(arr_lis.find(2))
    
