import dnaplotlib2 as dpl
import sbol3

doc = sbol3.Document()
doc.read("pysbol3_files/distribution.nt")

SO_to_glyph_type = {'0000031': 'Aptamer', '0001953':'Assembly Scar', '0001691':'Blunt Restriction Site', 
                    '0000316':'CDS', '0000830': "Chromosome Part 3' End",'0000830':"Chromosome Part 3' End",
                    '0002211':"Circular Plasmid 3' end", '0002211':"Circular Plasmid 5' end", '':"Spacer",
                    '0001688':"DNA Cleavage Site", '0001687':"DNA Cleavage Site",}
i = 0
objects_list = []
backbone_list = []
for object in doc.objects:
    # print(object.display_name)
    objects_list.append(object.display_name)
    backbone1 = dpl.Backbone(name=object.display_name)

    for feature in object.features:
        # print(f"Name: {feature.name}, roles: {feature.roles}, orientation: {feature.orientation}")
        SO_term = feature.roles[0][feature.roles[0].find("SO:")+3 : ]
        glyph_type = SO_to_glyph_type[SO_term]

        part1 = dpl.Part(part_type= glyph_type , name= feature.name, so_term= feature.roles, orientation= feature.orientation)
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