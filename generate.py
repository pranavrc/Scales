import populate
import sound
import random

populate._listen_(27.5, 5000, 1.059463094, 21)
_beats_ = 4
_intervalLength_ = random.choice(range(1,5))*1000
_interval_ = 0
_noteLength_ = random.choice([500,1000,2000,3000,4000,5000])
_barLength_ = _beats_ * (_intervalLength_ + _noteLength_)
_CmajorArpeggio_ = ['C3','E3','G3','B3']
_note_ = []


for base in range(1, _beats_+1):
	_note_.append(random.choice(_CmajorArpeggio_))

for repeat in range(1,3):
	for base in range(1, _beats_+1):
		sound._play_("foo.au", populate._freq_[_note_[base-1]], _noteLength_, 1, 'ab')
		sound._play_("foo.au", 0, _interval_, 1, 'ab')

