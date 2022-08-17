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


mo1 = MolecularSpecies('small molecule', 'SO:235396', 'First Molecule')
mo1.molec_spec()