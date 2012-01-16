from struct import pack
from math import sin, pi
import time
from populate import _listen_

def _play_(name, freq, dur, vol, mode='ab'):
    _dump_ = open(name, mode)
    _dump_.write('.snd' + pack('>5L', 24, 8*dur, 2, 8000, 1))
    _factor_ = 2 * pi * freq/8000
    for count in range(8 * dur):
        _wave_ = sin(count * _factor_)
        _dump_.write(pack('b', vol * 64 * _wave_))
    _dump_.close()

if __name__=="__main__":
	_play_("foo.au", 50, 1000, 1, 'ab')
	
