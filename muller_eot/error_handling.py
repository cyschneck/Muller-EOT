########################################################################
# ERROR CATCHES AND LOGGING
########################################################################
import logging

## Logging set up for .INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def errorHandlingEOT(eccentricity,
					obliquity_deg,
					orbit_period):

	# Ensure that eccentricity is a float or int
	if eccentricity is not None and type(eccentricity) != int and type(eccentricity) != float:
		logger.critical("\nCRITICAL ERROR, [eccentricity]: Must be a int or float, current type = '{0}'".format(type(eccentricity)))
		exit()
	if eccentricity is None:
		logger.critical("\nCRITICAL ERROR, [eccentricity]: Must be a int or float, currently is 'None'")
		exit()
	logger.debug("eccentricity = '{0}'".format(eccentricity))

	# Ensure that obliquity_deg is a float or int
	if obliquity_deg is not None and type(obliquity_deg) != int and type(obliquity_deg) != float:
		logger.critical("\nCRITICAL ERROR, [obliquity_deg]: Must be a int or float, current type = '{0}'".format(type(obliquity_deg)))
		exit()
	if obliquity_deg is None:
		logger.critical("\nCRITICAL ERROR, [obliquity_deg]: Must be a int or float, currently is 'None'")
		exit()
	logger.debug("obliquity_deg = '{0}'".format(obliquity_deg))

	# Ensure that orbit_period is a float or int
	if orbit_period is not None and type(orbit_period) != int and type(orbit_period) != float:
		logger.critical("\nCRITICAL ERROR, [orbit_period]: Must be a int or float, current type = '{0}'".format(type(orbit_period)))
		exit()
	if orbit_period is None:
		logger.critical("\nCRITICAL ERROR, [orbit_period]: Must be a int or float, currently is 'None'")
		exit()
	logger.debug("orbit_period = '{0}'".format(orbit_period))

def errorHandlingPlotEOT(planet_name,
						eot_dict,
						effect_title_str,
						plot_title,
						plot_x_title,
						plot_y_title,
						showPlot,
						fig_plot_color,
						figsize_n,
						figsize_dpi,
						save_plot_name):

	# Ensure that planet_name is a string
	if type(planet_name) != str:
		logger.critical("\nCRITICAL ERROR, [planet_name]: Must be a str, current type = '{0}'".format(type(planet_name)))
		exit()
	if planet_name is None:
		logger.critical("\nCRITICAL ERROR, [planet_name]: Must be a int or float, currently is 'None'")
		exit()
	logger.debug("planet_name = '{0}'".format(planet_name))

	# Ensure that all values in eot_dict for minute differences is a float or int
	if type(eot_dict) is not dict:
		logger.critical("\nCRITICAL ERROR, [eot_y]: Must be a dict, currently is '{0}'".format(type(eot_dict)))
		exit()
	for minute_dif in eot_dict.values():
		if type(minute_dif) != int and type(minute_dif) != float:
			logger.critical("\nCRITICAL ERROR, [eot_dict.values()]: Must be a int or float, current type = '{0}'".format(type(minute_dif)))
			exit()
	if len(eot_dict.values()) < 1:
		logger.critical("\nCRITICAL ERROR, [eot_dict.values()]: Must have a length greater than zero")
		exit()
	logger.debug("eot_dict = '{0}'".format(eot_dict))

	# Ensure that the effect title type is a string
	if type(effect_title_str) != str:
		logger.critical("\nCRITICAL ERROR, [effect_title_str]: Must be a str, current type = '{0}'".format(type(effect_title_str)))
		exit()
	if effect_title_str is None:
		logger.critical("\nCRITICAL ERROR, [effect_title_str]: Must be a str, currently is 'None'")

	# Ensure that plot_title is a string
	if plot_title is not None and type(plot_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_title]: Must be a str, current type = '{0}'".format(type(plot_title)))
		exit()
	logger.debug("plot_title = '{0}'".format(plot_title))

	# Ensure that plot_x_title is a string
	if plot_x_title is not None and type(plot_x_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_x_title]: Must be a str, current type = '{0}'".format(type(plot_x_title)))
		exit()
	logger.debug("plot_x_title = '{0}'".format(plot_x_title))

	# Ensure that plot_y_title is a string
	if plot_y_title is not None and type(plot_y_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_y_title]: Must be a str, current type = '{0}'".format(type(plot_y_title)))
		exit()
	logger.debug("plot_y_title = '{0}'".format(plot_y_title))

	# Ensure that all showPlot is a boolean ["True", "False"]
	if type(showPlot) != bool:
		logger.critical("\nCRITICAL ERROR, [showPlot]: Must be a bool, current type = '{0}'".format(type(showPlot)))
		exit()
	logger.debug("showPlot = '{0}'".format(showPlot))

	# Ensure that the color given is a string (matplotlib has error checking for invalid color options)
	if type(fig_plot_color) != str:
		logger.critical("\nCRITICAL ERROR, [fig_plot_color]: Must be a string, current type = '{0}'".format(type(fig_plot_color)))
		exit()
	logger.debug("fig_plot_color = '{0}'".format(fig_plot_color))

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
