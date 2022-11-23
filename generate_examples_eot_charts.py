# Test generate_star_chart functions
# python3 generate_examples_eot_charts.py
import matplotlib.pyplot as plt
import math
import numpy as np
import muller_eot

if __name__ == '__main__':
	obliquity_earth = 23.4367
	semimajor_axis_earth = 1.0000001124 # (AU)

	orbit_period_earth = muller_eot.calculateOrbitalPeriod(semimajor_axis_earth)

	eccentricity_earth = 0.01671022
	#eccentricity_earth = muller_eot.calculateEccentricity(aphelion_distance_earth, perihelion_distance_earth)

	# Effect of Eccentricity
	eccentricity_y = muller_eot.calculateEffectEccentricity(eccentricity_earth, orbit_period_earth)
	muller_eot.plotEOT(orbit_period_earth, eccentricity_y, "Eccentricity")

	# Effect of Obliquity
	obliquity_y = muller_eot.generateEffectObliquity(obliquity_earth, orbit_period_earth)
	muller_eot.plotEOT(orbit_period_earth, obliquity_y, "Obliquity")

	# Combined Effect of Obliquity and Eccentricity
	eot_combined_y = muller_eot.calculateDifferenceEOTMinutes(eccentricity_earth, obliquity_earth, orbit_period_earth)
	muller_eot.plotEOT(orbit_period_earth, eot_combined_y, "Obliquity and Eccentricity")
