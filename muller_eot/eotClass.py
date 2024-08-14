# Calculate and Plot Equation of Time Class
import muller_eot 

class EOT:
	def __init__(self,
				eccentricity: float =None,
				obliquity: float = None,
				orbit_period: float = None):
		# EOT Required
		self.eccentricity = eccentricity
		self.obliquity = obliquity
		self.orbit_period = orbit_period

		# Calculate the time different for each day
		self.eotDayAndMinutes = muller_eot.calculateDifferenceEOTMinutes(eccentricity=self.eccentricity,
															obliquity=self.obliquity,
															orbit_period=self.orbit_period)

	def plotEOT(self,
				plot_title: str = None,
				plot_x_title: str = None,
				plot_y_title: str = None,
				show_plot:bool = True,
				fig_plot_color: str = "cornflowerblue",
				figsize_n: int = 12,
				figsize_dpi: int = 100,
				save_plot_name: str = None):
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
