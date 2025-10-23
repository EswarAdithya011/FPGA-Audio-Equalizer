"""
%Steps to Run in MATLAB:

%Step 1: Reload the Python script to see your changes
fft_module = py.importlib.import_module('view_fft');
py.importlib.reload(fft_module);

%Step 2: Call the Python function to run the FFT calculation
results = fft_module.calculate_fft_and_return_for_plot();

%Step 3: Convert the Python data into MATLAB arrays
frequencies = double(py.numpy.array(results{1}));
fft_data = double(py.numpy.array(results{2}));

%Step 4: Use MATLAB to create the plot
figure;
plot(frequencies, fft_data);
title('Frequency Spectrum (Plotted in MATLAB)');
xlabel('Frequency (Hz)');
ylabel('Amplitude');
grid on;
"""

import numpy as np
# Matplotlib is no longer needed as MATLAB will handle the plotting.

def calculate_fft_and_return_for_plot():
    """
    This function reads a .hex file, calculates the FFT,
    and returns the frequency and amplitude data for MATLAB to plot.
    """
    # --- YOUR ORIGINAL CODE STARTS HERE (LOGIC IS UNCHANGED) ---

    # Path to the .hex file you want to analyze
    # This path is updated to match your project structure
    hex_path = r'C:\Verilog Labs\FPGA\Real_Time_3Band_Audio_Equalizer\samples\orginal_samples_for_testing\audio.hex'

    # Read the hex file
    with open(hex_path, 'r') as file:
        hex_data = file.read().splitlines()

    # Convert hex data to integers
    data = [int(x, 16) for x in hex_data]

    # Ensure the data is a numpy array
    data = np.array(data)

    # Compute the FFT
    sample_rate = 44100  # Given sample rate
    n = len(data)
    fft_data = np.fft.fft(data)
    fft_data = np.abs(fft_data)[:n//2]  # Take the positive half of the FFT

    # Create the frequency axis
    frequencies = np.fft.fftfreq(n, d=1/sample_rate)[:n//2]
    
    # --- YOUR ORIGINAL CODE ENDS HERE ---

    # Return the data needed for plotting
    return frequencies, fft_data

