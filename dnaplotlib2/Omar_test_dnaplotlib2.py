import dnaplotlib2 as dpl

## First Backbone
##############################################################
b1_part1 = dpl.Part('Promoter1',1,'SO:2253254236',"Omar's Promoter")
b1_part1_dict = b1_part1.part_di()
# print(part1_dic)

b1_part2 = dpl.Part('Promoter2',1,'SO:432436',"Tom's Promoter")
b1_part2_dict = b1_part2.part_di()

b1_part3 = dpl.Part('RDS',1,'SO:923659328567',"Ahmed's RBS")
b1_part3_dict = b1_part3.part_di()
# print(part3_dict)

b1_part4 = dpl.Part('CDS',1,'SO:87265923869328567',"James's CDS")
b1_part4_dict = b1_part4.part_di()

b1_part5 = dpl.Part('Terminator',1,'SO:87265923869328567',"Tom's Terminator")
b1_part5_dict = b1_part5.part_di()

backbone1 = dpl.Backbone(name="Backbone 1")
backbone1.append_part(b1_part1_dict)
backbone1.append_part(b1_part2_dict)
backbone1.append_part(b1_part3_dict)
backbone1.append_part(b1_part4_dict)
backbone1.append_part(b1_part5_dict)

## Second Backbone
############################################################ 
b2_part1 = dpl.Part('b2_Promoter1',1,'SO:2253254236',"Omar's Promoter")
b2_part1_dict = b2_part1.part_di()
# print(part1_dic)

b2_part2 = dpl.Part('b2_Promoter2',1,'SO:432436',"Tom's Promoter")
b2_part2_dict = b2_part2.part_di()

b2_part3 = dpl.Part('b2_RDS',1,'SO:923659328567',"Ahmed's RBS")
b2_part3_dict = b2_part3.part_di()
# print(part3_dict)

b2_part4 = dpl.Part('b2_CDS',1,'SO:87265923869328567',"James's CDS")
b2_part4_dict = b2_part4.part_di()

b2_part5 = dpl.Part('b2_Terminator',1,'SO:87265923869328567',"Tom's Terminator")
b2_part5_dict = b2_part5.part_di()

backbone2 = dpl.Backbone(name="Backbone 2")
backbone2.append_part(b2_part1_dict)
backbone2.append_part(b2_part2_dict)
backbone2.append_part(b2_part3_dict)
backbone2.append_part(b2_part4_dict)
backbone2.append_part(b2_part5_dict)


## Molecular Species
##################################
mo1 = dpl.MolecularSpecies('small molecule', 'SO:235396', 'First Molecule')
mo1.molec_spec_append()

mo2 = dpl.MolecularSpecies('macromolecule', 'SO:234455396', 'Second Molecule')
mo2.molec_spec_append()

## Interaction Node
############################################
node1 = dpl.InteractionNode('dissociation', 'SO:1858478', 'First Interaction Node')
node1.node_dict()

## Interaction between b1 CDS and b2 RBS
########################################
inter1 = dpl.Interaction('control', 'b2_RBS', 'b1_CDS', 'first interaction')
inter1.interaction_append()

inter2 = dpl.Interaction('control', 'b1_CDS', 'node1' , 'second interaction')
inter2.interaction_append()

inter3 = dpl.Interaction('control', 'mo2', 'node1' , 'third interaction')
inter3.interaction_append()

inter4 = dpl.Interaction('control', 'node1', 'mo1' , 'forth interaction')
inter4.interaction_append()

## Bio Design
##################################################

Bio1 = dpl.BioDesign("First BioDesign")
Bio1.add_backbone(backbone1.return_backbone())
Bio1.add_backbone(backbone2.return_backbone())

Bio1.add_moleculer(mo1.molec_spec_append())
Bio1.add_moleculer(mo2.molec_spec_append())

Bio1.add_interaction_node(node1.node_dict())

Bio1.add_interaction(inter1.interaction_append())
Bio1.add_interaction(inter2.interaction_append())
Bio1.add_interaction(inter3.interaction_append())
Bio1.add_interaction(inter4.interaction_append())


print('\n Bio1 \n\n')

# Bio1.add_backbone("Backbone2")
# Bio1.add_moleculer("Moleculer2")
# Bio1.add_interaction_node("Node2")
# Bio1.add_interaction("Interaction2")

# Bio1.print_biodesign()
print(Bio1.return_biodesign())
# Bio1.print_backbone()
# Bio1.print_node()
# Bio1.print_interaction()
# Bio1.print_moleculer()