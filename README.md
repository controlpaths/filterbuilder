# filterbuilder tool

Filterbuilder is a tool that allow the designer design different kind of digital filter. Filterbuilder designs and also implement the filter in verilog.

## Usage

In order to use the tool, you must call the filter_builder_main.py script with the argument --help.

```
filter_builder$ python3 filter_builder_main.py --help
usage: filter_builder_main.py [-h] [--name NAME] [--order ORDER] [--fsample FSAMPLE] [--fcut FCUT [FCUT ...]] [--window WINDOW] [--beta BETA] [--response RESPONSE] [--io_nbits IO_NBITS] [--io_nbits_decimal IO_NBITS_DECIMAL] [--coeff_nbits COEFF_NBITS] [--coeff_nbits_decimal COEFF_NBITS_DECIMAL] [--resetn] [--verbose] [--testbench] [--sim] [--axi_stream] [--force] [--version]

Filter builder utility.

optional arguments:
  -h, --help            show this help message and exit
  --name NAME, -n NAME  Module name. Default = filter
  --order ORDER, -o ORDER
                        Set the filter order. Default = 8
  --fsample FSAMPLE, -fs FSAMPLE
                        Set filter's sampling frequency. Default = 10000
  --fcut FCUT [FCUT ...], -fc FCUT [FCUT ...]
                        Set filter's cut frequency. It is possible to add more than one fcut ie: -fc 100 200. Default = 1000
  --window WINDOW, -w WINDOW
                        FIR filter window. If the window requires no parameters, then window can be a string. If the window requires parameters, then window must be a tuple with the first argument the
                        string name of the window, and the next arguments the needed parameters. Default = hamming
  --beta BETA, -b BETA  Beta argument for kaiser window
  --response RESPONSE, -r RESPONSE
                        Filter type: lowpass, highpass, bandpass or bandstop. Default = lowpass
  --io_nbits IO_NBITS   Number of bits for input/output quantization. Default = 16
  --io_nbits_decimal IO_NBITS_DECIMAL
                        Number of bits for input/output quantization. Default = IO nBIts -1
  --coeff_nbits COEFF_NBITS
                        Number of bits for coefficients quantization. Default = 16
  --coeff_nbits_decimal COEFF_NBITS_DECIMAL
                        Number of bits for coefficients quantization. Default = Coefficient nBits -1
  --resetn              Number of bits for coefficients quantization. Default = Coefficient nBits -1
  --verbose, -v         Enable print messages with design steps. Three different verbose levels (-v -vv -vvv)
  --testbench, -tb      Generates a testbench for the filter.
  --sim, -s             Generates a testbench for the filter and execute it using Icarus verilog. Needs Icarus Verilog installed and added to the PATH. Simulation results are stored in an vcd file
  --axi_stream, -axis   Generate AXI4 Stream interfaces for input and output
  --force, -f           Force deletion of the existing folder.
  --version             show program's version number and exit

```
Maintainers: 

**Pablo Trujillo**. FPGA designer (https://www.controlpaths.com)  
**Sara Martínez**. Python developer and QA analyst.
