from genericpath import exists
from matplotlib.pyplot import plot as plt

import os
import shutil
import argparse

from logger.log_resouce import *
from code_generator.v_code_generator import *
from filter_design.filter_design import *

def filter_builder_args(parser):  
    parser.add_argument("--name", "-n", type = str, default = "filter", help="Module name. Default = filter")
    parser.add_argument("--order", "-o", type = int, default = 8, help="Set the filter order. Default = 8")
    parser.add_argument("--fsample", "-fs", type = int, default = 10000, help="Set filter's sampling frequency. Default = 10000")
    parser.add_argument("--fcut", "-fc", type = float, nargs="+", default = [1000], help="Set filter's cut frequency. It is possible to add more than one fcut ie: -fc 100 200. Default = 1000")
    parser.add_argument("--window", "-w", type = str, default = "hamming", help="FIR filter window. If the window requires no parameters, then window can be a string.\
                                                                                If the window requires parameters, then window must be a tuple with the first argument the string name of the window, and the next arguments the needed parameters. Default = hamming")
    parser.add_argument("--beta", "-b", type = float, default = '0.1', help="Beta argument for kaiser window")
    parser.add_argument("--response", "-r", type = str, default = 'lowpass', help="Filter type: lowpass, highpass, bandpass or bandstop. Default = lowpass")

    parser.add_argument("--io_nbits", type = int, default = 16, help="Number of bits for input/output quantization. Default = 16")
    parser.add_argument("--io_nbits_decimal", type = int, help="Number of bits for input/output quantization. Default = IO nBIts -1")
    parser.add_argument("--coeff_nbits", type = int, default = 16, help="Number of bits for coefficients quantization. Default = 16")
    parser.add_argument("--coeff_nbits_decimal", type = int, help="Number of bits for coefficients quantization. Default = Coefficient nBits -1")
    parser.add_argument("--resetn", action = "store_true", default = False, help="Active low reset in the filter module")
    parser.add_argument("--verbose", "-v", action = "count", default = 0, help="Enable print messages with design steps. Three different verbose levels (-v -vv -vvv)")
    parser.add_argument("--testbench", "-tb", action = "store_true", default = False, help="Generates a testbench for the filter.")
    # parser.add_argument("--sim", "-s", action = "store_true", default = False, help="Generates a testbench for the filter and execute it using Icarus verilog. \
                                                                                              # Needs Icarus Verilog installed and added to the PATH. Simulation results \
                                                                                              # are stored in an vcd file")
    parser.add_argument("--axi_stream", "-axis", action = "store_true", default = False, help="Generate AXI4 Stream interfaces for input and output")
    parser.add_argument("--force", "-f", action = "store_true", help="Force deletion of the existing folder.")
    parser.add_argument('--version', action='version', version='v0.1 (April 2022)')

def filter_builder_main(args):
  # create filter file path
  output_module_path = f'./_output/{args.name}'
  log(f'Creating "{args.name}.v" file into "{output_module_path}"', 'info', args.verbose)
  
  if not(os.path.exists(output_module_path)):
    os.makedirs(output_module_path)
  
  filepath = f'{output_module_path}/{args.name}.v'

  # check arguments
  io_nbits_decimal = (args.io_nbits - 1) if not(args.io_nbits_decimal) else args.io_nbits_decimal
  if not(args.io_nbits_decimal):
    log(f'IN/OUT fractional bits are not defined. Defined in {args.io_nbits - 1} bits.', 'warning', args.verbose)

  coeff_nbits_decimal = (args.coeff_nbits - 1) if not(args.coeff_nbits_decimal) else args.coeff_nbits_decimal
  if not(args.coeff_nbits_decimal):
    log(f'Coefficients fractional bits are not defined. Defined in {args.io_nbits - 1} bits.', 'warning', args.verbose)

  wc = []
  for cutoff in args.fcut:
    if cutoff > args.fsample/2:
      log(f'Cut frequency {args.fcut} is greater than the Nyquist frequency {args.fsample/2}. Filter cannot be designed.', 'error', args.verbose)
    wc.append(cutoff / (args.fsample/2))

  coeffs = fir_design(wc, args.response, args.order, args.window, args.beta, args.verbose)

  # documentation
  fir_images(output_module_path, coeffs, args.name, args.order, wc, args.verbose)

  quantized_coeffs = quantize_coeffs(coeffs, coeff_nbits_decimal, args.verbose)

  write_verilog_fir_code(filepath, args.name,'fir', args.response, args.order, wc, args.window, args.beta, args.coeff_nbits, coeff_nbits_decimal, args.io_nbits, io_nbits_decimal, quantized_coeffs, args.resetn, args.axi_stream, args.verbose)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Filter builder utility.")
  filter_builder_args(parser)
  args = parser.parse_args()
  filter_builder_main(args)