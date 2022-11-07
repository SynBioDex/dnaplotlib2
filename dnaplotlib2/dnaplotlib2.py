import parasbolv as psv
import matplotlib.pyplot as plt
import sbol3

class BioDesign:
    """
    Class for collecting and printting all Bio Design components like Backbones, Molecular Species
    and Interactions
    """

    def __init__(self, name):
        self.name = name
        self.backbones = []
        self.molecular_species = []
        self.interaction_node = []
        self.interaction = []
        self.biodesign_output = []

    def __repr__(self):
        """return a string representation of the object"""
        self.biodesign_output = [
            self.name,
            self.backbones,
            self.molecular_species,
            self.interaction_node,
            self.interaction,
        ]

        return f"{self.biodesign_output}"

    def add_backbone(self, backbones):
        """
        function to append backbones to a list in a biodesign
        """
        self.backbones.append(backbones)

    def add_moleculer(self, moleculer):
        """
        function to add new molecule to the biodesign
        """
        self.molecular_species = moleculer


    
    def add_interaction_node(self, node):
        """
        function to append new interaction node to the biodesign
        """
        self.interaction_node.append(node)


    def add_interaction(self, interaction):
        """
        function to append new interaction to the biodesign
        """
        self.interaction.append(interaction)
   
    def show_biodesign(self):
        '''
        function to add components to current biodesign
        '''
        self.biodesign_output = [
        self.name,
        self.backbones,
        self.molecular_species,
        self.interaction_node,
        self.interaction,
    ]
        
    def print_biodesign(self):
        """
        function to print all biodesign components
        """
        print(
            f"Name of BioDesign is -> {self.name}",
            "\n\n",
            f"Backbones are -> {self.backbones}\n\n",
            f"Species are -> {self.molecular_species}\n\n",
            f"Nodes are -> {self.interaction_node}\n\n",
            f"Interactions are -> {self.interaction}",
        )


class Backbone:
    """
    class to create backbone through adding different parts
    output:  list of dict of added parts
    """

    def __init__(self, name="Backbone Init"):
        self.name = name
        self.backbones = []
        self.backbones_list = [self.name]

    def __repr__(self):
        """return a string representation of the object"""
        self.backbones_list = [self.name, self.backbones]
        return f"{self.backbones_list}"


    def append_part(self, part):
        """
        function to append new part to the backbone
        """
        self.backbones.append(part)
        self.backbones_list.append(self.backbones)


class Part:
    """
    class to create a new part with all components of it
    """

    def __init__(self, part_type, orientation, so_term, name, start_seq_range = -1 , end_seq_range = None, start_point= (0,0)):
        self.part_type = part_type
        self.orientation = orientation
        self.so_term = so_term
        self.name = name
        self.part_list = []
        self.part_dict = {}
        self.start_point = start_point
        self.start_range = start_seq_range
        self.end_range = end_seq_range
        

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

        self.part_list.append(self.start_point)
        self.part_list.append(self.start_range)
        self.part_list.append(self.end_range)

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

        self.part_dict["start_point"] = self.start_point
        self.part_dict["start_seq_range"] = self.start_range
        self.part_dict["end_seq_range"] = self.end_range

        return self.part_dict


class MolecularSpecies:
    """
    class to create a new molecular species
    """

    def __init__(self, molecular_species_type, so_term, name):
        self.molecular_species_type = molecular_species_type
        self.so_term = so_term
        self.name = name
        self.species = {}

    def __repr__(self):
        """return a string representation of the object"""
        return f"(Molecule object contains {self.species})"

    def molec_spec_append(self):
        """
        function to add new molecule to a list of all molecules
        """
        self.species["molecular_species_type"] = self.molecular_species_type
        self.species["so_term"] = self.so_term
        self.species["name"] = self.name
        return self.species

    def print_spec(self):
        """
        function to print a list of all available molecules
        """
        print(self.species)


class Interaction:
    """
    class to create new interaction between parts, molecules or nodes
    """

    def __init__(self, interaction_type, start_object, end_object, name):
        self.interaction_type = interaction_type
        self.start_object = start_object
        self.end_object = end_object
        self.name = name
        self.interaction_dict = {}

    def __repr__(self):
        """return a string representation of the object"""
        return f"(Interaction object contains {self.interaction_dict})"

    def interaction_append(self):
        """
        function to append new interaction to the interaction list
        """

        self.interaction_dict["interaction_type"] = self.interaction_type
        self.interaction_dict["start_object"] = self.start_object
        self.interaction_dict["end_object"] = self.end_object
        self.interaction_dict["name"] = self.name

    def print_interaction(self):
        """
        function to print a list of all interactions
        """

        print(self.interaction_dict)


class InteractionNode:
    """
    class to create new list of interaction nodes
    """

    def __init__(self, interaction_node_type, so_term, name):
        self.interaction_node_type = interaction_node_type
        self.so_term = so_term
        self.name = name
        self.inter_node_dict = {}

    def __repr__(self):
        """return a string representation of the object"""
        return f"(Node object contains {self.inter_node_dict})"

    def node_dict(self):
        """
        function to create a dictionary of interaction node components
        """

        self.inter_node_dict["interaction_node_type"] = self.interaction_node_type
        self.inter_node_dict["so_term"] = self.so_term
        self.inter_node_dict["name"] = self.name

    def print_node(self):
        """
        function to print list of interaction nodes
        """
        print(self.node_dict)


class Renderer:
    """This class will render biological glyphs and plot them into matplotlib figure
    """
    
    def __init__(self):

        self.renderer = psv.GlyphRenderer()
        self.biodesign = []
        self.part_dict = {}
        self.part_list = []
        self.backbone1 = Backbone(name='Omar backbone')
        self.backbone_list = []
        self.molecules_list = []
        self.visited = set()
        
    def get_components(self, doc, index = -1):  # not working yet
        if index >= 0 and index <= len(doc.objects):
            Renderer().dfs(doc.objects[index-1])     # search for subcomponents to draw complete backbones (flatten the hierarichy)
            self.backbone_list.append(self.backbone1)
            self.backbone1 = Backbone(name='Omar backbone')
        else:   
            # Go through every component object in the doc and return its subcomponent using dfs function
            for object in doc.objects:
                # print(f'Function works _>>>>>>>>>>>>>>> {len(doc.objects)}')
                if not isinstance(object, sbol3.Component):    # iterate only through component objects
                    continue
                if object not in self.visited:
                    Renderer().dfs(object)     # search for subcomponents to draw complete backbones (flatten the hierarichy)
                    # print(f'self backbone ->>> {self.backbone1}')
                    self.backbone_list.append(self.backbone1)
                    self.backbone1 = Backbone(name='Omar backbone')
                    # print(f'backbones ->>> {self.backbone_list}')

    def dfs(self, obj):
        '''
        function to flatten the hierarchy of the backbone through getting its subcomponents

        input: 
        node -> doc.object that will be a beackbone 

        output: 
        backbone1 -> a list of parts dictionary of the backbone
        molecular list -> a list of molecular species
        '''
        self.node = obj

        # iterate only through component objects
        if isinstance(self.node, sbol3.Component):    
            
            self.visited.add(self.node)
            # print(f"node display id ->>> {self.node.display_id}, roles ->> {self.node.roles}, instance of ->> {self.node.instance_of}")
            # if object doesn't contain subcomponents features, get its attributes
            if self.node.features == []:    

                # skip objects that don't have SO_term or SBO_term
                if self.node.roles != []:   
                    SBO_term = self.node.roles[0][self.node.roles[0].find("SBO:") : ]
                    SO_term = self.node.roles[0][self.node.roles[0].find("SO:") : ]

                    # map SO_term to glyph type in parasbolv
                    if SO_term in self.renderer.glyph_term_map.keys():    

                        glyph_type = self.renderer.glyph_term_map[SO_term]

                        part1 = Part(part_type= glyph_type , name= self.node.name, 
                                    so_term= self.node.roles, orientation=None )
                        part1_dict = part1.part_di()
                        self.backbone1.append_part(part1_dict)

                    # map SBO_term to glyph type in parasbolv
                    if SBO_term in self.renderer.glyph_term_map.keys():    

                        glyph_type = self.renderer.glyph_term_map[SBO_term]

                        mol1 = MolecularSpecies(molecular_species_type= glyph_type, 
                                                name= self.node.name, so_term=SBO_term)
                        mol1_dict = mol1.molec_spec_append()
                        # print(f"Mol1 -> {mol1_dict}")
                        self.molecules_list.append(mol1_dict)    
                        # print(f"self.molecules_list -> {self.molecules_list}")

            # get attributes of subcomponents
            for feature in self.node.features:
                print(f"Name: {feature.display_id}, roles: {feature.roles}, instance of:{feature.instance_of} ") #{feature.instance_of} {feature.locations.property_owner}
                
                # skip features that don't have SO_term
                if feature.roles == []:            
                    continue
                SO_term = feature.roles[0][feature.roles[0].find("SO:") : ]

                # map SO_term to glyph type in parasbolv
                if SO_term in self.renderer.glyph_term_map.keys():    
                    glyph_type = self.renderer.glyph_term_map[SO_term]

                    part1 = Part(part_type= glyph_type , name= feature.name,
                                so_term= feature.roles, orientation=feature.orientation)
                    part1_dict = part1.part_di()
                    
                    self.backbone1.append_part(part1_dict)
                
                Renderer().dfs(feature)

    
    def bio_render(self, biodesign):
        """
        This function take biodesign as input and plot it using matplotlib
        """
        # Generate Matplotlib Figure and Axes
        fig = plt.figure(figsize=(9,6))
        ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)
        x = 10
        y = 10
        i=1
        start_point = (x, y)
        end_point = start_point
        mol_pos = (50,50)
        self.biodesign = biodesign
        
        ## draw molecular species
        if len(self.biodesign.molecular_species) != 0:
            for mol in self.biodesign.molecular_species:
                bound, end_point = self.renderer.draw_glyph(ax, mol['molecular_species_type'], position=mol_pos)
                mol_pos = mol_pos + (20,20)

        # we will sort parts according to range start position on seq
        for i in range(0, len(self.biodesign.backbones)):
            self.biodesign.backbones[i] = sorted(self.biodesign.backbones[i], key=lambda k: k['start_seq_range']) 
            # print(f"sorted backbone -> {self.biodesign.backbones[i]}")

        ### draw parts of different backbones
        for backbone in self.biodesign.backbones:
            # print(f'backbone to draw = {backbone}')
            for part in backbone:
                part['start_point'] = start_point
                bounds, end_point = self.renderer.draw_glyph(ax, part['part_type'], position=part['start_point'])
                start_point = end_point 

            y = y + 30
            start_point = (x, y)
 
        # Set Bounds
        ax.set_ylim([0,end_point[1]+20])
        ax.set_xlim([0,end_point[0]+50])

        plt.show()

    # def draw_construct(self, biodesign, part_list=[]):
    #     import parasbolv as psv
    #     import matplotlib.pyplot as plt

    #     # Draw construct
    #     self.biodesign = biodesign
    #     self.part_list = part_list

    #     i = 0

    #     for b in self.biodesign.backbones:

    #         for part in b:
    #             self.part_list.append(list(part.values()))

    #         self.part_dict[i] = self.part_list
    #         i = i + 1
            
    #         # print(self.part_list)
    #         self.part_list = []
    #         # print(self.part_list)

    #     # from collections import namedtuple
    #     self.interaction_dict = {}
    #     interaction_list = []
    #     # interaction = namedtuple('interaction', ['starting_glyph', 'ending_glyph', 'interaction_type', 'interaction_parameters'])

    #     i = 0

    #     for interaction in self.biodesign.interaction:
    #         print('part_dict - > ',self.part_dict)
    #         print('interaction - >', interaction)


    #         interaction['start_object'] = list(interaction['start_object'].values())
    #         interaction['end_object'] = list(interaction['end_object'].values())

    #         # interaction[]
    #         interaction_list.append([interaction['start_object'], interaction['end_object'], interaction['interaction_type'],
    #          {'color': (0.75,0,0)}])
    #         # interaction_list.append(interaction(part_list[2], part_list[4], 'control', {'color': (0, 0.75, 0),
    #         #                                                                 'direction':'reverse'}))
    #         self.interaction_dict[i] = interaction_list
    #         i = i + 1
    #         interaction_list = []
    #         print('part_dict - > ',self.part_dict)
    #         print('interaction_list -> ',interaction_list)
    #         print('self.interaction_dict - >  ', self.interaction_dict)


    #     # todo- create a loop to draw a list of backbones

    #     construct = psv.Construct(self.part_dict[0], self.renderer, interaction_list=self.interaction_dict[0]) 
        
    #     fig, ax, baseline_start, baseline_end, bounds = construct.draw()
    #     ax.plot([baseline_start[0], baseline_end[0]], [baseline_start[1], baseline_end[1]], color=(0,0,0), linewidth=1.5, zorder=0)

    #     construct2 = psv.Construct(self.part_dict[1], self.renderer, interaction_list=self.interaction_dict[1], 
    #                                 fig=fig, ax=ax, start_position=(0,60), additional_bounds_list=[bounds])
    #     construct2.update_bounds()
    #     fig, ax, baseline_start, baseline_end, bounds = construct2.draw()
    #     ax.plot([baseline_start[0], baseline_end[0]], [baseline_start[1], baseline_end[1]], color=(0,0,0), linewidth=1.5, zorder=0)

    #     plt.show()


    #     # def draw_construct(self, biodesign, part_list):
