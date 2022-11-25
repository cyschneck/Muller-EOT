########################################################################
# ERROR CATCHES AND LOGGING
########################################################################
import logging

## Logging set up for .INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def errorHandlingEOT(eccentricity,
					obliquity_deg,
					orbit_period):

	# Ensure that eccentricity is a float or int
	if type(eccentricity) != int and type(eccentricity) != float:
		logger.critical("\nCRITICAL ERROR, [eccentricity]: Must be a int or float, current type = '{0}'".format(type(eccentricity)))
		exit()
	logger.debug("eccentricity = '{0}'".format(eccentricity))

	# Ensure that obliquity_deg is a float or int
	if type(obliquity_deg) != int and type(obliquity_deg) != float:
		logger.critical("\nCRITICAL ERROR, [obliquity_deg]: Must be a int or float, current type = '{0}'".format(type(obliquity_deg)))
		exit()
	logger.debug("obliquity_deg = '{0}'".format(obliquity_deg))

	# Ensure that orbit_period is a float or int
	if type(orbit_period) != int and type(orbit_period) != float:
		logger.critical("\nCRITICAL ERROR, [orbit_period]: Must be a int or float, current type = '{0}'".format(type(orbit_period)))
		exit()
	logger.debug("orbit_period = '{0}'".format(orbit_period))

def errorHandlingPlotEOT(planet_name,
						orbital_period,
						eot_y,
						effect_title_str,
						figsize_n,
						figsize_dpi,
						save_plot_name):

	# Ensure that planet_name is a string
	if type(planet_name) != str:
		logger.critical("\nCRITICAL ERROR, [planet_name]: Must be a str, current type = '{0}'".format(type(planet_name)))
		exit()
	logger.debug("planet_name = '{0}'".format(planet_name))

	# Ensure that orbital_period is a float or int
	if type(orbital_period) != int and type(orbital_period) != float:
		logger.critical("\nCRITICAL ERROR, [orbital_period]: Must be a int or float, current type = '{0}'".format(type(orbital_period)))
		exit()
	logger.debug("orbital_period = '{0}'".format(orbital_period))

	# Ensure that all y values for minute differences is a float or int
	for minute_dif in eot_y:
		if type(minute_dif) != int and type(minute_dif) != float:
			logger.critical("\nCRITICAL ERROR, [minute_dif]: Must be a int or float, current type = '{0}'".format(type(minute_dif)))
			exit()
		logger.debug("minute_dif = '{0}'".format(minute_dif))

	# Ensure that the effect title type is a string
	if type(effect_title_str) != str:
		logger.critical("\nCRITICAL ERROR, [effect_title_str]: Must be a str, current type = '{0}'".format(type(effect_title_str)))
		exit()
	logger.debug("effect_title_str = '{0}'".format(effect_title_str))

	# Ensure that all figsize_n is a float or int
	if type(figsize_n) != int and type(figsize_n) != float:
		logger.critical("\nCRITICAL ERROR, [figsize_n]: Must be a int or float, current type = '{0}'".format(type(figsize_n)))
		exit()
	logger.debug("figsize_n = '{0}'".format(figsize_n))

	# Ensure that all figsize_dpi is a float or int
	if type(figsize_dpi) != int and type(figsize_dpi) != float:
		logger.critical("\nCRITICAL ERROR, [figsize_dpi]: Must be a int or float, current type = '{0}'".format(type(figsize_dpi)))
		exit()
	logger.debug("figsize_dpi = '{0}'".format(figsize_dpi))

	# Ensure that the effect title type is a string
	if save_plot_name!= None and type(save_plot_name) != str:
		logger.critical("\nCRITICAL ERROR, [save_plot_name]: Must be a str, current type = '{0}'".format(type(save_plot_name)))
		exit()
	logger.debug("save_plot_name = '{0}'".format(save_plot_name))
