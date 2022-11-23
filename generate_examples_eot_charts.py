# Test generate_star_chart functions
# python3 generate_examples_eot_charts.py
import matplotlib.pyplot as plt
import numpy as np
import muller_eot

if __name__ == '__main__':
	eccentricity_earth = 0.01671022
	obliquity_earth = 23.4367
	orbital_period_earth = 365.25696
	days_x = np.arange(1, 366, 1) # calculates based on midnight at start of UT day

	# Effect of Eccentricity
	eccentricity_y = muller_eot.calculateEffectEccentricity(eccentricity_earth, orbital_period_earth, days_x)
	muller_eot.plotEOT(days_x, eccentricity_y, "Eccentricity")

	# Effect of Obliquity
	obliquity_y = muller_eot.generateEffectObliquity(obliquity_earth, orbital_period_earth, days_x)
	muller_eot.plotEOT(days_x, obliquity_y, "Obliquity")

	# Combined Effect of Obliquity and Eccentricity
	eot_combined_y = muller_eot.calculateDifferenceEOTMinutes(eccentricity_earth, obliquity_earth, orbital_period_earth, days_x)
	muller_eot.plotEOT(days_x, eot_combined_y, "Obliquity and Eccentricity")
