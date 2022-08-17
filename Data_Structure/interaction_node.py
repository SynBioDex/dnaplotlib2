class InteractionNode:


    def __init__(self, interaction_node_type, so_term, name):
        self.interaction_node_type = interaction_node_type
        self.so_term = so_term
        self.name = name
        self.inter_node_dict = {}

    def node_dict(self):
        self.inter_node_dict['interaction_node_type'] = self.interaction_node_type
        self.inter_node_dict['so_term'] = self.so_term
        self.inter_node_dict['name'] = self.name
        return self.inter_node_dict

    def print_node(self):
        print(self.node_dict)

	
node1 = InteractionNode('dissociation', 'SO:1858478', 'First Interaction Node')
node1.node_dict()