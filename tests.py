import os

expected = "KhaAsbyBainDeanFifeWileBakerEllisEvansFoleyGlockGraffHeiglLundyMcVeyNylonPeeryReyesWhiteAdkinsBroomeHickeyLaymonRogersTantonTaylorByfieldDulaneyHagbergHillmanMcCraveMichaelPadgettRoutsonStarkeyStegmanBostwickCachedonGiddingsGuentherHatfieldKalivodaKirklandPhillipsReynoldsSullivanWilliamsClevengerFitzjerrellHendrickson"

def test_output_correct():
    os.system("cat Sort\ Me.txt | python3 sort.py")
    with open("sorted.txt",'r') as file:
        output = file.read().replace('\n','')
        output = output.replace(' ', '')
    assert output == expected
    print("test output passed")

test_output_correct()
