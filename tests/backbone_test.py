'''
test case for backbone class functions
'''

import dnaplotlib2 as dpl 

def test_backbone_append():
    '''
    functiont o test return function of backbone class
    '''
    part1 = dpl.Part('p','1','123','q')
    backbone1 = dpl.Backbone(name='test1')
    backbone1.append_part(part1.part_li())

    assert backbone1.return_backbone() == ['test1', [['p','1','123','q']]]
