class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)
        prev_distance = float('-inf')
        fleets = 0
        for pos, spd in cars:
            distance = (target - pos) / spd
            if distance > prev_distance:
                fleets +=1
                prev_distance = distance
        return fleets
