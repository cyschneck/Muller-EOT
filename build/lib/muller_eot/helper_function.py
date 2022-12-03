def calculateOrbitalPeriod(semimajor_axis):
	# caculate orbital period (days): P**2 = a**2 where P=period and a = semimajor axis
	# return a list of days starting at midnight
	sidereal_year = pow(semimajor_axis, 3/2)
	orbital_period_days = sidereal_year * 365.25
	return orbital_period_days

def calculateEccentricity(aphelion_distance, perihelion_distance):
	# caclulate the eccentricity of orbit based on orbit
	## TODO
	eccentricity_orbit = (aphelion_distance - perihelion_distance) / (aphelion_distance + perihelion_distance)
	return eccentricity_orbit

def calculatePerihelionDay():
	 # calendar day of perihelion (ranges from 3 to 5th)
	## TODO
	day_of_perhelion = 5.325 # 2020   
	return day_of_perhelion    

def calculateWinterSolsticeDay():
	 # calendar day of the winter solstice (ranges from 21 to 23th)
	## TODO
	day_of_winter_solstice = 21 # 2020   
	return day_of_winter_solstice    

def calculateDistanceBetweenSolisticePerhelion():
	# angle covered by the Earth between the begnning of Winter (21st December) and the arrival of the Earth at perihelion (2nd January)
	## TODO
	distance_between_solistice_perhelion_deg = 14.40 # 2020
	return distance_between_solistice_perhelion_deg
