#O(n) time and O(n) space
def sunsetViews(buildings, direction):
    candidateBuildings = []

    if direction == "EAST":
        maxValue = 0
        for i in range(len(buildings) -1 , -1, -1):
            if buildings[i] > maxValue:
                maxValue = buildings[i]
                candidateBuildings.append(i)
        return candidateBuildings[::-1]
        
    if direction == "WEST":
        maxValue = 0
        for i in range(len(buildings)):
            if buildings[i] > maxValue:
                maxValue = buildings[i]
                candidateBuildings.append(i)
        return candidateBuildings
