#O(n) time and #O(n) space
def mergeOverLappingIntervals(intervals):
    #Sort based of starting value
    intervals.sort(key=lambda i:i[0])
    mergedIntervals = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = mergedIntervals[-1][1]

        #If intervals  overlap add to update the lastEnd
        if lastEnd >= start:
            mergedIntervals[-1][1] = max(end, lastEnd)
        else:
            mergedIntervals.append([start,end])

    return mergedIntervals

def mergeOverlappingIntervals2(intervals):
    intervals.sort(key=lambda i:i[0])
    mergedInterval = [intervals[0]]
    
    for start, end in intervals[1:]:
        lastEnd = mergedInterval[-1][1]

        #If intervals  don't overlap add to mergedInterval
        if start > lastEnd:
            mergedInterval.append([start,end])
        else:
            mergedInterval[-1][1] = max(end, lastEnd)
    return mergedInterval
        

def test_mergeOverLappingIntervals():
    intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    expected = [[1, 2], [3, 8], [9, 10]]
    actual = mergeOverLappingIntervals(intervals)
    assert(actual == expected)