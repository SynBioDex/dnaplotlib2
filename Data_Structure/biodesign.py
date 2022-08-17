
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
        return self.backbone


    def add_moleculer(self, moleculer):
        self.molecular_species.append(moleculer)   

    def print_moleculer(self):
        print(self.molecular_species)
        return self.molecular_species


    def add_interaction_node(self, node):
        self.interaction_node.append(node)

    def print_node(self):
        print(self.interaction_node)
        return self.interaction_node

    
    def add_interaction(self, interaction):
        self.interaction.append(interaction)

    def print_interaction(self):
        print(self.interaction)
        return self.interaction
    

    def print_biodesign(self):
        print(f"Name of BioDesign is -> {self.name}","\n",
            f"Backbones are -> {self.print_backbone()}\n",
            f"Species are -> {self.print_moleculer()}\n",
            f"Nodes are -> {self.print_node()}\n",
            f"Interactions are -> {self.print_interaction()}")



Bio1 =BioDesign("First BioDesign")
Bio1.add_backbone("Backbone1")
Bio1.add_moleculer("Moleculer1")
Bio1.add_interaction_node("Node1")
Bio1.add_interaction("Interaction1")

Bio1.add_backbone("Backbone2")
Bio1.add_moleculer("Moleculer2")
Bio1.add_interaction_node("Node2")
Bio1.add_interaction("Interaction2")

Bio1.print_biodesign()