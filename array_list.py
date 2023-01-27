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
        for ind in range(self.size):
            if ind == self.size-1:
                return_string += f"{self.arr[ind]} "
            else:
                return_string += f"{self.arr[ind]}, "
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value,0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, ind, ordered = False):
        if ind > self.size or ind < 0:
            raise IndexOutOfBounds
        if not ordered:
            self.is_ordered = False

        if self.size+1 == self.capacity:
            self.resize()
        
        for ind in range(self.size,ind-1, -1):
            self.arr[ind+1] = self.arr[ind] 
        self.arr[ind] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value, ordered = False):
        self.insert(value, self.size, ordered)

    #Time complexity: O(1) - constant time
    def set_at(self, value, ind):
        if ind > self.size-1 or ind < 0:
            raise IndexOutOfBounds
        self.is_ordered = False
        self.arr[ind] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, ind):
        if ind > self.size-1 or ind < 0:
            raise IndexOutOfBounds
        return self.arr[ind]

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty
        return self.arr[self.size-1]


    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        new_capacity = self.capacity*2
        new_arr = [0]*new_capacity
        for ind in range(self.size):
            new_arr[ind] = self.arr[ind]

        self.arr = new_arr
        self.capacity = new_capacity
        

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, ind):
        if ind > self.size-1 or ind < 0:
            raise IndexOutOfBounds

        for ind in range(ind,self.size-1):
            self.arr[ind] = self.arr[ind+1] 
        self.arr[self.size-1] = 0
            
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.arr = [0]*self.capacity 
        self.size = 0
        self.is_ordered = True

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if not self.is_ordered:
            raise NotOrdered
        for ind in range(self.size):
            if self.arr[ind] > value:
                self.insert(value,ind,ordered=True) 
                return
        self.append(value,ordered=True)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.is_ordered:
            ind = binary_search_recur(self.arr[:self.size],value,0,self.size-1)
        else:
            for ind in range(self.size):
                if self.arr[ind] == value:
                    ind = ind
                    break
        
        if ind == None:
            raise NotFound
        return ind
        

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        try:
            ind = self.find(value)
            self.remove_at(ind)
        except NotFound:
            raise NotFound
        


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
    print(str(arr_lis))
    arr_lis.insert_ordered(1)
    arr_lis.insert_ordered(19)
    arr_lis.insert_ordered(4)
    arr_lis.insert_ordered(8)
    arr_lis.insert_ordered(17)
    arr_lis.insert_ordered(19)
    print(str(arr_lis))
    print(arr_lis.find(1))

    # import random
    # lis = [44, 28, 41, 93, 34, 83, 52, 85, 34, 74, 65, 78, 43, 10, 39, 13, 76, 33, 44, 21, 29, 16, 91, 95, 82, 96, 38, 73, 26, 86, 23, 23]
    # for ind,x in enumerate(lis):
    #     arr_lis.append(x)
    #     print(f"ind: {ind} of value: {x}")
    # print(str(arr_lis))

    # print(arr_lis.find(21))




    
