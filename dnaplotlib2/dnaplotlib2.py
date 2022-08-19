class BioDesign:
    '''
    
    '''

    def __init__(self, name):
        self.name = name
        self.backbone = []
        self.molecular_species = []
        self.interaction_node = []
        self.interaction = []


    def add_backbone(self, backbone):
        self.backbone.append(backbone)
        
    def print_backbone(self):
        print(self.backbone)

    def return_backbone(self):
        return self.backbone


    def add_moleculer(self, moleculer):
        self.molecular_species.append(moleculer)   

    def print_moleculer(self):
        print(self.molecular_species)
        
    def return_moleculer(self):
        return self.molecular_species


    def add_interaction_node(self, node):
        self.interaction_node.append(node)

    def print_node(self):
        print(self.interaction_node)
        
    def return_node(self):
        return self.interaction_node

    
    def add_interaction(self, interaction):
        self.interaction.append(interaction)

    def print_interaction(self):
        print(self.interaction)

    def return_interaction(self):
        return self.interaction
    

    def print_biodesign(self):
        print(f"Name of BioDesign is -> {self.name}","\n\n",
            f"Backbones are -> {self.return_backbone()}\n\n",
            f"Species are -> {self.return_moleculer()}\n\n",
            f"Nodes are -> {self.return_node()}\n\n",
            f"Interactions are -> {self.return_interaction()}")

class Backbone:
    '''
    list of dict 
    parts as dict collected in a list with order of appending
    '''

    def __init__(self,name = "Backbone Init"):
        self.name = name
        self.backbone = []

    def append_part(self, part):
        '''
        
        '''
        self.backbone.append(part) 

    def return_backbone(self):
        return_list = [self.name, self.backbone]
        return return_list

    def print_backbone(self):
        '''
        
        '''
        print(self.backbone)

class Part:
    '''
    
    
    '''
    def __init__(self, part_type, orientation, so_term, name):
        self.part_type = part_type
        self.orientation = orientation
        self.so_term = so_term
        self.name = name
        self.part_list = []
        self.part_dict = {}
    
    def part_li(self):
        '''
        Parameters: 
        part_type -> string
        orientation -> num (should be forward or backward (
            from enum import Enum

            class Orientation(Enum):
                FORWARD = 1
                REVERSE = 2))    

        so_term -> ontology
        name -> string    
        
        '''
        self.part_list.append(self.part_type)
        self.part_list.append(self.orientation)
        self.part_list.append(self.so_term)
        self.part_list.append(self.name)
        # print(self.part_list)

        return self.part_list
    
    def part_di(self):
        '''
        
        Parameters: 
        part_type -> string
        orientation -> num (should be forward or backward (
            from enum import Enum

            class Orientation(Enum):
                FORWARD = 1
                REVERSE = 2))    

        so_term -> ontology
        name -> string  
        '''
        self.part_dict['part_type'] = self.part_type
        self.part_dict['orientation'] = self.orientation
        self.part_dict['so_term'] = self.so_term
        self.part_dict['name'] = self.name
        # print(self.part_dict)
        
        return self.part_dict

class MolecularSpecies:


    def __init__(self,molecular_species_type, so_term, name):
        self.molecular_species_type = molecular_species_type
        self.so_term = so_term
        self.name = name
        self.species = {}
        
    def molec_spec_append(self):
        self.species['molecular_species_type'] = self.molecular_species_type
        self.species['so_term'] = self.so_term
        self.species['name'] = self.name
        return self.species
    
    def print_spec(self):
        print(self.species)

class Interaction:


    def __init__(self, interaction_type, start_object, end_object, name):
        self.interaction_type = interaction_type
        self.start_object = start_object
        self.end_object = end_object
        self.name = name
        self.interaction_dict = {}

        
    def interaction_append(self):
        self.interaction_dict['interaction_type'] = self.interaction_type
        self.interaction_dict['start_object'] = self.start_object
        self.interaction_dict['end_object'] = self.end_object
        self.interaction_dict['name'] = self.name
        return self.interaction_dict

    def print_interaction(self):
        print(self.interaction_dict)

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

