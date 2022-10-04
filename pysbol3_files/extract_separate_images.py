import dnaplotlib2 as dpl
import sbol3

# create document to read sbol file
doc = sbol3.Document()
doc.read("pysbol3_files\distribution.nt")
print(len(doc))
print(doc)

# create renderer to draw components
renderer  = dpl.Renderer()

i = 0
backbone_list = []


for object in doc.objects:
    if not isinstance(object, sbol3.Component):    # iterate only through component objects
        continue
    print(object.display_name , i)
    # print(f"Name: {object.name}, roles: {object.roles}")
    
    backbone1 = dpl.Backbone(name=object.display_name)

    for feature in object.features:  
        # print(f"Name: {feature.display_id}, roles: {feature.roles}, orientation: {feature.orientation}")
        # print(object.display_name , i)

        if feature.roles == []:   # skip features that don't have SO_term
            continue
        # print(f'SO: {feature.roles}')
        SO_term = feature.roles[0][feature.roles[0].find("SO:") : ]
        # print(f'SO_term = {SO_term}')

        if SO_term in renderer.renderer.glyph_term_map.keys():    # map SO_term to glyph type in parasbolv
            # print(f'SO_term {SO_term}')
            glyph_type = renderer.renderer.glyph_term_map[SO_term]

            part1 = dpl.Part(part_type= glyph_type , name= feature.name, so_term= feature.roles, orientation= feature.orientation)
            part1_dict = part1.part_di()
            # print(part1_dict)

            backbone1.append_part(part1_dict)

        backbone_list.append(backbone1)
    i += 1
    if i > 70:
        break

# print(f'backbone_list = {backbone_list[45].backbones}')
Bio1 = dpl.BioDesign("First BioDesign")
for i in range(0, len(backbone_list)):
    if backbone_list[i].backbones == []:
        continue
    Bio1.add_backbone(backbone_list[i].backbones)
print(f'Bio1 Backbones: {Bio1.backbones}')

draw_dpl = dpl.Renderer().bio_render(Bio1)

