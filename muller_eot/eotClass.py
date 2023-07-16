# Calculate and Plot Equation of Time Class
import muller_eot 

class EOT:
	def __init__(self, eccentricity, obliquity, orbit_period):
		self.eccentricity = eccentricity
		self.obliquity = obliquity
		self.orbit_period = orbit_period

		# Calculate the time different for each day
		self.eotDayAndMinutes = muller_eot.calculateDifferenceEOTMinutes(eccentricity=self.eccentricity,
															obliquity=self.obliquity,
															orbit_period=self.orbit_period)

	def plotEOT(self,
				planet_name="Earth",
				effect_title=None,
				plot_title=None,
				plot_x_title=None,
				plot_y_title=None,
				showPlot=True,
				fig_plot_color="C0",
				figsize_n=12,
				figsize_dpi=100):
		# Plot the EOT time difference generated from calculateDifferenceEOTMinutes()
		muller_eot.plotEOT(planet_name=planet_name,
							eot_dict=self.eotDayAndMinutes,
							effect_title=effect_title,
							plot_title=plot_title,
							plot_x_title=plot_x_title,
							plot_y_title=plot_y_title,
							showPlot=showPlot,
							fig_plot_color=fig_plot_color,
							figsize_n=figsize_n,
							figsize_dpi=figsize_dpi)
