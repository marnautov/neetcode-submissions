class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        max_time = 0

        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd

            if time > max_time:
                fleets += 1
                max_time = time

        return fleets



        