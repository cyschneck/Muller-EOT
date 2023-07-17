# Calculate and Plot Equation of Time Class
import muller_eot 

class EOT:
	def __init__(self,
				eccentricity=None,
				obliquity=None,
				orbit_period=None):
		# EOT Required
		self.eccentricity = eccentricity
		self.obliquity = obliquity
		self.orbit_period = orbit_period

		# Calculate the time different for each day
		self.eotDayAndMinutes = muller_eot.calculateDifferenceEOTMinutes(eccentricity=self.eccentricity,
															obliquity=self.obliquity,
															orbit_period=self.orbit_period)

	def plotEOT(self,
				plot_title=None,
				plot_x_title=None,
				plot_y_title=None,
				show_plot=True,
				fig_plot_color="cornflowerblue",
				figsize_n=12,
				figsize_dpi=100,
				save_plot_name=None):
		# Plot the EOT time difference generated from calculateDifferenceEOTMinutes()
		muller_eot.plotEOT(eot_dict=self.eotDayAndMinutes,
							plot_title=plot_title,
							plot_x_title=plot_x_title,
							plot_y_title=plot_y_title,
							show_plot=show_plot,
							fig_plot_color=fig_plot_color,
							figsize_n=figsize_n,
							figsize_dpi=figsize_dpi,
							save_plot_name=save_plot_name)
