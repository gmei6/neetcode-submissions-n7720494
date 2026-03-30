class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = list(zip(position, speed))
        combined.sort()
        
        fleets = 1

        #car_leader = combined[-1]
        car_leader_time = (target-combined[-1][0])/combined[-1][1]

        for i in range(len(combined)-2, -1, -1):
            # calculate the time for each car
            
            car_i_time = (target - combined[i][0])/combined[i][1]
            #print("Leader time: ", car_leader_time, "other time: ", car_i_time)

            if car_leader_time < car_i_time:
                fleets += 1
                #car_leader = combined[i]
                car_leader_time = car_i_time
        
        #if car_leader == combined[0]:
        #    fleets += 1
        return fleets
                