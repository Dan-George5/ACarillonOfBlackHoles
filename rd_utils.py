import numpy
import bisect
from scipy.io import wavfile

class BHI(object):
	l2 = [[2,0,1.5251,-1.1568,0.1292,1.85,0.700,1.4187,-0.4990,0.88],
	[2,1,1.3673,-1.0260,0.1628,1.56,0.1000,0.5436,-0.4731,1.69],
	[2,2,1.3223,-1.0257,0.1860,1.91,-0.1000,0.4206,-0.4256,2.52],
	[1,0,0.6000,-0.2339,0.4175,2.03,-0.3000,2.3561,-0.2277,3.65],
	[1,1,0.5800,-0.2416,0.4708,2.40,-0.3300,0.951,-0.2072,3.18],
	[1,2,0.5660,-0.2740,0.4960,4.04,-0.1000,0.417,-0.2774,2.46],
	[0,0,0.4437,-0.0739,0.3350,1.04,4.0000,-1.9550,0.1420,2.63],
	[0,1,0.4185,-0.0768,0.4355,1.50,1.2500,-0.6359,0.1614,4.01],
	[0,2,0.3734,-0.0794,0.6306,2.72,0.5600,-0.2589,0.3034,4.33],
	[-1,0,0.3441,0.0293,2.0010,0.07,2.0000,0.1078,5.0069,2.82],
	[-1,1,0.3165,0.0301,2.3415,0.05,0.6100,0.0276,13.1683,0.67],
	[-1,2,0.2696,0.0315,2.7755,0.43,0.2900,0.0276,6.4715,2.40],
	[-2,0,0.2938,0.0782,1.3546,0.63,1.6700,0.4192,1.4700,0.71],
	[-2,1,0.2528,0.0921,1.3344,0.87,0.4550,0.1729,1.3617,0.79],
	[-2,2,0.1873,0.1117,1.3322,1.34,0.1850,0.1266,1.3661,1.16]]

	l3 = [[3,0,1.8956,-1.3043,0.1818,1.36,0.9000,2.3430,-0.4810,0.42],
	[3,1,1.8566,-1.2818,0.1934,1.35,0.2274,0.8173,-0.4731,0.88],
	[3,2,1.8004,-1.2558,0.2133,1.28,0.0400,0.5445,-0.4539,1.52],
	[2,0,1.1481,-0.5552,0.3002,1.09,0.8313,2.3773,-0.3655,1.28],
	[2,1,1.1226,-0.5471,0.3264,1.23,0.2300,0.8025,-0.3684,0.51],
	[2,2,1.0989,-0.5550,0.3569,1.41,0.1000,0.4804,-0.3784,0.81],
	[1,0,0.8345,-0.2405,0.4095,1.12,23.8450,-20.7240,0.03837,3.47],
	[1,1,0.8105,-0.2342,0.4660,1.55,8.8530,-7.8506,0.03418,3.64],
	[1,2,0.7684,-0.2252,0.5805,2.67,2.1800,-1.6273,0.1136,4.04],
	[0,0,0.6873,-0.09282,0.3479,0.83,6.7841,-3.6112,0.09480,3.99],
	[0,1,0.6687,-0.09155,0.4021,0.95,2.0075,-0.9930,0.12297,4.18],
	[0,2,0.6343,-0.08915,0.5117,1.28,0.9000,-0.3409,0.2679,2.89],
	[-1,0,0.5751,0.02508,3.1360,0.42,3.0464,0.1162,-0.2812,2.65],
	[-1,1,0.5584,0.02514,3.4154,0.42,1.2000,-0.1928,0.1037,2.75],
	[-1,2,0.5271,0.02561,3.8011,0.29,1.0000,-0.4424,0.02467,3.15],
	[-2,0,0.5158,0.08195,1.4084,0.35,2.9000,0.3356,2.3050,0.72],
	[-2,1,0.4951,0.08577,1.4269,0.41,0.9000,0.1295,1.6142,0.80],
	[-2,2,0.4567,0.09300,1.4469,0.53,0.4900,0.0848,1.9737,0.52],
	[-3,0,0.4673,0.1296,1.3255,0.61,2.5500,0.6576,1.3378,0.79],
	[-3,1,0.4413,0.1387,1.3178,0.68,0.7900,0.2381,1.3706,0.73],
	[-3,2,0.3933,0.1555,1.3037,0.82,0.4070,0.1637,1.3819,0.88]]

	l4 = [[4,0,2.3000,-1.5056,0.2244,1.83,1.1929,3.1191,-0.4825,0.37],
	[4,1,2.3000,-1.5173,0.2271,1.75,0.3000,1.1034,-0.4703,0.77],
	[4,2,2.3000,-1.5397,0.2321,1.61,0.1100,0.6997,-0.4607,0.10],
	[3,0,1.6869,-0.8862,0.2822,1.05,1.4812,2.8096,-0.4271,0.14],
	[3,1,1.6722,-0.8843,0.2923,1.10,0.4451,0.9569,-0.4250,0.37],
	[3,2,1.6526,-0.8888,0.3081,1.15,0.2200,0.5904,-0.4236,0.66],
	[2,0,1.2702,-0.4685,0.3835,1.11,-3.6000,7.7749,-0.1491,0.97],
	[2,1,1.2462,-0.4580,0.4139,1.39,-1.5000,2.8601,-0.1392,0.12],
	[2,2,1.2025,-0.4401,0.4769,2.26,-1.5000,2.2784,-0.1124,0.31],
	[1,0,1.0507,-0.2478,0.4348,0.97,14.0000,-9.8240,0.09047,0.81],
	[1,1,1.0337,-0.2439,0.4695,1.15,4.2000,-2.8399,0.1081,0.91],
	[1,2,1.0019,-0.2374,0.5397,1.53,2.2000,-1.4195,0.1372,0.53],
	[0,0,0.9175,-0.1144,0.3511,0.75,7.0000,-2.7934,0.1708,0.26],
	[0,1,0.9028,-0.1127,0.3843,0.82,2.2000,-0.8308,0.2023,0.26],
	[0,2,0.8751,-0.1096,0.4516,0.96,1.2000,-0.4159,0.2687,0.60],
	[-1,0,0.7908,0.02024,5.4628,0.96,4.6000,-0.4038,0.4629,2.52],
	[-1,1,0.7785,0.02005,5.8547,0.98,1.6000,-0.2323,0.2306,2.37],
	[-1,2,0.7549,0.01985,6.5272,0.96,1.6000,-0.8136,0.0316,2.32],
	[-2,0,0.7294,0.07842,1.5646,0.23,4.0000,0.2777,2.0647,2.11],
	[-2,1,0.7154,0.07979,1.5852,0.25,1.3200,0.08694,4.3255,0.75],
	[-2,2,0.6885,0.08259,1.6136,0.32,0.7500,0.05803,3.7971,0.66],
	[-3,0,0.6728,0.1338,1.3413,0.43,3.700,0.5829,1.6681,0.45],
	[-3,1,0.6562,0.1377,1.3456,0.46,1.1800,0.2111,1.4129,0.70],
	[-3,2,0.6244,0.1454,1.3513,0.52,0.6600,0.1385,1.3742,0.82],
	[-4,0,0.6256,0.1800,1.3218,0.62,3.4000,0.8696,1.4074,0.63],
	[-4,1,0.6061,0.1869,1.3168,0.67,1.0800,0.3095,1.3279,0.81],
	[-4,2,0.5686,0.2003,1.3068,0.74,0.5980,0.2015,1.3765,0.69]]

	G = 6.67408e-11
	c = 299792458.
	MS = 1.989e30
	SAMPLE_RATE = 44100

	def __init__(self):
		self.F1 = {} 
		self.F2 = {} 
		self.F3 = {} 
		self.Q1 = {} 
		self.Q2 = {} 
		self.Q3 = {} 
		for l, row in [(2, BHI.l2), (3, BHI.l3), (4, BHI.l4)]:
			for (m,n,f1,f2,f3,_,q1,q2,q3,_) in row:
				self.F1[(l,m,n)] = float(f1)
				self.F2[(l,m,n)] = float(f2)
				self.F3[(l,m,n)] = float(f3)
				self.Q1[(l,m,n)] = float(q1)
				self.Q2[(l,m,n)] = float(q2)
				self.Q3[(l,m,n)] = float(q3)

        def mass_given_F(self, j):
                mass = {}
                for (l,m,n) in self.F1:
                        mass[(l,m,n)] = 1. / (2. * numpy.pi * BHI.G * BHI.MS * 440 / BHI.c**3) * (self.F1[(l,m,n)] + self.F2[(l,m,n)] * (1.-j)**self.F3[(l,m,n)])
                return mass

	def f(self, M, j):
		out = {}
		for (l,m,n) in self.F1:
			out[(l,m,n)] = 1. / (2. * numpy.pi * BHI.G * M * BHI.MS / BHI.c**3) * (self.F1[(l,m,n)] + self.F2[(l,m,n)] * (1.-j)**self.F3[(l,m,n)])
		return out


	def Q(self, j):
		out = {}
		for (l,m,n) in self.Q1:
			out[(l,m,n)] = self.Q1[(l,m,n)] + self.Q2[(l,m,n)] * (1.-j)**self.Q3[(l,m,n)]
		return out


	def ordered_spectrum(self, M, j, modes = None):
		out = ()
		if modes is None:
			modes = self.modes
		thisf = self.f(M,j)
		thisQ = self.Q(j)
		return sorted(zip( [thisf[m] for m in modes], [thisQ[m] for m in modes], modes))
		
	@property
	def bell_modes(self):
		return sorted([k for (k,v) in self.Q3.items() if v <= 0.0])


	@property
	def drum_modes(self):
		return sorted(list(set(self.Q3) - set(self.bell_modes)))


	@property
	def modes(self):
		return self.Q3.keys()


	def perfect_bell(self, j, minQ = 100):
		"""
		Return the most bell like 5 modes.  These modes have
		frequency ratios of:

		2**(0/12.) = 1
		2**(12/12.) = 2
		2**(15/12.) = 2.378 
		2**(19/12.) = 2.997 
		2**(24/12.) = 4.0
		"""
		bell_candidates = []
		modes_to_consider = [x for x in self.ordered_spectrum(10,j) if x[1] >= minQ]
		for to_process in [modes_to_consider[n:] for n, row in enumerate(modes_to_consider)]:
			freqs = numpy.array([f[0] for f in to_process])
			freqs /= freqs[0]
			# check if we have enough data, otherwise move on
			if len(freqs) < 5:
				continue
			closest = [to_process[0]]
			accuracy = []
			# we set the first frequency to be "1" so we only check the other ratios
			for bf in numpy.array([2., 2.378, 2.997, 4.]):
				closest_after = bisect.bisect_left(freqs, bf)
				accuracya = float('inf') if closest_after >= len(freqs) else abs(bf-freqs[closest_after]) / bf
				accuracyb = abs(bf-freqs[closest_after-1]) / bf
				
				if accuracyb < accuracya:
					accuracy.append(accuracyb)
					closest.append(to_process[closest_after-1])
				else:
					accuracy.append(accuracya)
					closest.append(to_process[closest_after])
			# take the worst case scenario.
			accuracy = numpy.max(accuracy)
			bell_candidates.append((accuracy, closest))
			
		bell_candidates.sort()
		for bell in bell_candidates:
			modes = tuple(set([f[2] for f in bell[1]]))
			f_ratios = tuple(f[0] for f in bell[1])
			accuracy = bell[0]
			# just pick the first one with the correct number of distinct modes
			if len(modes) == 5:
				return modes, accuracy, f_ratios
		return None, None, None

	def perfect_drum(self, j, minQ = 5):
		"""
		Return the most drum like 5 modes.  These modes have
		frequency ratios of:

		2**(0/12.) = 1
		2**(12/12.) = 1.59
		2**(15/12.) = 2.14 
		2**(19/12.) = 2.30 
		2**(24/12.) = 2.65
		"""
		drum_candidates = []
                #Included restriction of Q < 100
		modes_to_consider = [x for x in self.ordered_spectrum(10,j) if x[1] >= minQ and x[1] <= 100]
		for to_process in [modes_to_consider[n:] for n, row in enumerate(modes_to_consider)]:
			freqs = numpy.array([f[0] for f in to_process])
			freqs /= freqs[0]
			# check if we have enough data, otherwise move on
			if len(freqs) < 5:
				continue
			closest = [to_process[0]]
			accuracy = []
			# we set the first frequency to be "1" so we only check the other ratios
			for bf in numpy.array([1.59, 2.14, 2.3, 2.65]):
				closest_after = bisect.bisect_left(freqs, bf)
				accuracya = float('inf') if closest_after >= len(freqs) else abs(bf-freqs[closest_after]) / bf
				accuracyb = abs(bf-freqs[closest_after-1]) / bf
				
				if accuracyb < accuracya:
					accuracy.append(accuracyb)
					closest.append(to_process[closest_after-1])
				else:
					accuracy.append(accuracya)
					closest.append(to_process[closest_after])
			# take the worst case scenario.
			accuracy = numpy.max(accuracy)
			drum_candidates.append((accuracy, closest))
			
		drum_candidates.sort()
		for drum in drum_candidates:
			modes = tuple(set([f[2] for f in drum[1]]))
			f_ratios = tuple(f[0] for f in drum[1])
			accuracy = drum[0]
			# just pick the first one with the correct number of distinct modes
			if len(modes) == 5:
				return modes, accuracy, f_ratios
		return None, None, None



	def waveform(self, A, key, j, MAX_DURATION = 5.0):
		def _key_to_f(key):
			return 2**((key-49)/12.) * 440.

		# compute the maximum time constant to determine the duration of this waveform
		tQ = self.Q(j)
		max_mode = sorted([(v,tQ[k],k) for k,v in A.items()])[-1][2]
		# just use an arbitrary mass for now M = 10
		tf = self.f(10, j)
		# Renormalize to the right piano key
		freq_factor = _key_to_f(key) / tf[max_mode]
		print "effective mass: ", 10. / freq_factor
		for mode in tf:
			tf[mode] *= freq_factor
		
		duration = min(10 * max([tQ[m] / numpy.pi / tf[m] for m in A if A[m] != 0]), MAX_DURATION)
		t = numpy.linspace(0, numpy.ceil(duration), numpy.ceil(duration) * BHI.SAMPLE_RATE)
		out = numpy.zeros(len(t))
		for (l,m,n) in A:
			this_mode = numpy.exp(-numpy.pi * tf[l,m,n] * t / tQ[l,m,n]) * numpy.sin(2 * numpy.pi * tf[l,m,n] * t)
			this_mode /= sum(this_mode**2)**.5
			out += A[l,m,n] * this_mode
	
		return t, out


	def to_wave_file(self, t, w, fname = "BHI.wav"):
		w = numpy.copy(w)
		out = numpy.zeros(len(w), numpy.float32)
		out[:] = w[:] / max(w)
		wavfile.write(fname, BHI.SAMPLE_RATE, out)

