import sys
from collections import namedtuple
Segment = namedtuple('Segment', 'start end') 
#print(Segment)
def optimal_points(segments):
    sortedEnd = sorted(segments, key = lambda x: x[1])
    #print(sortedBeg)
    #print(sortedEnd)

    threshold = -1
    listOfPoints = []
    for i in range(len(sortedEnd) - 1):
        beg, end = sortedEnd[i]
        if beg > threshold:
            listOfPoints.append(end)
            threshold = end
            
    if (listOfPoints[len(listOfPoints) - 1] < sortedEnd[len(sortedEnd) - 1][0]):
        if (sortedEnd):
            listOfPoints.append(sortedEnd[len(sortedEnd) - 1][1])
    print(len(listOfPoints))
    print(*listOfPoints)
    
if __name__ == '__main__':
    #input = sys.stdin.read()
    n, *data = map(int, input().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #segments = sorted(segments,key=lambda x: x[1])
    #print(segments)
    optimal_points(segments) 
