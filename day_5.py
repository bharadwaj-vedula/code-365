"""
Day - 5
Write a program to print the first ‘n’ layers of the pascal triangle.
Sample input - 4
sample output - 
1
1 1 
1 2 1
1 3 3 1
1 4 6 4 1

"""

start = 11

n = int(input())

for i in range(1,n+1):
    temp = start**i
    print(temp)
