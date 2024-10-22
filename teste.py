from cifrarMsg import *
from decifrarMsg import *

msgc = cifrarMsg('./chaveJonasPub.txt', 'bom dia')

decifrarMsg('./chaveJonasPri.txt', msgc)