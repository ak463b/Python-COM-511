#Example Case
Matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#Reverse every 2nd row
k=2
#Loop for reversing Matrix
for i in range(0,len(Matrix), k):
    Matrix[i:i+k] = reversed(Matrix[i:i+k])

#Print the result
print("Reversed Matrix")
for row in Matrix:
    print(row)