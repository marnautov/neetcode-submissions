class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  
        fleets = 0
        max_time = -1.0
        for pos, sp in cars:
            t = (target - pos) / sp
            if t > max_time:
                fleets += 1
                max_time = t
        return fleets