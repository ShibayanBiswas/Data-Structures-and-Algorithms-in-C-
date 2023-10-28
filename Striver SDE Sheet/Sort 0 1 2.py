'''

Use any good sorting algorithm like Merge Sort, Quick Sort or inbuilt sorting function of different languages. Sort the Array and 
just return.

Time Complexity : O(N*log(N)), where ‘N’ is the size of the array. We are using inbuilt sort algorithm which has Overall Time Complexity 
O(N*log(N)).

Space Complexity : O(1), As we are using constant space.

'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
	arr.sort()


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())
	if n == 0 :
		return list(), 0
	arr = list(map(int, stdin.readline().strip().split(" ")))
	return arr, n


def printAnswer(arr, n) :
    for i in range(n) :
        print(arr[i],end=" ")
    print()
    
#main
t = int(input().strip())
for i in range(t) :
    arr, n = takeInput()
    sort012(arr, n)
    printAnswer(arr, n)

