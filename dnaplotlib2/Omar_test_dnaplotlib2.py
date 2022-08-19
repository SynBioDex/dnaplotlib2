from dnaplotlib2 import BioDesign, Backbone, Part, MolecularSpecies, Interaction, InteractionNode

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

Bio1.print_biodesign()

Bio1.print_backbone()
Bio1.print_node()
Bio1.print_interaction()
Bio1.print_moleculer()