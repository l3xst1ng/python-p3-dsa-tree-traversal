class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if self.root is None:
            return None

        # Create a list to store the nodes to visit
        nodes_to_visit = [self.root]

        # Traverse the tree
        while nodes_to_visit:
            # Get the next node to visit
            node = nodes_to_visit.pop(0)

            # Check if the node's ID matches the desired ID
            if node['id'] == id:
                return node

            # Add the node's children to the list of nodes to visit
            nodes_to_visit.extend(node['children'])

        # If the desired node is not found, return None
        return None