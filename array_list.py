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
    def insert(self, value, index):
        if self.size == self.capacity:
            self.resize()
        if self.size < index:
            raise IndexOutOfBounds
        for index in range(self.size,index-1, -1):
            self.arr[index+1] = self.arr[index] 
        self.arr[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if self.size < index:
            raise IndexOutOfBounds
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.size < index:
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
        if self.size-1 < index or self.size == 0:
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
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.size == 0:
            raise Empty

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    # print(str(arr_lis))
    arr_lis.prepend(4)
    arr_lis.append(1)
    arr_lis.insert(10,1)
    arr_lis.append(12)
    print(str(arr_lis))
    arr_lis.remove_at(1)
    print(str(arr_lis))
