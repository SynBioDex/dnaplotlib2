from enum import Enum

class Orientation(Enum):
	FORWARD = 1
	REVERSE = 2

class Part:
	part_type
	orientation
	so_term
	name


class Backbone:
	backbone_type
	parts = []

	def append_part(new_part):


class MolecularSpecies:
	molecular_species_type
	so_term
	name

    
class InteractionNode:
	interaction_node_type
	so_term
	name


class Interaction:
	interaction_type
	start_object
	end_object
	name


class BioDesign:
	name
	backbones = []
	molecular_species = []
	interaction_nodes = []
	interactions = []


