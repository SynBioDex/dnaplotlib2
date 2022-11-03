import dnaplotlib2 as dpl
import sbol3

# create document to read sbol file
docu = sbol3.Document()
docu.read("gfp.nt")
# print(f"doc lenght -> {docu.objects[1].features.display_id}")

# create renderer to draw components
renderer  = dpl.Renderer()

def get_components(doc, index = -1):

    if index >= 0 and index <= len(doc.objects):
        if isinstance(doc.objects[index-1], sbol3.Component):    # iterate only through component objects
            renderer.dfs(doc.objects[index-1])     # search for subcomponents to draw complete backbones (flatten the hierarichy)
            renderer.backbone_list.append(renderer.backbone1)
            renderer.backbone1 = dpl.Backbone(name='Omar backbone')
    else:   
        # Go through every component object in the doc and return its subcomponent using dfs function
        for object in doc.objects:
            # print(f'Function works _>>>>>>>>>>>>>>> {len(doc.objects)}')
            if not isinstance(object, sbol3.Component):    # iterate only through component objects
                continue
            if object not in renderer.visited:
                renderer.dfs(object)     # search for subcomponents to draw complete backbones (flatten the hierarichy)
                renderer.backbone_list.append(renderer.backbone1)
                renderer.backbone1 = dpl.Backbone(name='Omar backbone')

get_components(docu) ## how to call this function from class Renderer???

### Create biodesign to store backbones and molecular species inside
Bio1 = dpl.BioDesign("First BioDesign")
Bio1.add_moleculer(renderer.molecules_list)

### add backbones to the biodesign
for i in range(0, len(renderer.backbone_list)):
    if renderer.backbone_list[i].backbones == []:
        continue
    Bio1.add_backbone(renderer.backbone_list[i].backbones)

### draw the biodesign
draw_dpl = dpl.Renderer().bio_render(Bio1)