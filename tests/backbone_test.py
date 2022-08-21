# import sys
# sys.path.append("../DNAplotlib2")

from dnaplotlib2 import Backbone, Part

def test_backbone_append():
    part1 = Part('p','1','123','q')
    backbone1 = Backbone(name='test1')
    backbone1.append_part(part1.part_li())

    # backbone2 = Backbone(name='test2')
    # backbone2.append_part(Part('a',1,'12233','qee'))
    assert backbone1.return_backbone() == ['test1', [['p','1','123','q']]]


