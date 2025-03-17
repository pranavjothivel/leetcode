class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda a: a[0])
        merged_intervals = [intervals[0]]
        print(intervals)

        for i in range(1, len(intervals)):
            previous = merged_intervals[-1]
            current = intervals[i]

            if previous[1] >= current[0]:
                previous[1] = max(previous[1], current[1])
            else:
                merged_intervals.append(current)
        return merged_intervals

