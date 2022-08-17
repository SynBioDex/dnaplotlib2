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


inter1 = Interaction('control', 'CDS', 'interactiion_node -> dissociation', 'first interaction')
inter1.interaction()