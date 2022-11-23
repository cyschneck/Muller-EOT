import matplotlib.pyplot as plt
import math
import numpy as np

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

def calculateOrbitalPeriod(semimajor_axis):
	# caculate orbital period (days): P**2 = a**2 where P=period and a = semimajor axis
	# return a list of days starting at midnight
	sidereal_year = pow(semimajor_axis, 3/2)
	orbital_period_days = sidereal_year * 365.25
	return orbital_period_days

def calculateEccentricity(aphelion_distance, perihelion_distance):
	# caclulate the eccentricity of orbit based on orbit
	eccentricity_orbit = (aphelion_distance - perihelion_distance) / (aphelion_distance + perihelion_distance)
	return eccentricity_orbit

def calculatePerihelionDay():
	 # calendar day of perihelion (ranges from 3 to 5th)
	## TODO
	day_of_perhelion = 5.325 # 2020   
	return day_of_perhelion    

def calculateDistanceBetweenSolisticePerhelion():
	# angle covered by the Earth between the begnning of Winer (21st December) and the arrival of the Earth at perihelion (2nd January)
	## TODO
	distance_between_solistice_perhelion_deg = 14.40 # 2020
	return distance_between_solistice_perhelion_deg

def calculateDifferenceEOTMinutes(eccentricity, obliquity_deg, orbit_period):
	distance_between_solistice_perhelion_deg = calculateDistanceBetweenSolisticePerhelion()
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

	time_mins = (24 * 60) / (2 * math.pi)
	eot_mins = []
	perihelion_day = calculatePerihelionDay()
	orbit_days_x = np.arange(1, round(orbit_period), 1)
	for d in orbit_days_x:
		m = 2*math.pi*((d - perihelion_day)/orbit_period)
		a = tan2_1_4e2*math.sin(2*(m+distance_between_solistice_perhelion_rad))+e2*math.sin(m)
		b = tan2_2e*math.sin(m+2*distance_between_solistice_perhelion_rad)+tan2_2e*math.sin(3*m+2*distance_between_solistice_perhelion_rad)
		c = tan4_1_2*math.sin(4*(m+distance_between_solistice_perhelion_rad))+e2_5_4*math.sin(2*m)-tan4_2e*math.sin((3*m)+(4*distance_between_solistice_perhelion_rad))
		d = tan4_2e*math.sin((5*m)+(4*distance_between_solistice_perhelion_rad))+tan2_2e_13_4*math.sin(4*m+2*distance_between_solistice_perhelion_rad)
		e = tan6_1_3*math.sin(6*(m+distance_between_solistice_perhelion_rad))
		eot_mins.append(-( a - b + c + d + e)*time_mins)

	return eot_mins

def calculateEffectEccentricity(eccentricity, orbit_period):
	eot_eccentricty_mins =  calculateDifferenceEOTMinutes(eccentricity, 0, orbit_period)
	return eot_eccentricty_mins

def generateEffectObliquity(obliquity, orbit_period):
	eot_obliquity_mins = calculateDifferenceEOTMinutes(0, obliquity, orbit_period)
	return eot_obliquity_mins

def plotEOT(orbital_period_x, eot_y, title_plot):
	fig = plt.figure(figsize=(12,12), dpi=120)
	orbital_period_days_lst = np.arange(1, round(orbital_period_x), 1)
	plt.scatter(orbital_period_days_lst, eot_y)
	plt.grid()
	plt.title("Equation of Time - Difference in Minutes, due to {0}".format(title_plot))
	plt.show()
