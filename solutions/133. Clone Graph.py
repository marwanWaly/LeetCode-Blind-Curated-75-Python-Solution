if not node:
            return None

        visited = {}
        stack = [node]
        while stack:
            n = stack.pop()
            if n not in visited:
                visited[n] = Node(n.val)

            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    stack.append(nei)

                visited[n].neighbors.append(visited[nei])
                
        return visited[node]
