import dnaplotlib2 as dpl
import sbol3

doc = sbol3.Document()
doc.read("pysbol3_files/distribution.nt")
i = 0
objects_list = []
backbone_list = []
for object in doc.objects:
    # print(object.display_name)
    objects_list.append(object.display_name)
    backbone1 = dpl.Backbone(name=object.display_name)

    for feature in object.features:
        # print(f"Name: {feature.name}, roles: {feature.roles}, orientation: {feature.orientation}")

        part1 = dpl.Part(part_type=' ', name= feature.name, so_term= feature.roles, orientation= feature.orientation)
        part1_dict = part1.part_di()
        # print(part1_dict)

        backbone1.append_part(part1_dict)
    # print(backbone1)
    backbone_list.append(backbone1)
    backbone_list.append('\n')
    # print("\n\n")
    i += 1
    if i > 43:
        break


Bio1 = dpl.BioDesign("First BioDesign")
Bio1.add_backbone(backbone_list)
print(Bio1)

# part1 = dpl.Part(part_type=' ', orientation= part_orientation, so_term= part_roles , name= part_name)
# part1_dict = part1.part_di()
# print(part1_dict)


# backbone1 = dpl.Backbone(name="Backbone 1")
# backbone1.append_part(part1_dict)
# print(backbone1)
# print(objects_list,'\n')
# print(backbone_list)