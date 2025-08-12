class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        
        def sort_key(log):
            identifier, content = log.split(" ", 1)
            return (content, identifier)

        for log in logs:
            iden, content = log.split(" ", 1)
            if content[0].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter.sort(key=sort_key)

        return letter + digit


    

        

        