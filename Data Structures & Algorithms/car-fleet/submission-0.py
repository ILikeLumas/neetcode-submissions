class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for s, p in zip(speed, position):
            time = (target - p) / s
            cars.append((p,time))
        
        cars.sort(reverse = True)

        fleets = 0
        fleetTimes = 0

        for p, time in cars:
            if time > fleetTimes:
                fleets += 1
                fleetTimes = time
        

        return fleets


