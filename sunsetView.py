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

def sunsetViews2(buildings, direction):
    candidateBuildings = []
    maxValue = 0
    
    for i in range(len(buildings) -1 , -1, -1) if direction == "EAST" else range(len(buildings)):
        if buildings[i] > maxValue:
                maxValue = buildings[i]
                candidateBuildings.append(i)
    
    return candidateBuildings[::-1] if direction == "EAST" else candidateBuildings
    
def test_east_sunsetView():
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"
        expected = [1, 3, 6, 7]
        actual = sunsetViews(buildings, direction)
        assert(actual == expected)

def test_east_sunsetView2():
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "EAST"
        expected = [1, 3, 6, 7]
        actual = sunsetViews2(buildings, direction)
        assert(actual == expected)

def test_west_sunsetView():
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "WEST"
        expected = [0, 1]
        actual = sunsetViews(buildings, direction)
        assert(actual == expected)

def test_west_sunsetView2():
        buildings = [3, 5, 4, 4, 3, 1, 3, 2]
        direction = "WEST"
        expected = [0, 1]
        actual = sunsetViews2(buildings, direction)
        assert(actual == expected)