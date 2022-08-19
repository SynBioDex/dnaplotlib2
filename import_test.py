from DNAplotlib2.dnaplotlib2 import Backbone, Part

def test_backbone_append():
    part2 = Part('p','1','123','q')
    backbone2 = Backbone(name='test2')
    backbone2.append_part(part2.part_li())

    # backbone1 = Backbone(name='test1')
    # backbone1.append_part(Part('p',1,'123','q'))
    assert backbone2.return_backbone() == ['test2', [['p','1','123','q']]]