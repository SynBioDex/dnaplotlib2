import dnaplotlib2 as dpl
import sbol3


### function dfs -Depth First Search- to flatten all components
'''
# create document to read sbol file
doc = sbol3.Document()
doc.read("pysbol3_files\distribution.nt")
print(len(doc))
print(doc)

# print(list(doc))
# create renderer to draw components
renderer  = dpl.Renderer()

i = 0
backbone_list = []

dfs_result = []
visited = set()

def dfs(node, doc, i):
    if isinstance(node, sbol3.Component):    # iterate only through component objects
        
        visited.add(node)
        dfs_result.append(node)


        # print(type(node), i)
        i = i + 1
        
        if node.features != []:
            for feature in node.features: 
                # if type(feature) == str:
                #     continue
                if feature not in visited:
                    dfs(feature, doc, i)

# dfs(doc.objects[0], doc, i) 
# print(dfs_result)    

# print(doc.objects[3].features)
for object in doc.objects:
    if not isinstance(object, sbol3.Component):    # iterate only through component objects
        continue
    # print(object._owned_objects)
    dfs(object, doc, i)
print(len(dfs_result)) 
'''

doc = sbol3.Document()
doc.read("pysbol3_files\distribution.nt")
print(len(doc))
print(doc)

# for obj in doc.objects:
#     if not isinstance(obj, sbol3.Component):
#         continue
#     print(obj.display_id)
#     print(f"Name: {obj.name}, roles: {obj.roles}, types: {obj.types}")

#     for feature in obj.features:
#         print(f"Name: {feature.display_id}, roles: {feature.roles}")
#         for sub in feature.features:
#             print(f"Name: {feature.display_id}, roles: {feature.roles}")

# ...
# # SO_to_glyph_type = {'0000031': 'Aptamer', 
#                     '0001953':'Assembly Scar', 
#                     '0001691':'Blunt Restriction Site', 
#                     '0000316':'CDS', 
#                     '0000830': "Chromosome Part 3' End",
#                     '0000830':"Chromosome Part 3' End",
#                     '0002211':"Circular Plasmid 3' end", 
#                     '0002211':"Circular Plasmid 5' end", 
#                     '0001688':"DNA Cleavage Site",
#                      '0001687':"DNA Cleavage Site",
#                      '0001236':"DNA Location",
#                     '0000699': "DNA Location",
#                      '0000616':"DNA Stop Site",
#                      '0000251':"Double-Stranded Nucleic Acid",
#                      '0000804':"Engineered Region",
#                      '0000627':"Insulator",
#                      '0000245':"Macromolecule",
#                      '0000057':"Operator",
#                      '0000409':"Operator",
#                      '0000296':"OriginOfReplication",
#                      '0000724':"OriginOfTransfer",
#                      '0001933':"3' Overhang Site",
#                      '0001932':"5' Overhang Site",
#                      '0000553':"PolyA Site",
#                      '0000839':"Polypeptide Region",
#                      '0005850':"PrimerBindingSite",
#                      '0000167':"Promoter",
#                      '0000252':"Polypeptide Chain",
#                      '0001956':"Protein Cleavage Site",
#                      '0001237':"Protein Location",
#                      '0000699':"Protein Location",
#                      '0001237':"Protein Location",
#                      '0000699':"Protein Location",
#                      '0001955':"Protein Stability Element",
#                      '0001546':"Protein Stability Element",
#                      '0000139':"RibosomeEntrySite",
#                      '0001688':"RNA Cleavage Site",
#                      '0001687':"RNA Cleavage Site",
#                      '0001977':"RNA Cleavage Site",
#                      '0001236':"RNA Location",
#                      '0000699':"RNA Location",
#                      '0001236':"RNA Location",
#                      '0000699':"RNA Location",
#                      '0001979':"RNA Stability Element",
#                      '0000319':"RNA Stop Site",
#                      '0000327':"RNA Stop Site",
#                      '0001978':"Signature",
#                      '0000247':"Simple Chemical (Circle)",
#                      '0000250':"Single-Stranded Nucleic Acid",
#                      '0002223':"InertDNASpacer",
#                      '0001976':"3' Sticky Restriction Site",
#                      '0001975':"5' Sticky Restriction Site",
#                      '0000141':"Terminator",
#                      '0000110':"Unspecified"
#                     }

renderer  = dpl.Renderer()

i = 0
objects_list = []
backbone_list = []
glyph_type = ''

# for object in doc.objects:
#     # if not isinstance(object, sbol3.Component):
#     #     continue
#     print(object.display_name , i)
#     print(f"Name: {object.name}, roles: {object.roles}")

#     # objects_list.append(object.display_name)
#     # backbone1 = dpl.Backbone(name=object.display_name)
#     print(object.features)
#     for feature in object.features:
#         print(f"Name: {feature.name}, roles: {feature.roles}, orientation: {feature.orientation}")
#     #     print(object.display_name , i)

#         # print(f'SO: {feature.roles[0]}')
#         # SO_term = feature.roles[0][feature.roles[0].find("SO:") : ]
#         # print(f'SO_term = {SO_term}')

#         # if SO_term in renderer.renderer.glyph_term_map.keys():
#         #     glyph_type = renderer.renderer.glyph_term_map[SO_term]

#         #     part1 = dpl.Part(part_type= glyph_type , name= feature.name, so_term= feature.roles, orientation= feature.orientation)
#         #     part1_dict = part1.part_di()
#         # print(part1_dict)

#             # backbone1.append_part(part1_dict)
#     # print(backbone1)
#     # backbone_list.append(backbone1)
#     # backbone_list.append('\n')
#     # print("\n\n")
#     i += 1
#     # if i > 44:
#     #     break


# Bio1 = dpl.BioDesign("First BioDesign")
# # Bio1.add_backbone(backbone_list[42])
# Bio1.add_backbone(backbone_list[1].backbones)
# # Bio1.add_backbone(backbone_list[43].backbones)
# # Bio1.add_backbone(backbone_list[44].backbones)
# print(Bio1)

# part1 = dpl.Part(part_type=' ', orientation= part_orientation, so_term= part_roles , name= part_name)
# part1_dict = part1.part_di()
# print(part1_dict)

# draw_dpl = dpl.Renderer().bio_render(Bio1)
