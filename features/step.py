from lettuce import *
from nose.tools import assert_equals
from f2w import f2w

@step(u'I have a wavelength of (\d+\.\d+)')
def test_frequence(step, wf):
    world.number = float(wf)

@step('I compute the frequence')
def calc_frequence(step):
    world.number = float(f2w.w2f(world.number))
        
    
@step('I receive (\d+\.\d+)')
def receive(step,result):
    assert_equals(world.number, float(result))

@step(u'I have a frequence of (\d+\.\d+)')
def test_wavelength(step, wf):
    world.number = float(wf)

@step('I compute the wavelength')
def calc_frequence(step):
    world.number = float(f2w.f2w(world.number))
