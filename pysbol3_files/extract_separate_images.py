import dnaplotlib2 as dpl
import sbol3

# create document to read sbol file
doc = sbol3.Document()
doc.read("gfp.nt")
print(len(doc))
print(doc)

# print(list(doc))
# create renderer to draw components
renderer  = dpl.Renderer()
backbone1 = dpl.Backbone(name='Omar backbone')

doc.find('https://github.com/iGEM-Engineering/iGEM-distribution/Anderson%20Promoters/pSB1C5')
i = 0
backbone_list = []

dfs_result = []
visited = set()
objects_list = []
object_dict = {}

def dfs(node, doc, i):
    if isinstance(node, sbol3.Component):    # iterate only through component objects
        
        visited.add(node)
        dfs_result.append(node)
        objects_list.append(node.display_id)
        # print(type(node), i)
        i = i + 1

        if node.features == []:
            if node.roles != []:   # skip features that don't have SO_term
                SO_term = node.roles[0][node.roles[0].find("SO:") : ]
                if SO_term in renderer.renderer.glyph_term_map.keys():    # map SO_term to glyph type in parasbolv
                    # print(f'SO_term {SO_term}')
                    glyph_type = renderer.renderer.glyph_term_map[SO_term]

                    part1 = dpl.Part(part_type= glyph_type , name= node.name, so_term= node.roles, orientation=None)
                    part1_dict = part1.part_di()
                    # print(part1_dict)
                    backbone1.append_part(part1_dict)
            

        # print(node.display_id)
        for feature in node.features: 
            print(f"Name: {feature.display_id}, roles: {feature.roles}")
            if feature.roles == []:   # skip features that don't have SO_term
                continue
            SO_term = feature.roles[0][feature.roles[0].find("SO:") : ]
            if SO_term in renderer.renderer.glyph_term_map.keys():    # map SO_term to glyph type in parasbolv
                # print(f'SO_term {SO_term}')
                glyph_type = renderer.renderer.glyph_term_map[SO_term]

                part1 = dpl.Part(part_type= glyph_type , name= feature.name, so_term= feature.roles, orientation=feature.orientation)
                part1_dict = part1.part_di()
                # print(part1_dict)
                backbone1.append_part(part1_dict)
            
            # print(feature.display_id)
            # if type(feature) == str:
            #     continue
            # if feature not in visited:

            dfs(feature, doc, i)

# dfs(doc.objects[0], doc, i) 
# print(dfs_result)    

# print(doc.objects[3].features)
for object in doc.objects:
    if not isinstance(object, sbol3.Component):    # iterate only through component objects
        continue
    if object not in visited:

        dfs(object, doc, i)
        object_dict[object.display_id] = objects_list
        # print(object_dict)

        backbone_list.append(backbone1)
        objects_list = []


print(f'backbone list = {len(backbone_list)}')
print(len(dfs_result))  
 
print(len(object_dict))
# print(object_dict)
# print(dfs_result)    

    # print(object.display_name , i)
    # print(f"Name: {object.name}, roles: {object.roles}")
    
#     backbone1 = dpl.Backbone(name=object.display_name)
#     if object.features == []:
#         print(f"Name: {object.display_id}, roles: {object.roles}")
#     # print(f'object features : {object.features}')

#     for feature in object.features:  
#         # print(f'feature : {feature}')
#         print(f"Name: {feature.display_id}, roles: {feature.roles}, orientation: {feature.orientation}")
#         # print(object.display_name , i)

#         if feature.roles == []:   # skip features that don't have SO_term
#             continue
#         # print(f'SO: {feature.roles}')
#         SO_term = feature.roles[0][feature.roles[0].find("SO:") : ]
#         # print(f'SO_term = {SO_term}')

#         if SO_term in renderer.renderer.glyph_term_map.keys():    # map SO_term to glyph type in parasbolv
#             # print(f'SO_term {SO_term}')
#             glyph_type = renderer.renderer.glyph_term_map[SO_term]

#             part1 = dpl.Part(part_type= glyph_type , name= feature.name, so_term= feature.roles, orientation= feature.orientation)
#             part1_dict = part1.part_di()
#             # print(part1_dict)

#             backbone1.append_part(part1_dict)

#         backbone_list.append(backbone1)
#     i += 1
#     if i > 44:
#         break

# # print(f'backbone_list = {backbone_list[45].backbones}')
Bio1 = dpl.BioDesign("First BioDesign")
Bio1.add_backbone(backbone1.backbones)
# print(f'Bio1 Backbones: {Bio1.backbones}')
print(f'backbone1 = {backbone1}')

# for i in range(0, len(backbone_list)):
#     if backbone_list[i].backbones == []:
#         continue
#     Bio1.add_backbone(backbone_list[i].backbones)
# print(f'Bio1 Backbones: {Bio1.backbones}')

draw_dpl = dpl.Renderer().bio_render(Bio1)

