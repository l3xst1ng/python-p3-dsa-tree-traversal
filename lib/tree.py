class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if self.root is None:
            return None

        # List to store the nodes to visit
        nodes_to_visit = [self.root]

        # Traversing the tree
        while nodes_to_visit:
            # Get the next node to visit
            node = nodes_to_visit.pop(0)

            # Checking if the node's ID matches the desired ID
            if node['id'] == id:
                return node

            # Adding the node's children to the list of nodes to visit
            nodes_to_visit.extend(node['children'])

        # Returning None if the desired node isn't found
        return None