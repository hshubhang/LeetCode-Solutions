class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i])for i in range(len(position))]
        cars.sort(reverse = True)
        print(cars)
        pos, spd = cars[0]
        first_car_time = (target - pos) / spd
        carstack = [first_car_time]
        for pos, speed in cars[1:]:
            time = (target - pos) / speed
            if time > carstack[-1]:
                carstack.append(time)
                print(carstack)
            else:
                pass
        return len(carstack)

