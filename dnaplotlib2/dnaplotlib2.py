class BioDesign:
    '''
    Class for collecting and printting all Bio Design components like Backbones, Molecular Species 
    and Interactions
    '''
    
    def __init__(self, name):
        self.name = name
        self.backbone = []
        self.molecular_species = []
        self.interaction_node = []
        self.interaction = []
        self.biodesign_output = []

    def __repr__(self):
        '''return a string representation of the object'''
        self.biodesign_output = [
            self.name,
            self.return_backbone(),
            self.return_moleculer(),
            self.return_node(),
            self.return_interaction(),]

        return self.biodesign_output

    def add_backbone(self, backbone):
        '''
        function to append backbones to a list in a biodesign
        '''
        self.backbone.append(backbone)

    def print_backbone(self):
        '''
        function to print to a list of available backbones
        '''
        print(self.backbone)

    def return_backbone(self):
        '''
        function to return alist of available backbones
        '''
        return self.backbone

    def add_moleculer(self, moleculer):
        '''
        function to add new molecule to the biodesign
        '''
        self.molecular_species.append(moleculer)

    def print_moleculer(self):
        '''
        function to print all melocules added to the biodesign
        '''
        print(self.molecular_species)

    def return_moleculer(self):
        '''
        function to return a list of available molecules
        '''
        return self.molecular_species

    def add_interaction_node(self, node):
        '''
        function to append new interaction node to the biodesign
        '''
        self.interaction_node.append(node)

    def print_node(self):
        '''
        funciton to print available list of interaction nodes
        '''
        print(self.interaction_node)

    def return_node(self):
        '''
        function to return list of available nodes
        '''
        return self.interaction_node

    def add_interaction(self, interaction):
        '''
        function to append new interaction to the biodesign
        '''
        self.interaction.append(interaction)

    def print_interaction(self):
        '''
        function to print a list of available interactions
        '''
        print(self.interaction)

    def return_interaction(self):
        '''
        function to return a list of available interaction in the biodesign
        '''
        return self.interaction

        # def return_biodesign(self):
        #     self.biodesign_output = [f"Name of BioDesign is -> {self.name}","\n\n",
        #         f"Backbones are -> {self.return_backbone()}\n\n",
        #         f"Species are -> {self.return_moleculer()}\n\n",
        #         f"Nodes are -> {self.return_node()}\n\n",
        #         f"Interactions are -> {self.return_interaction()}"]
        #     return self.biodesign_output

        # def return_biodesign(self):
        #     '''
        #     function to return current biodesign
        #     '''
        #     # self.biodesign_output = [
            #     self.name,
            #     self.return_backbone(),
            #     self.return_moleculer(),
            #     self.return_node(),
            #     self.return_interaction(),
            # ]
            # return self.biodesign_output



    def print_biodesign(self):
        '''
        function to print all biodesign components
        '''
        print(
            f"Name of BioDesign is -> {self.name}",
            "\n\n",
            f"Backbones are -> {self.return_backbone()}\n\n",
            f"Species are -> {self.return_moleculer()}\n\n",
            f"Nodes are -> {self.return_node()}\n\n",
            f"Interactions are -> {self.return_interaction()}",)


class Backbone:
    '''
    class to create backbone through adding different parts
    output:  list of dict of added parts
    '''

    def __init__(self, name="Backbone Init"):
        self.name = name
        self.backbone = []
        self.backbone_list = []

    def __repr__(self):
        '''return a string representation of the object'''
        self.backbone_list = [self.name, self.backbone]
        return f'(Backbone object contains {self.backbone_list})'

    def append_part(self, part):
        '''
        function to append new part to the backbone
        '''
        self.backbone.append(part)
        
    
    # def return_backbone(self):
    #     '''
    #     function to return current backbone as a list of all parts appended
    #     '''
    #     return_list = [self.name, self.backbone]
    #     return return_list

    def print_backbone(self):
        """ 
        function to print current backbone parts
        """
        print(self.backbone)


class Part:
    """ 
    class to create a new part with all components of it
    """

    def __init__(self, part_type, orientation, so_term, name):
        self.part_type = part_type
        self.orientation = orientation
        self.so_term = so_term
        self.name = name
        self.part_list = []
        self.part_dict = {}

    def part_li(self):
        """ 
        function to return a list contains part components

        Parameters:
        part_type -> string
        orientation -> num (should be forward or backward (
            from enum import Enum

            class Orientation(Enum):
                FORWARD = 1
                REVERSE = 2))

        so_term -> ontology
        name -> string

        """
        self.part_list.append(self.part_type)
        self.part_list.append(self.orientation)
        self.part_list.append(self.so_term)
        self.part_list.append(self.name)
        # print(self.part_list)

        return self.part_list

    def part_di(self):
        """
        function to return to dictionary of part components

        Parameters:
        part_type -> string
        orientation -> num (should be forward or backward (
            from enum import Enum

            class Orientation(Enum):
                FORWARD = 1
                REVERSE = 2))

        so_term -> ontology
        name -> string
        """
        self.part_dict["part_type"] = self.part_type
        self.part_dict["orientation"] = self.orientation
        self.part_dict["so_term"] = self.so_term
        self.part_dict["name"] = self.name
        # print(self.part_dict)

        return self.part_dict


class MolecularSpecies:
    '''
    class to create a new molecular species
    '''

    def __init__(self, molecular_species_type, so_term, name):
        self.molecular_species_type = molecular_species_type
        self.so_term = so_term
        self.name = name
        self.species = {}

    def __repr__(self):
        '''return a string representation of the object'''
        return f'(Molecule object contains {self.species})'


    def molec_spec_append(self):
        '''
        function to add new molecule to a list of all molecules
        '''
        self.species["molecular_species_type"] = self.molecular_species_type
        self.species["so_term"] = self.so_term
        self.species["name"] = self.name
        # return self.species

    def print_spec(self):
        '''
        function to print a list of all available molecules
        '''
        print(self.species)


class Interaction:
    '''
    class to create new interaction between parts, molecules or nodes
    '''
    
    def __init__(self, interaction_type, start_object, end_object, name):
        self.interaction_type = interaction_type
        self.start_object = start_object
        self.end_object = end_object
        self.name = name
        self.interaction_dict = {}

    def __repr__(self):
        '''return a string representation of the object'''
        return f'(Interaction object contains {self.interaction_dict})'


    def interaction_append(self):
        '''
        function to append new interaction to the interaction list
        '''

        self.interaction_dict["interaction_type"] = self.interaction_type
        self.interaction_dict["start_object"] = self.start_object
        self.interaction_dict["end_object"] = self.end_object
        self.interaction_dict["name"] = self.name
        # return self.interaction_dict

    def print_interaction(self):
        '''
        function to print a list of all interactions
        '''

        print(self.interaction_dict)


class InteractionNode:
    '''
    class to create new list of interaction nodes 
    '''

    def __init__(self, interaction_node_type, so_term, name):
        self.interaction_node_type = interaction_node_type
        self.so_term = so_term
        self.name = name
        self.inter_node_dict = {}

    def __repr__(self):
        '''return a string representation of the object'''
        return f'(Node object contains {self.inter_node_dict})'


    def node_dict(self):
        '''
        function to create a dictionary of interaction node components
        '''

        self.inter_node_dict["interaction_node_type"] = self.interaction_node_type
        self.inter_node_dict["so_term"] = self.so_term
        self.inter_node_dict["name"] = self.name
        # return self.inter_node_dict

    def print_node(self):
        '''
        function to print list of interaction nodes
        '''
        print(self.node_dict)
