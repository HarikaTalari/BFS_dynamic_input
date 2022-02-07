class Bfs:
    def __init__(self):
        self.queue = []

    def bfs_using_queue(self, root):
        self.queue.append(root)
        root_child = int(input(f"Enter the number of child nodes for {root}: "))
        self.bfs_recursion(root_child)

    def bfs_recursion(self, root_child):
        list_of = list(map(str, input("Enter the children: ").split()))
        self.queue.append(" ".join(list_of))
        for i in range(root_child):
            value = int(input(f"Enter the number of children for {list_of[i]}: "))
            if value == 0:
                i += 1
            else:
                self.bfs_recursion(value)

    def display(self):
        for element in range(0, len(self.queue)):
            print(self.queue[element], end=" ")


bfs = Bfs()
bfs.bfs_using_queue(input("Enter the root node: "))
bfs.display()
