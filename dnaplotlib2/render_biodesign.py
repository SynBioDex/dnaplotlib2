import parasbolv as psv
import matplotlib.pyplot as plt
import dnaplotlib2 as dpl

# # Generate Matplotlib Figure and Axes
# fig = plt.figure(figsize=(6,6))
# ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

# # Generate renderer object
# renderer = psv.GlyphRenderer()

# # Draw Ribosome Entry Site
# bounds, end_point = renderer.draw_glyph(ax, 'Recombination Site', (20, 50))


b1_part1 = dpl.Part("Promoter", "forward", None, None)
b1_part1_dict = b1_part1.part_di()

b1_part2 = dpl.Part("Promoter", "forward", None, None)
b1_part2_dict = b1_part2.part_di()

b1_part3 = dpl.Part("Recombination Site", "forward", None, None)
b1_part3_dict = b1_part3.part_di()
# print(part3_dict)

b1_part4 = dpl.Part("CDS", "forward", None, None)
b1_part4_dict = b1_part4.part_di()

b1_part5 = dpl.Part("Terminator", "forward", None, None)
b1_part5_dict = b1_part5.part_di()


backbone1 = dpl.Backbone(name="Backbone 1")
backbone1.append_part(b1_part1_dict)
backbone1.append_part(b1_part2_dict)
backbone1.append_part(b1_part3_dict)
backbone1.append_part(b1_part4_dict)
backbone1.append_part(b1_part5_dict)

print('backbone1.backbones[0] - >',backbone1.backbones[0])
print('backbone1.backbones[2] - >',backbone1.backbones[2])

## Interaction between b1 CDS and b2 RBS
########################################
inter1 = dpl.Interaction(interaction_type="control", start_object=backbone1.backbones[0], 
                        end_object=backbone1.backbones[2], 
                        name="first interaction")
inter1.interaction_append()


## Second Backbone
b2_part1 = dpl.Part("Promoter", "forward", None, None)
b2_part1_dict = b2_part1.part_di()
# print(part1_dic)


b2_part2 = dpl.Part("Recombination Site", "forward", None, None)
b2_part2_dict = b2_part2.part_di()
# print(part3_dict)

b2_part3 = dpl.Part("Terminator", "forward", None, None)
b2_part3_dict = b2_part3.part_di()

backbone2 = dpl.Backbone(name="Backbone 2")
backbone2.append_part(b2_part1_dict)
backbone2.append_part(b2_part2_dict)
backbone2.append_part(b2_part3_dict)



inter2 = dpl.Interaction(interaction_type="control", start_object=backbone2.backbones[1], end_object=backbone2.backbones[2], 
                        name="second interaction")
inter2.interaction_append()


Bio1 = dpl.BioDesign("First BioDesign")
Bio1.add_backbone(backbone1.backbones)
Bio1.add_interaction(inter1.interaction_dict)
Bio1.add_interaction(inter2.interaction_dict)


Bio1.add_backbone(backbone2.backbones)

# draw_dpl = dpl.Renderer().bio_render(Bio1)


draw_constract = dpl.Renderer().draw_construct(Bio1)
# # Set Bounds
# ax.set_ylim([0,100])
# ax.set_xlim([0,100])

# plt.show()
