########################################################################
# ERROR CATCHES AND LOGGING
########################################################################
import logging

## Logging set up for .INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

def errorHandlingEOT(eccentricity=None,
					obliquity=None,
					orbit_period=None):

	# Ensure that eccentricity is a float or int
	if eccentricity is None:
		logger.critical("\nCRITICAL ERROR, [eccentricity]: eccentricity is required")
		exit()
	if eccentricity is not None and type(eccentricity) != int and type(eccentricity) != float:
		logger.critical("\nCRITICAL ERROR, [eccentricity]: Must be a int or float, current type = '{0}'".format(type(eccentricity)))
		exit()

	# Ensure that obliquity is a float or int
	if obliquity is None:
		logger.critical("\nCRITICAL ERROR, [obliquity]: obliquity is required")
		exit()
	if obliquity is not None and type(obliquity) != int and type(obliquity) != float:
		logger.critical("\nCRITICAL ERROR, [obliquity]: Must be a int or float, current type = '{0}'".format(type(obliquity)))
		exit()

	# Ensure that orbit_period is a float or int
	if orbit_period is None:
		logger.critical("\nCRITICAL ERROR, [orbit_period]: orbit_period is required")
		exit()
	if orbit_period is not None and type(orbit_period) != int and type(orbit_period) != float:
		logger.critical("\nCRITICAL ERROR, [orbit_period]: Must be a int or float, current type = '{0}'".format(type(orbit_period)))
		exit()
	

def errorHandlingPlotEOT(eot_dict=None,
						plot_title=None,
						plot_x_title=None,
						plot_y_title=None,
						show_plot=None,
						fig_plot_color=None,
						figsize_n=None,
						figsize_dpi=None,
						save_plot_name=None):

	# Ensure that plot_title is a string
	if plot_title is not None and type(plot_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_title]: Must be a str, current type = '{0}'".format(type(plot_title)))
		exit()

	# Ensure that plot_x_title is a string
	if plot_x_title is not None and type(plot_x_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_x_title]: Must be a str, current type = '{0}'".format(type(plot_x_title)))
		exit()

	# Ensure that plot_y_title is a string
	if plot_y_title is not None and type(plot_y_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_y_title]: Must be a str, current type = '{0}'".format(type(plot_y_title)))
		exit()

	# Ensure that all show_plot is a boolean ["True", "False"]
	if type(show_plot) != bool:
		logger.critical("\nCRITICAL ERROR, [show_plot]: Must be a bool, current type = '{0}'".format(type(show_plot)))
		exit()

	# Ensure that the color given is a string (matplotlib has error checking for invalid color options)
	if type(fig_plot_color) != str:
		logger.critical("\nCRITICAL ERROR, [fig_plot_color]: Must be a string, current type = '{0}'".format(type(fig_plot_color)))
		exit()

	# Ensure that all figsize_n is a float or int
	if type(figsize_n) != int and type(figsize_n) != float:
		logger.critical("\nCRITICAL ERROR, [figsize_n]: Must be a int or float, current type = '{0}'".format(type(figsize_n)))
		exit()

	# Ensure that all figsize_dpi is a float or int
	if type(figsize_dpi) != int and type(figsize_dpi) != float:
		logger.critical("\nCRITICAL ERROR, [figsize_dpi]: Must be a int or float, current type = '{0}'".format(type(figsize_dpi)))
		exit()

	# Ensure that the effect title type is a string
	if save_plot_name!= None and type(save_plot_name) != str:
		logger.critical("\nCRITICAL ERROR, [save_plot_name]: Must be a str, current type = '{0}'".format(type(save_plot_name)))
		exit()
