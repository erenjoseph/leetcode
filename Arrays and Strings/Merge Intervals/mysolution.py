class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        ans=[]
        for i in range(len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i+1][0]=intervals[i][0]
                intervals[i+1][1]=max(intervals[i][1],intervals[i+1][1])
            else:
                ans.append(intervals[i])
        ans.append(intervals[-1])       
        return ans
