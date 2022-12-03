import matplotlib.pyplot as plt
import math
import numpy as np

import muller_eot 

# EQUATION OF TIME - PROBLEM IN ASTRONOMY
# M. Müller
# Gymnasium Münchenstein, Grellingerstrasse 5,
# 4142 Münchenstein, Switzerland
# This paper was awarded in the II International Competition (1993/94) ”First Step to Nobel Prize in Physics” and published in the competition proceedings (Acta Phys. Pol. A 88 Supplement, S-49 (1995))

# EOT:
# Equation of Time = (apparent solar time) - (mean solar time)
# Equation of Time = "True Equatorial Sun Angle" - "Mean Equatorial Sun Angle" (Geocentric View) - (True Projected Anomaly - Mean anomaly) (heliocentric view)
# Equation of Time = M - R^P

# Effect of Eccentricity and Obliquity:
# R = true anomaly: angle covered by Earth after leaving perihelion
# M = mean anomaly: mean earth would cover an angle (called mean anomaly) in the same period of time as true earth covers the angle R
# T = One year: revolution lasts on year
# t = time span after passaage through the perihelion
# M = 2pi * (t/T) ==> mean anomaly = (time span since perhelion / total time) in radians
# E = (angle) eccentric anomaly: used to calculate the area of elliptic sectors
# e = eccentricity of Earth = 0.0167
# ε = obliquity of Earth = 23.45◦

def calculateDifferenceEOTMinutes(eccentricity=None,
								obliquity_deg=None,
								orbit_period=None):
	# Calculate the time difference (in minutes) for the Equation of Time

	muller_eot.errorHandlingEOT(eccentricity,
								obliquity_deg,
								orbit_period) # Verify argument behavior

	distance_between_solistice_perhelion_deg = muller_eot.calculateDistanceBetweenSolisticePerhelion()
	distance_between_solistice_perhelion_rad = np.deg2rad(distance_between_solistice_perhelion_deg)

	obliquity_rad = np.deg2rad(obliquity_deg)

	minutes_conversion = (24 * 60) / (2 * math.pi)
	perihelion_day = muller_eot.calculatePerihelionDay()

	eot_mins = []
	orbit_days_x = np.arange(1, round(orbit_period), 1)

	# Equation [45], page 11: expansion of sine function yields:
	for day in orbit_days_x:
		mean_anomaly = 2 * math.pi * ((day - perihelion_day) / orbit_period) # M from [2]
		tan2 = (1 - math.cos(obliquity_rad)) / (1 + math.cos(obliquity_rad)) # tan2(ε/2)

		# M + tan2(ε/2)(1 − 4e^2)*sin2(M + P) + 2 * e * sin(M)
		t1 = (obliquity_rad / 2) * (1 - 4 * pow(eccentricity, 2))
		tan2_1_4e2 = (1 - math.cos(2 * t1)) / (1 + math.cos(2 * t1)) # tan2(ε/2)(1 − 4e^2)
		sin2_m_p = math.sin(2 * (mean_anomaly + distance_between_solistice_perhelion_rad)) # sin2(M + P)
		e2_sin_m = (2 * eccentricity) * math.sin(mean_anomaly) # 2 * e * sin(M)
		line_one = tan2_1_4e2 * sin2_m_p + e2_sin_m

		# -2etan2(ε/2) * sin(M + 2P) + 2 * e * tan2(ε/2) * sin(3M + 2P)
		neg_tan2_2e = -(2 * eccentricity * tan2) # -2etan2(ε/2)
		sin_m_2p = math.sin(mean_anomaly + (2 * distance_between_solistice_perhelion_rad))  # sin(M + 2P)
		tan2_e_2 = 2 * eccentricity * tan2 # 2 * e * tan2(ε/2)
		sin_3m_2p = math.sin((3 * mean_anomaly) + (2 * distance_between_solistice_perhelion_rad)) # sin(3M + 2P)
		line_two = neg_tan2_2e * sin_m_2p + tan2_e_2 * sin_3m_2p

		# 1/2 tan4(ε/2) * sin4(M + P) + (5/4) * e^2 * sin(2m) - 2 * e * tan4(ε/2) * sin(3M + 4P)
		tan4_1_2 = (1/2) * pow(tan2, 2) # 1/2 tan4(ε/2)
		sin4_m_p = math.sin(4 * (mean_anomaly + distance_between_solistice_perhelion_rad)) # sin4(M + P)
		e2_5_4 = ((5/4) * pow(eccentricity, 2)) # (5/4) * e^2
		sin2m = math.sin(2 * mean_anomaly) # sin(2m)
		tan4_2e = 2 * eccentricity * pow(tan2, 2) # 2 * e * tan4(ε/2)
		sin_3m_4p = math.sin((3 * mean_anomaly)+(4 * distance_between_solistice_perhelion_rad)) # sin(3M + 4P)
		line_three = tan4_1_2 * sin4_m_p + e2_5_4 * sin2m - tan4_2e * sin_3m_4p

		# 2 * e * tan4(ε/2) * sin(5M + 4P) + (13/4) * e^2 * tan2(ε/2) * sin(4M + 2P)
		tan4_2e = 2 * eccentricity * pow(tan2, 2) # 2 * e * tan4(ε/2)
		sin_5m_4p = math.sin((5 * mean_anomaly)+(4 * distance_between_solistice_perhelion_rad))  # sin(5M + 4P)
		tan2_2e_13_4 = (13/4) * (pow(eccentricity, 2)) * tan2 # (13/4) * e^2 * tan2(ε/2)
		sin_4m_2p = math.sin(4 * mean_anomaly + 2 * distance_between_solistice_perhelion_rad) # sin(4M + 2P)
		line_four = tan4_2e * sin_5m_4p + tan2_2e_13_4 * sin_4m_2p

		# 1/3 * tan6(ε/2) * sin6(M + P)
		tan6_1_3 = (1/3) * pow(tan2, 3) # 1/3 * tan6(ε/2)
		sin6_m_p = math.sin(6 * (mean_anomaly + distance_between_solistice_perhelion_rad)) # sin6(M + P)
		line_five = tan6_1_3 * sin6_m_p

		eot_mins.append(-( line_one + line_two + line_three + line_four + line_five)*minutes_conversion)
	return eot_mins

def plotEOT(planet_name=None,
			orbital_period=None,
			eot_y=[],
			effect_title_str=None,
			plot_title=None,
			plot_x_title=None,
			plot_y_title=None,
			showPlot=True,
			figsize_n=12,
			figsize_dpi=100,
			save_plot_name=None):
	# Plot EOT Time Differences

	muller_eot.errorHandlingPlotEOT(planet_name,
									orbital_period,
									eot_y,
									effect_title_str,
									plot_title,
									plot_x_title,
									plot_y_title,
									showPlot,
									figsize_n,
									figsize_dpi,
									save_plot_name) # Verify argument behavior

	fig = plt.figure(figsize=(figsize_n,figsize_n), dpi=figsize_dpi)

	# X - Axis, split by months
	orbit_days_x = np.arange(1, round(orbital_period), 1)
	date_range_split_into_months = np.arange(0, round(orbital_period)+1, orbital_period/12) # split into 12 months (based on Earth)
	for i, value in enumerate(date_range_split_into_months): date_range_split_into_months[i] = math.floor(value) # round all values
	
	plt.xticks(date_range_split_into_months)
	plt.xlim([min(date_range_split_into_months), max(date_range_split_into_months)])
	plt.scatter(orbit_days_x, eot_y)
	plt.grid()

	if plot_title is None: plt.title("{0}: Effect of {1} (Min = {2:.4f}, Max = {3:.4f})".format(planet_name, effect_title_str, min(eot_y), max(eot_y)))
	else: plt.title(plot_title)

	if plot_x_title is None: plt.xlabel("Days in the Sidereal Year")
	else: plt.xlabel(plot_x_title)

	if plot_y_title is None: plt.ylabel("Time Difference (Minutes)")
	else: plt.ylabel(plot_y_title)

	if showPlot:
		plt.show()

	if save_plot_name:
		fig.savefig(save_plot_name)
