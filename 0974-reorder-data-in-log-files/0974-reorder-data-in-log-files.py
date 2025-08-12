class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []

        for log in logs:
            iden, content = log.split(" ", 1)
            if content[0].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        
        letter.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))

        return letter + digit


    

        

        