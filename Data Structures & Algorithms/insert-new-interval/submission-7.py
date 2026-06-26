class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals) # 5

        temp = []

        for i in range(size):
            interval = intervals[i]

            if interval[1] >= newInterval[0]:
                if interval[0] <= newInterval[0]:
                    temp.append(interval)
                    temp.append(newInterval)
                else:
                    temp.append(newInterval)
                    temp.append(interval)
                break
            
            temp.append(interval)
        else:
            # No overlapping
            temp.append(newInterval)
            return temp
        
        temp.extend(intervals[len(temp) - 1:])
        

        res = [temp[0]]

        # print(temp, res)

        for i in range(1, size + 1):
            current = temp[i]
            last = res[-1]

            print(current, last)

            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                res.append(current)
            
        return res



        
        
