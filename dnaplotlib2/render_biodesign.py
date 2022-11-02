import dnaplotlib2 as dpl


b1_part2 = dpl.Part(part_type="Promoter", orientation = None, 
                        so_term=['https://identifiers.org/SO:0000167'], name='Promoter 1', start_range=1)
b1_part2_dict = b1_part2.part_di()

b1_part3 = dpl.Part(part_type="Recombination Site", orientation=None ,
                         so_term=['https://identifiers.org/SO:0000139'], name='RBS 1', start_range=6)
b1_part3_dict = b1_part3.part_di()

b1_part4 = dpl.Part(part_type="CDS", orientation=None , 
                        so_term=['https://identifiers.org/SO:0000316'], name='GFP 1', start_range=3)
b1_part4_dict = b1_part4.part_di()

b1_part5 = dpl.Part(part_type="Terminator", orientation=None , 
                        so_term=['https://identifiers.org/SO:0000141'], name='Terminator 1', start_range=4)
b1_part5_dict = b1_part5.part_di()


backbone1 = dpl.Backbone(name="Backbone 1")
backbone1.append_part(b1_part2_dict)
backbone1.append_part(b1_part3_dict)
backbone1.append_part(b1_part4_dict)
backbone1.append_part(b1_part5_dict)

## Interaction between b1 CDS and b2 RBS
########################################
# inter1 = dpl.Interaction(interaction_type="control", start_object=backbone1.backbones[0], 
#                         end_object=backbone1.backbones[2], 
#                         name="first interaction")
# inter1.interaction_append()


## Second Backbone

b2_part2 = dpl.Part(part_type="Promoter", orientation = None,
                             so_term=['https://identifiers.org/SO:0000167'], name='Promoter 2', start_range=1)
b2_part2_dict = b2_part2.part_di()

b2_part3 = dpl.Part(part_type="Recombination Site", orientation=None , 
                            so_term=['https://identifiers.org/SO:0000139'], name='RBS 2', start_range=2)
b2_part3_dict = b2_part3.part_di()


b2_part5 = dpl.Part(part_type="Terminator", orientation=None , 
                            so_term=['https://identifiers.org/SO:0000141'], name='Terminator 2', start_range=3)
b2_part5_dict = b2_part5.part_di()

backbone2 = dpl.Backbone(name="Backbone 2")
backbone2.append_part(b2_part2_dict)
backbone2.append_part(b2_part3_dict)
backbone2.append_part(b2_part5_dict)



# inter2 = dpl.Interaction(interaction_type="control", start_object=backbone2.backbones[1], end_object=backbone2.backbones[2], 
#                         name="second interaction")
# inter2.interaction_append()


Bio1 = dpl.BioDesign("First BioDesign")
Bio1.add_backbone(backbone1.backbones)
Bio1.add_backbone(backbone2.backbones)
# Bio1.add_interaction(inter1.interaction_dict)
# Bio1.add_interaction(inter2.interaction_dict)



draw_dpl = dpl.Renderer().bio_render(Bio1)


# draw_constract = dpl.Renderer().draw_construct(Bio1)
# # Set Bounds
# ax.set_ylim([0,100])
# ax.set_xlim([0,100])

# plt.show()
