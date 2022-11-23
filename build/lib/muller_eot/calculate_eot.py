import matplotlib.pyplot as plt
import math
import numpy as np

import muller_eot 

# EOT:
# Equation of Time = (apparent solar time) - (mean solar time)

# Effect of Eccentricity:
# R = true anomaly: angle covered by Earth after leaving perihelion
# M = mean anomaly: mean earth would cover an angle (called mean anomaly) in the same period of time as true earth covers the angle R
# T = One year: revolution lasts on year
# t = time span after passaage through the perihelion
# M = 2pi * (t/T) ==> mean anomaly = (time span since perhelion / total time) in radians
# E = (angle) eccentric anomaly: used to calculate the area of elliptic sectors
# e = eccentricity of Earth = 0.0167

def calculateDifferenceEOTMinutes(eccentricity, obliquity_deg, orbit_period):
	perihelion_day = muller_eot.calculatePerihelionDay()
	distance_between_solistice_perhelion_deg = muller_eot.calculateDistanceBetweenSolisticePerhelion()
	distance_between_solistice_perhelion_rad = np.deg2rad(distance_between_solistice_perhelion_deg)
	obliquity_rad = np.deg2rad(obliquity_deg)

	# Equation [45]
	t1 = (obliquity_rad/2)*(1-4*pow(eccentricity, 2))
	tan2_1_4e2 = (1-math.cos(2*t1)) / (1+math.cos(2*t1))
	tan2 = (1-math.cos(obliquity_rad)) / (1+math.cos(obliquity_rad))

	e2 = 2*eccentricity
	tan2_2e = 2 * eccentricity * tan2
	tan4_1_2 = (1/2)*pow(tan2, 2)

	e2_5_4 = (5/4)*(pow(eccentricity, 2))
	tan4_2e = 2 * eccentricity * pow(tan2, 2)
	tan2_2e_13_4 = (13/4)*(pow(eccentricity, 2))*tan2
	tan6_1_3 = (1/3)*pow(tan2, 3)

	minutes_conversion = (24 * 60) / (2 * math.pi)
	orbit_days_x = np.arange(1, round(orbit_period), 1)
	eot_mins = []
	for d in orbit_days_x:
		m = 2*math.pi*((d - perihelion_day)/orbit_period)
		a = tan2_1_4e2*math.sin(2*(m+distance_between_solistice_perhelion_rad))+e2*math.sin(m)
		b = tan2_2e*math.sin(m+2*distance_between_solistice_perhelion_rad)+tan2_2e*math.sin(3*m+2*distance_between_solistice_perhelion_rad)
		c = tan4_1_2*math.sin(4*(m+distance_between_solistice_perhelion_rad))+e2_5_4*math.sin(2*m)-tan4_2e*math.sin((3*m)+(4*distance_between_solistice_perhelion_rad))
		d = tan4_2e*math.sin((5*m)+(4*distance_between_solistice_perhelion_rad))+tan2_2e_13_4*math.sin(4*m+2*distance_between_solistice_perhelion_rad)
		e = tan6_1_3*math.sin(6*(m+distance_between_solistice_perhelion_rad))
		eot_mins.append(-( a - b + c + d + e)*minutes_conversion)

	return eot_mins

def calculateEffectEccentricity(eccentricity, orbit_period):
	eot_eccentricty_mins =  calculateDifferenceEOTMinutes(eccentricity, 0, orbit_period)
	return eot_eccentricty_mins

def generateEffectObliquity(obliquity, orbit_period):
	eot_obliquity_mins = calculateDifferenceEOTMinutes(0, obliquity, orbit_period)
	return eot_obliquity_mins

def plotEOT(planet_name, orbital_period, eot_y, variation_type):
	fig = plt.figure(figsize=(12,12), dpi=120)

	# X - Axis, split by months
	orbit_days_x = np.arange(1, round(orbital_period), 1)
	date_range_split_into_months = np.arange(0, round(orbital_period)+1, orbital_period/12) # split into 12 months (based on Earth)
	for i, value in enumerate(date_range_split_into_months): date_range_split_into_months[i] = math.floor(value) # round all values
	
	plt.xticks(date_range_split_into_months)
	plt.scatter(orbit_days_x, eot_y)
	plt.grid()
	plt.title("{0}: Effect of {1} (Min = {2:.4f}, Max = {3:.4f})".format(planet_name, variation_type, min(eot_y), max(eot_y)))
	plt.xlabel("Days in the Sidereal Year")
	plt.ylabel("Time Difference (Minutes)")
	plt.show()
