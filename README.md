# A Carillon Of Black Holes
Create your own black hole instrument with the help of gravitational waves!

Much like a bell emits sound waves when tapped; black holes emit gravitational waves when perturbed. Previously, we have not been able to observe black holes due to the strong gravitational fields not allowing light to escape. In his theory of General Relativity, Einstein predicted the existence of gravitational waves. Around a 100 years later, a scientific collaboration named LIGO (Laser Interferometer Gravitational-Wave Observatory) proved this prediction by detecting gravitational-waves emitted from a binary black hole system that merged around 1.3 billion years ago.

<a href="http://www.codecogs.com/eqnedit.php?latex=h(t)&space;=&space;\sum_{n=0}^2\sum_{l=2}^4\sum_{m=-l}^l&space;A_{lmn}&space;e^{-\pi&space;f_{lmn}/Q_{lmn}}\sin({2\pi&space;f_{lmn}t})" target="_blank"><img src="http://latex.codecogs.com/gif.latex?h(t)&space;=&space;\sum_{n=0}^2\sum_{l=2}^4\sum_{m=-l}^l&space;A_{lmn}&space;e^{-\pi&space;f_{lmn}/Q_{lmn}}\sin({2\pi&space;f_{lmn}t})" title="h(t) = \sum_{n=0}^2\sum_{l=2}^4\sum_{m=-l}^l A_{lmn} e^{-\pi f_{lmn}/Q_{lmn}}\sin({2\pi f_{lmn}t})" /></a>

## How to run

Here, we provide you with the tools to simulate your own array of 88 black holes. You can choose which modes are to be excited by editing, or adding your own amp.txt file. You can also change the spin of the black holes to create different kind of sounds

$ ./instrument_creator 

creates 88 WAV files based on the pre-set amplitudes and spin. You can change the spin by running

$ ./instrument_creator -s 0.9999

replace 0.999 by any spin value 0 < spin < 1. Using a spin equal to, or greater than 1 will result in an error (i.e. your black hole being torn apart)
