"""
%Steps to Run in MATLAB:

%Step 1: Reload the Python script to see your changes
iir_module = py.importlib.import_module('iir');
py.importlib.reload(iir_module);

%Step 2: Call the Python function to run your filter logic
results = iir_module.process_iir_and_return_for_plot();

%Step 3: Convert the Python data into MATLAB arrays
original_signal = double(py.numpy.array(results{1}));
filtered_signal = double(py.numpy.array(results{2}));

%Step 4: Use MATLAB to create the plot
figure;
subplot(2,1,1);
plot(original_signal);
title('Original Signal (IIR)');
grid on;

subplot(2,1,2);
plot(filtered_signal);
title('Filtered Signal (IIR Low-Pass)');
grid on;
"""

import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wavfile
# Matplotlib is no longer needed as MATLAB will handle the plotting.

def process_iir_and_return_for_plot():
    """
    This function contains your original, unchanged logic for the IIR filter.
    It returns the original and filtered data so MATLAB can create the plot.
    """

    # --- YOUR ORIGINAL CODE STARTS HERE (LOGIC IS UNCHANGED) ---

    input_path = r'C:\Verilog Labs\FPGA\Real_Time_3Band_Audio_Equalizer\samples\orginal_samples_for_testing\audio.wav'
    
    # Read the input .wav file
    sample_rate, data = wavfile.read(input_path)
    
    print(f'sample rate = {sample_rate}')

    # Design an IIR lowpass filter
    numtaps = 4  # Number of filter taps
    high_cutoff = 500  # High cutoff frequency in Hz
    nyquist_rate = sample_rate / 2.0
    cutoff = high_cutoff / nyquist_rate
    b, a = signal.iirfilter(numtaps, cutoff, btype='lowpass', analog=False, ftype='butter')

    print(f'Writing file successfully')

    # Apply the filter to the data
    filtered_data = signal.lfilter(b, a, data)
    
    print(f'a = {a}')
    print(f'b = {b}')

    output_path = r'C:\Verilog Labs\FPGA\Real_Time_3Band_Audio_Equalizer\samples\Matlab_Output\iir_audio.wav'

    # Write the filtered data to a new .wav file
    wavfile.write(output_path, sample_rate, filtered_data.astype(np.int16))

    # --- YOUR ORIGINAL CODE ENDS HERE ---
    
    # Return the data needed for plotting
    return data, filtered_data
