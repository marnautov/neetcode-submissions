class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)
        prev_time = float('-inf')
        fleets = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prev_time:
                fleets +=1
                prev_time = time
        return fleets
