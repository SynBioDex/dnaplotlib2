'''
test case for backbone class functions
'''

import dnaplotlib2 as dpl 

def test_backbone_append():
    '''
    functiont to test return function of backbone class
    '''
    part1 = dpl.Part('p','1','123','q')
    backbone1 = dpl.Backbone(name='test1')
    backbone1.append_part(part1.part_li())
    output = ['test1', [['p','1','123','q']]]
    assert backbone1.backbones_list == output
