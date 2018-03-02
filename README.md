# A Carillon Of Black Holes
Create your own black hole instrument with the help of gravitational waves! 

Much like a bell emits sound waves when tapped; black holes emit gravitational waves that propagate through spacetime when perturbed. In his theory of General Relativity (GR), Einstein showed that spacetime is curved around massive objects. This curvature is what allows the moon to orbit the earth, our planets to orbit the sun, and so on. Within this theory, he predicted the existence of gravitational waves that are caused by many violent astrophysical events, including the inspiral of a binary black hole system. Around a 100 years after GR was formulated, a scientific collaboration named LIGO (Laser Interferometer Gravitational-Wave Observatory) detected gravitational-waves emitted from a binary black hole system which merged around 1.3 billion years ago. This detection, along with several more recent ones have provided us with a new window into our Universe. The gravitational waves emitted from some black hole binary systems are emitted at a frequency that is within our ears' hearing range. Thus, we can, in a nutshell, now listen to our universe with the help of gravitational waves.

In this project, we provide software that utilizes the solutions to Einstein's field equations that allows one to hear what black holes with extremely high spin sound like when something falls in. The signal that we would receive from these black holes is (approximately) what we call the strain (h). We can now decompose this signal into a summation of vector functions that encode information about the excited modes

<a href="http://www.codecogs.com/eqnedit.php?latex=h(t)&space;=&space;\sum_{n=0}^2\sum_{l=2}^4\sum_{m=-l}^l&space;A_{lmn}&space;e^{-\pi&space;f_{lmn}/Q_{lmn}}\sin({2\pi&space;f_{lmn}t})" target="_blank"><img src="http://latex.codecogs.com/gif.latex?h(t)&space;=&space;\sum_{n=0}^2\sum_{l=2}^4\sum_{m=-l}^l&space;A_{lmn}&space;e^{-\pi&space;f_{lmn}/Q_{lmn}}\sin({2\pi&space;f_{lmn}t})" title="h(t) = \sum_{n=0}^2\sum_{l=2}^4\sum_{m=-l}^l A_{lmn} e^{-\pi f_{lmn}/Q_{lmn}}\sin({2\pi f_{lmn}t})" /></a>.

While the theory behind this is long and complex, we wish to distill it into saying that it is the manner in which a black hole is perturbed that lends to how much of each mode is excited. By changing the amplitude of each mode, you essentially change how the black hole is perturbed, and thus leads to a different kind of sound. You can do this by editing the right column of the defaul_amp.txt file. Let us know if you find some cool sounds!

## How to run

Here, we provide you with the tools to simulate your own array of 88 black holes. You can choose which modes are to be excited by editing, or adding your own amp.txt file. You can also increase the spin of the black holes to create longer-ringing sounds.

NOTE: Make sure you have Python 2 installed, with all dependent libraries listed in instrument_creator and rd_utils. 

On terminal, enter

$ ./instrument_creator 

to create 88 WAV files based on the pre-set amplitudes and spin. You can change the spin of every black hole by running

$ ./instrument_creator -s 0.9999

Replace 0.9999 by any spin value 0 < spin < 1. Using a spin equal to, or greater than 1 will result in an error as such a black hole is unstable. Please also be cautioned into using spins > 0.998 as this results in a black hole that is not astrophysical.
