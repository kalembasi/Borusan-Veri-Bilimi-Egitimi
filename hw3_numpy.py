#1
import numpy as np

#2
b = np.arange(6)

#3
np.zeros((4,5))

#4
np.full((3,5),7)

#5
np.arange(10,71, 5)

#6
np.linspace(10,20,15)

#7
np.random.rand(3,5) #reel numbers
np.random.randint(low=0, high=100, size=(3,5)) #integers

#8
np.eye(5)

#9
arr = np.arange(0,24)
arr.reshape(4,6)

#10
arr2 = np.random.uniform(low=0, high=1, size=10)
arr2.max() #max
arr2.min() #min

#11
arr3 = np.random.rand(6,6)

#12
arr3[4]

#13
arr3[5,5]

#14
arr3[:,5]

#15
for i in range(np.size(arr3)):
    print(arr3.flat[0:i])

#16
arr4 = np.arange(0,1, 0.1).reshape(2,5)
arr4 *=5

#17
arr4.sum()

#18
arr4.std()

#19
arr4.var()

#10
arr4.transpose()