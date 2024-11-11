class Solution:
    def simplifyPath(self, path: str) -> str:
        folder_stack = []
        split_path = path.split("/")
        print(split_path)
        for i in split_path:
            if i =="..":
                if folder_stack:
                    folder_stack.pop()
            elif i == "." or not i:
                continue
            else:
                folder_stack.append(i)
            
        new_path = "/" + "/".join(folder_stack)
        return new_path
