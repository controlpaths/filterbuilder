import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

from logger.log_resouce import log

# FIR design function according arguments
def fir_design (wc, response, order, conf_window, conf_beta, verbose):

  log(f'Designing {order}th orderFIR filter', 'info', verbose)

  if conf_window == 'kaiser':
    taps = signal.firwin(order+1,tuple(wc),window = (conf_window, conf_beta), pass_zero = response)
  else:
    taps = signal.firwin(order+1,tuple(wc),window = conf_window, pass_zero = response)

  log(f'Coefficients:  {"".join(str(taps))}', 'info', verbose)

  return taps

def fir_images (output_path, taps, module_name, order, wc, verbose):

  # bode magnitude
  w1,h1 = signal.freqz(taps)
  plt.plot(w1/np.pi, 20 * np.log10(abs(h1)), 'k') 
  plt.title(f'{order}th FIR, wc = {wc}')
  plt.grid()
  plt.savefig(f'{output_path}/{module_name}_mag_bode.svg')

# Quantize coefficients according arguments
def quantize_coeffs (coeffs, bits, verbose):

  log("Quantifying coefficients...", 'info', verbose)

  coeffs_quantized = []
  for coeff in coeffs:
    if np.floor(coeff * 2**bits) == 0:
      log(f'Coefficient {coeff} is zero after quantification', 'warning', verbose)

    coeffs_quantized.append(int(np.floor(coeff * 2**bits)))
  
  log(f'Coefficients quantized:  {"".join(str(coeffs_quantized))}', 'info', verbose)

  return coeffs_quantized