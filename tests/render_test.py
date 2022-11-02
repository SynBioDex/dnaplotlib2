'''
test case for render class functions
'''

import dnaplotlib2 as dpl

# def test_render():
#     '''
#     '''

    

#      assert 


def test_sort_backbones():
    '''
    
    '''
    b1_part1 = dpl.Part(part_type="Promoter", orientation = None, so_term=['https://identifiers.org/SO:0000167'], name='Promoter 1',   start_range=1, end_range= None)
    b1_part1_dict = b1_part1.part_di()

    b1_part2 = dpl.Part(part_type="Recombination Site", orientation=None , so_term=['https://identifiers.org/SO:0000139'], name='RBS 1',  start_range=2, end_range= None)
    b1_part2_dict = b1_part2.part_di()

    b1_part3 = dpl.Part(part_type="CDS", orientation=None , so_term=['https://identifiers.org/SO:0000316'], name='GFP 1',  start_range=3, end_range= None)
    b1_part3_dict = b1_part3.part_di()

    b1_part4 = dpl.Part(part_type="Terminator", orientation=None , so_term=['https://identifiers.org/SO:0000141'], name='Terminator 1',  start_range=4, end_range= None)
    b1_part4_dict = b1_part4.part_di()


    backbone1 = dpl.Backbone(name="Backbone 1")
    backbone1.append_part(b1_part1_dict)
    backbone1.append_part(b1_part2_dict)
    backbone1.append_part(b1_part3_dict)
    backbone1.append_part(b1_part4_dict)

    Bio1 = dpl.BioDesign("First BioDesign")
    Bio1.add_backbone(backbone1.backbones)

    draw_dpl = dpl.Renderer().bio_render(Bio1)


    assert print(dpl.Renderer.biodesign.backbones) == print(Bio1.backbones)
