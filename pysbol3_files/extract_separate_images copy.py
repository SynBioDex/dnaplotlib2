import dnaplotlib2 as dpl
import sbol3

# create document to read sbol file
doc = sbol3.Document()
doc.read("sbol_test_cases\\sbol_files\\two_backbones_and_molecule_case.nt")
print(f"doc lenght -> {len(doc)}")

# create renderer to draw components
backbone1 = dpl.Backbone(name='Omar backbone')
renderer  = dpl.Renderer()

# i = 0
# backbone_list = []
# molecules_list = []

# dfs_result = []
# visited = set()
# objects_list = []
# object_dict = {}

# def dfs(node):
#     '''
#     function to flatten the hierarchy of the backbone through getting its subcomponents

#     input: 
#     node -> doc.object that will be a beackbone 

#     output: 
#     backbone1 -> a list of parts dictionary of the backbone
#     molecular list -> a list of molecular species
#     '''
#     if isinstance(node, sbol3.Component):    # iterate only through component objects
        
#         visited.add(node)
#         dfs_result.append(node)
#         objects_list.append(node.display_id)
        
#         if node.features == []:    # if object doesn't contain subcomponents features, get its attributes
#             if node.roles != []:   # skip objects that don't have SO_term or SBO_term
#                 SBO_term = node.roles[0][node.roles[0].find("SBO:") : ]
#                 SO_term = node.roles[0][node.roles[0].find("SO:") : ]

#                 if SO_term in renderer.renderer.glyph_term_map.keys():    # map SO_term to glyph type in parasbolv

#                     glyph_type = renderer.renderer.glyph_term_map[SO_term]

#                     part1 = dpl.Part(part_type= glyph_type , name= node.name, so_term= node.roles, orientation=None )
#                     part1_dict = part1.part_di()
#                     backbone1.append_part(part1_dict)
                
#                 if SBO_term in renderer.renderer.glyph_term_map.keys():    # map SBO_term to glyph type in parasbolv

#                     glyph_type = renderer.renderer.glyph_term_map[SBO_term]

#                     mol1 = dpl.MolecularSpecies(molecular_species_type= glyph_type, name= node.name, so_term=SBO_term)
#                     mol1_dict = mol1.molec_spec_append()
#                     print(f"Mol1 -> {mol1_dict}")
#                     molecules_list.append(mol1_dict)    

#         for feature in node.features:    # get attributes of subcomponents
#             print(f"Name: {feature.display_id}, roles: {feature.roles}, instance of: ") #{feature.instance_of} {feature.locations.property_owner}
            
#             if feature.roles == []:            # skip features that don't have SO_term
#                 continue
#             SO_term = feature.roles[0][feature.roles[0].find("SO:") : ]
#             if SO_term in renderer.renderer.glyph_term_map.keys():    # map SO_term to glyph type in parasbolv
#                 glyph_type = renderer.renderer.glyph_term_map[SO_term]

#                 part1 = dpl.Part(part_type= glyph_type , name= feature.name, so_term= feature.roles, orientation=feature.orientation)
#                 part1_dict = part1.part_di()
                
#                 backbone1.append_part(part1_dict)
            
#             dfs(feature)

#############################################################################
### Go through every component object in the doc and return its subcomponent using dfs function
for object in doc.objects:

    if not isinstance(object, sbol3.Component):    # iterate only through component objects
        continue
    if object not in renderer.visited:
        renderer.dfs(object)     # search for subcomponents to draw complete backbones (flatten the hierarichy)
        objects_list = []

        renderer.backbone_list.append(renderer.backbone1)
        renderer.backbone1 = dpl.Backbone(name='Omar backbone')

### Create biodesign to store backbones and molecular species inside
Bio1 = dpl.BioDesign("First BioDesign")
Bio1.add_moleculer(renderer.molecules_list)
print(Bio1.molecular_species[0])

### add backbones to the biodesign
for i in range(0, len(renderer.backbone_list)):
    if renderer.backbone_list[i].backbones == []:
        continue
    Bio1.add_backbone(renderer.backbone_list[i].backbones)
# print(f'Bio1 Backbones: {Bio1.backbones}')

### draw the biodesign
draw_dpl = dpl.Renderer().bio_render(Bio1)