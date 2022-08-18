

class BioDesign:



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

    def __init__(self,name ):
        self.name = name
        self.backbone = []

    def append_part(self, part):
        '''
        
        '''
        self.backbone.append(part) 

    def return_backbone(self):
        return [self.name, self.backbone]

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
        
    def molec_spec(self):
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

        
    def interaction(self):
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


part1 = Part('Promoter1',1,'SO:2253254236',"Omar's Promoter")
part1_dict = part1.part_di()
# print(part1_dic)

part2 = Part('Promoter2',1,'SO:432436',"Tom's Promoter")
part2_dict = part2.part_di()

part3 = Part('RDS',1,'SO:923659328567',"Ahmed's RBS")
part3_dict = part3.part_di()
# print(part3_dict)

part4 = Part('CDS',1,'SO:87265923869328567',"James's CDS")
part4_dict = part4.part_di()

part5 = Part('Terminator',1,'SO:87265923869328567',"Tom's Terminator")
part5_dict = part5.part_di()

backbone1 = Backbone(name="Backbone name")
backbone1.append_part(part1_dict)
backbone1.append_part(part2_dict)
backbone1.append_part(part3_dict)
backbone1.append_part(part4_dict)
backbone1.append_part(part5_dict)


node1 = InteractionNode('dissociation', 'SO:1858478', 'First Interaction Node')
node1.node_dict()


inter1 = Interaction('control', 'CDS', 'interactiion_node -> dissociation', 'first interaction')
inter1.interaction()

mo1 = MolecularSpecies('small molecule', 'SO:235396', 'First Molecule')
mo1.molec_spec()

Bio1 =BioDesign("First BioDesign")
Bio1.add_backbone(backbone1.return_backbone())
Bio1.add_moleculer("Moleculer1")
Bio1.add_interaction_node("Node1")
Bio1.add_interaction("Interaction1")

print('Bio1\n')

Bio1.add_backbone("Backbone2")
Bio1.add_moleculer("Moleculer2")
Bio1.add_interaction_node("Node2")
Bio1.add_interaction("Interaction2")

# Bio1.print_biodesign()

Bio1.print_backbone()
Bio1.print_node()
Bio1.print_interaction()
Bio1.print_moleculer()