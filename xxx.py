#!/usr/bin/python3
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
     
    def change_data(self, index, n):
        self.nums[index] = n        	

data_one = Data()
data_one.nums[0] = 100
data_one.nums[1] = 100
data_one.nums[2] = 100
data_one.nums[3] = 100
data_one.nums[4] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(3, 100)
print(data_two.nums)
