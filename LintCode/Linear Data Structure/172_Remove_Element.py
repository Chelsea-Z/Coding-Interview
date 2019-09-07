class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        if len(A) > 0:
            j = len(A)-1
            for i in range(len(A)):
                if A[i] == elem:
                    while A[j] == elem and j>=0:
                        j -= 1 
                    if i>=j:
                        break
                    else:
                        A[i] = A[j]
                        j -= 1 
                

            return j+1 
            
        else:
            return 0