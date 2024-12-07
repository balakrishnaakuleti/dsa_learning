class Solution:

    def print_mat(self,mat):
        for row in mat:
            print(row)
    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, mat):
        time_to_rot = 0
        iteration_needed = self.iteration_needed(mat)
        while iteration_needed:
            # Rotten the near by oranges
            rows_count = len(mat)
            col_count = len(mat[0])
            any_updates = False
            to_rotten_list =[]
            for i in range(rows_count):
                for j in range(col_count):
                    # Check if rotten orange
                    if mat[i][j] == 2:
                        # Rotten top orange
                        if i-1>-1:
                            if mat[i-1][j] == 1:
                                to_rotten_list.append((i-1,j))
                        #Rotten bot orange
                        if i+1<rows_count:
                            if mat[i+1][j] == 1:
                                to_rotten_list.append((i+1,j))
                        #Rotten left orange
                        if j-1>-1:
                            if mat[i][j-1] == 1:
                                to_rotten_list.append((i,j-1))
                        #Rotten right orange
                        if j+1<col_count:
                            if mat[i][j+1] == 1:
                                to_rotten_list.append((i,j+1))
            #Updates at once
            for i,j in to_rotten_list:
                mat[i][j] = 2
            iteration_needed = self.iteration_needed(mat)
            # Consider the iteration if any oranges are rottened
            if iteration_needed:
                # Rotting was not possible
                if len(to_rotten_list) == 0:
                    return -1

                time_to_rot +=1
            else:
                time_to_rot+=1
                return time_to_rot

        return time_to_rot

    def iteration_needed(self, mat):
        for row in mat:
            for item in row:
                if item == 1:
                    return True
        return False
#{ 
 # Driver Code Starts
from queue import Queue

mat = [[2, 1, 0], [1, 1, 0], [0, 1, 1]]
obj = Solution()
ans = obj.orangesRotting(mat)
print(ans)
print("~")

# } Driver Code Ends