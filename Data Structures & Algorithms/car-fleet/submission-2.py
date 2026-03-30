class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        combined = list(zip(position, speed))
        combined.sort()

        # Calculate the time for the car closest to target
        # This is our initial "bottleneck"
        last_pos, last_speed = combined[-1]
        current_bottleneck = (target - last_pos) / last_speed
        
        fleets = 1  # We always have at least the first fleet

        # Loop backwards starting from the second to last car
        for i in range(len(combined) - 2, -1, -1):
            pos, spd = combined[i]
            arrival_time = (target - pos) / spd

            # If this car is SLOWER (takes more time) than the bottleneck,
            # it becomes the new bottleneck for any cars behind it.
            if arrival_time > current_bottleneck:
                fleets += 1
                current_bottleneck = arrival_time
            
            # If arrival_time <= current_bottleneck:
            # It catches up. We do nothing. It merges.

        return fleets