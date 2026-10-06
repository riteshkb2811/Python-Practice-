import array
arr1=array.array('i',[1,2,3,4,5 ,6,7,8,9])
print(arr1)
for i in arr1:
    print(id(i))

#Largest number in an array
arr2=array.array('i',[1,4,6,6,3,5,1])
large=0;
for i in arr2:
    if i>large:
        large=i
print(large)


#Second largest number in an array
seclarge=-1
large=0
for i in arr2:
    if i>large and i!=large:
        seclarge=large
        large=i
    elif i>seclarge and i!=large:
        seclarge=i
print(seclarge)


#Second smallest number in an array
arr3=array.array('i',[2,9,1,7,6,8,0])
secsml=0
small=arr3[-1]
for i in arr3:
   if i<small and i!=small:
       secsml=small
       small=i
   elif i<secsml and i!=small:
       secsml=i
print(secsml)

#Check if an array is sorted or not
arr4=array.array('i',[1,2,3,4,5,6,2,3,8,6])
for i in reversed(arr4):
    if i>arr4[-1]:
        print("Array is not sorted")
        break

#Remove duplicates from an array - direct 
arr5=array.array('i',sorted([3,5,7,4,6,8,9,2,4]))
set1=set(arr5)
print(set1)

#Remove duplicates from an array - optimal 
i=0
for k in arr5[1:10]:
    if k!=arr5[i]:
        arr5[i+1]=k
        i+=1
print(arr5[0:i+1])

#Left rotate an array by one place 
temp=arr5[0]
for i in range(1,len(arr5)-1):
    arr5[i-1]=arr5[i]
arr5[len(arr5)-1]=temp
print(arr5)

#linear Search in an array
def linear_search(arr, target):
    for i in arr:
        if i == target:
            print("Element found")
            return 1
    print("Element not found")
    return -1

n = int(input("Enter the number to be searched: "))
linear_search(arr5, n)

# Union and Intersection of two arrays
arr6=array.array('i',[1,2,3,4,5])
arr7=array.array('i',[4,5,6,7,8])
set1=set(arr6)
set1=set1.union(set(arr7))
print("Union of two arrays: ",set1)

#optimal way to find union and intersection of two arrays
arr8=array.array('i',[1,2,3,4,5])
arr9=array.array('i',[4,5,6,7,8])
union=[]
i=0
j=0
while i<len(arr8) and j<len(arr9):
    if arr8[i]<=arr9[j]:
        if(union==[] or union[-1]!=arr8[i]):
         union.append(arr8[i])
        i+=1
    elif arr8[i]>=arr9[j]:
        if(union==[] or union[-1]!=arr9[j]): 
         union.append(arr9[j])
        j+=1
    else:
        union.append(arr8[i])
        i+=1
        j+=1
while j<len(arr9):
    if(union==[] or union[-1]!=arr9[j]):
        union.append(arr9[j])
    j+=1
while i<len(arr8):
    if(union==[] or union[-1]!=arr8[i]):
        union.append(arr8[i])
    i+=1
print(union)



#Intersection of two arrays
intersection=[]
a=0
b=0
while a<len(arr8) and b<len(arr9):
    if arr8[a]<arr9[b]:
        a+=1
    elif arr8[a]>arr9[b]:
        b+=1
    else: 
        intersection.append(arr8[a])
        a+=1
        b+=1
print("Intersection of two arrays: ", intersection)



#Finding the number occuring once in a array 
arr10=array.array('i',[1,1,2,2,3,3,4,4,5])
dict1={}
for i in arr10:
    dict1[i]=dict1.get(i,0)+1

for i, count in dict1.items():
    if count == 1:
        print("The number occuring once is: ", i)
        break

#Finding the number occuring once in a array - optimal using xor
arr11=array.array('i',[1,1,2,2,3,3,4,4,5])
res=0
for i in arr11:
    
    res=res^i
print("The number occuring once is: ", res)