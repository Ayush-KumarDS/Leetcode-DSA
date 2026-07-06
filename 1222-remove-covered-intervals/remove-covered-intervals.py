class Solution(object):
    def removeCoveredIntervals(self, intervals):
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_end = 0
        
        for interval in intervals:
            # If the current end fits inside max_end, it is covered
            if interval[1] <= max_end:
                continue
            else:
                # It is a unique interval
                count += 1
                max_end = interval[1]
                
        return count
