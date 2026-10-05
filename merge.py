'''
Given a list of [start, end] intervals, merge all overlapping ones.
'''

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key = lambda x: x[0])
    result = [intervals[0][:]]
    
    for start, end in intervals[1:]:
        last = result[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            result.append([start, end])

    return result
    
    
    
        


assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert merge([[1,4],[4,5]]) == [[1,5]]