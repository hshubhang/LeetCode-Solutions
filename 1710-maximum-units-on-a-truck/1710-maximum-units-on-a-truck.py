class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        boxTypes.sort(key=lambda x: x[1], reverse = True)


        for boxes, units in boxTypes:

            if boxes < truckSize:
                count += boxes * units
                truckSize -= boxes

            elif boxes >= truckSize:

                count += truckSize * units

                break

            if truckSize == 0:
                break

        
        return count

        

            
