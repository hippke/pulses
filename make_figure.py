import numpy
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from astropy.stats import LombScargle
from astropy.io import fits
from astropy import units
from astropy.constants import c


def running_median(data, kernel):
    """Returns sliding median of width 'kernel' and same length as data """
    idx = numpy.arange(kernel) + numpy.arange(len(data) - kernel + 1)[:, None]
    med = numpy.median(data[idx], axis=1)

    # Append the first/last value at the beginning/end to match the length of data
    first_values = med[0]
    last_values = med[-1]
    missing_values = len(data) - len(med)
    values_front = int(missing_values / 2)
    values_end = missing_values - values_front
    med = numpy.append(numpy.full(values_front, first_values), med)
    med = numpy.append(med, numpy.full(values_end, last_values))
    return med


def find_nearest(array, value):
    idx = (numpy.abs(array - value)).argmin()
    return idx


def linearize(frequencies, flux, upsteps=100000, targetsteps=10000):
    frequencies_interpolated = interp1d(
        numpy.linspace(0, 1, len(frequencies)), frequencies, kind='linear') \
        (numpy.linspace(min(numpy.linspace(0, 1, len(frequencies))), \
            max(numpy.linspace(0, 1, len(frequencies))), num=upsteps))
    flux_interpolated = interp1d(numpy.linspace(0, 1, len(flux)), flux, kind='linear') \
        (numpy.linspace(min(numpy.linspace(0, 1, len(flux))),
            max(numpy.linspace(0, 1, len(flux))), num=upsteps))
    linearized_frequencies = numpy.linspace(
        min(frequencies), max(frequencies), targetsteps)
    linearized_flux = numpy.zeros(targetsteps)
    for i in range(len(linearized_frequencies)):
        linearized_flux[i] = flux_interpolated[find_nearest(
            frequencies_interpolated, linearized_frequencies[i])]
    return linearized_frequencies, linearized_flux


# Load Kurucz synthetic solar spectrum
file = 'solar_spectrum_kurucz_4k.csv'
data = numpy.genfromtxt(file)
wavelengths = data[:,0] * 10
flux = data[:,1]

# Normalize flux to the range [0, 1]
flux = flux - min(flux)
flux = flux / max(flux)

# Convert wavelengths to equally spaced frequencies
frequencies = numpy.divide(c / (units.meter / units.second) * 10**10, wavelengths)  # Hz
linearized_frequencies, linearized_flux = linearize(frequencies, flux)

# Fit running median
window = 0.03
windowsize = int(len(linearized_flux) * window)
median = running_median(linearized_flux, windowsize)
cleaned_flux = linearized_flux - median

# Cut off the first and last window size, where the median could not be fit
cleaned_flux = cleaned_flux[windowsize:-windowsize]
linearized_frequencies = linearized_frequencies[windowsize:-windowsize]
linearized_flux = linearized_flux[windowsize:-windowsize]
median = median[windowsize:-windowsize]

# Calculate Lomb-Scargle periodogram
freqs, power = LombScargle(linearized_frequencies, cleaned_flux).autopower()
continuum = numpy.std(power)
power = numpy.divide(power, continuum)  # Normalize to S/N

# Calculate sine model for best freq
best_frequency = freqs[numpy.argmax(power)]
y_fit = LombScargle(linearized_frequencies, cleaned_flux).model(
    linearized_frequencies, best_frequency)

# Make figure
fig = plt.figure(figsize=(9,6))
plt.rc('font', family='serif', serif='Computer Modern')
plt.rc('text', usetex=True)
plt.subplots_adjust(wspace=0.25, hspace=0.3)
plt.subplot(2, 2, 1)
plt.xlim(min(linearized_frequencies), max(linearized_frequencies))
plt.plot(linearized_frequencies, linearized_flux, color='black', linewidth=0.5)
plt.plot(linearized_frequencies, median, color='red', linewidth=1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized flux')
plt.text(3.6*10**14, 0.95, 'a')

plt.subplot(2, 2, 2)
plt.ylim([0, max(power)*1.2])
plt.xlim([10**-14, 4*10**-12])
plt.plot(freqs, power, color='black', linewidth=0.5)
peak1 = 1.09*10**-13
peak2 = 1.64*10**-12
plt.plot([peak1, peak1], [0, max(power) * 1.2], color='red', linewidth=1, linestyle='dashed', alpha=0.5)
plt.plot([peak2, peak2], [0, max(power) * 1.2], color='red', linewidth=1, linestyle='dashed', alpha=0.5)
plt.xlabel('Period (s)')
plt.ylabel('Power')
plt.xscale("log")
plt.text(1.2*10**-14, 24.5, 'b')
plt.text(1.25*10**-13, 24.5, r'$1.09\times10^{-13}\,$s')

plt.subplot(2, 2, 3)
plt.xlim(min(linearized_frequencies), max(linearized_frequencies))
plt.plot(linearized_frequencies, cleaned_flux, color='black', linewidth=0.5)
plt.plot(linearized_frequencies, y_fit, color='red', linewidth=1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized flux')
plt.text(3.6*10**14, 0.20, 'c')

plt.subplot(2, 2, 4)
plt.xlim(min(linearized_frequencies), max(linearized_frequencies))
plt.plot(linearized_frequencies, cleaned_flux, color='black', linewidth=0.5)
plt.plot(linearized_frequencies, y_fit, color='red', linewidth=1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized flux')
plt.xlim(6.5*10**14, 7*10**14)
plt.text(6.52*10**14, 0.20, 'd')

fig.align_labels()
plt.savefig('1.pdf', bbox_inches='tight')
plt.savefig('1.png', bbox_inches='tight', dpi=200)
