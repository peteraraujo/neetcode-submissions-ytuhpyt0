class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        size = len(days)

        cache = {} # (day) : minn

        
        def bs(day):
            l, r = 0, size - 1

            while l <= r:
                m = (l + r) // 2

                if days[m] == day:
                    return day
                
                if days[m] < day:
                    l = m + 1

                else:
                    r = m - 1
            
            
            if l == size:
                return -1
            else:
                return days[l]

        
        def dfs(day=days[0]):

            if day == -1:
                return 0
            
            query = day

            if query in cache:
                return cache[query]

            # 1-day pass
            oneDay = costs[0] + dfs(bs(day + 1))

            # 7-day pass
            sevenDays = costs[1] + dfs(bs(day + 7))   
            
            # 30-day pass
            thirtyDays = costs[2] + dfs(bs(day + 30))

            minn = min(oneDay, sevenDays, thirtyDays)

            cache[query] = minn

            return minn
        

        return dfs()