class Solution:
    def simplifyPath(self, path: str) -> str:
        folder_stack = []
        split_path = path.split("/")
        for i in split_path:
            if i == ".." and folder_stack:
                folder_stack.pop()
            if i == "" or i == ".":
                continue
            folder_stack.append(i)
            if i == "..":
                folder_stack.pop()

        return "/" + "/".join(folder_stack)
            
            
        
        
