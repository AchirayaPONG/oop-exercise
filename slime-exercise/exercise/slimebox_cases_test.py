import hashlib
import pytest
from slimebox import Slime, Color, clamp, mix_colors
import sim

def test_case2(capsys):
    sim.main('case2.input')
    captured = capsys.readouterr()
    assert hashlib.sha256(captured.out.strip().encode('utf_8')).hexdigest() == 'e3db407a9099d5f8d608ef40af14f5ca16cccf332c93150d03ac3d041747d860'

def test_case3(capsys):
    sim.main('case3.input')
    captured = capsys.readouterr()
    assert hashlib.sha256(captured.out.strip().encode('utf_8')).hexdigest() == 'b2aca59de7e9a20948a3a3d173fc6097f0b1d744ccb7fedbd8600d351257178c'


