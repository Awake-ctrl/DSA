#User function Template for python3
"""

idea is when we sort the arr then only condition to check is left+mid>right

do with right traversing from reverse directions
left and mid are 0,right-1
if correct add the count 




"""



class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        
        arr.sort()
        
        n=len(arr)
        count=0
        for k in range(n-1,-1,-1):
            
            i,j=0,k-1
            
            while i<j:
                
                if arr[i]+arr[j]>arr[k]:
                    count+=(j-i)
                    j-=1
                    
                else:
                    i+=1
        return count 