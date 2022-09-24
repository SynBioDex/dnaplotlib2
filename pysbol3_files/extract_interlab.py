import dnaplotlib2 as dpl
import sbol3

doc = sbol3.Document()
doc.read("pysbol3_files/iGEM-Engineering iGEM-distribution develop iGEM20Devices/iGEM Interlab Devices/iGEM_SBOL2_imports.nt")
i = 0
objects_list = []
backbone_list = []
for object in doc.objects:
    print(object.display_name)
    objects_list.append(object.display_name)
    backbone1 = dpl.Backbone(name=object.display_name)
    # print(object.features)
    print(i)
    # for seq in object.features:
    #     # print(seq)

    #     # print(f"Name: {feature.name}, roles: {feature.roles}, orientation: {feature.orientation}")

    #     # part1 = dpl.Part(part_type=' ', name= feature.name, so_term= feature.roles, orientation= feature.orientation)
    #     # part1_dict = part1.part_di()
    #     # print(part1_dict)

    #     # backbone1.append_part(part1_dict)
    # # print(backbone1)
    # backbone_list.append(backbone1)
    # backbone_list.append('\n')
    # print("\n\n")
    i += 1
    if i > 8:
        break


# Bio1 = dpl.BioDesign("First BioDesign")
# Bio1.add_backbone(backbone_list)
# print(Bio1)
