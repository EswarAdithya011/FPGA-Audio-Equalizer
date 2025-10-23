"""
%Steps to Run in MATLAB:

%Step 1: Reload the Python script to see your changes
fir_module = py.importlib.import_module('fir');
py.importlib.reload(fir_module);

%Step 2: Call the Python function to run your filter logic and get the data
results = fir_module.process_audio_and_return_for_plot();

%Step 3: Convert the Python data into MATLAB arrays
original_signal = double(py.numpy.array(results{1}));
filtered_signal = double(py.numpy.array(results{2}));

%Step 4: Use MATLAB to create the plot in a new window
figure;
subplot(2,1,1);
plot(original_signal);
title('Original Signal (Plotted in MATLAB)');
grid on;

subplot(2,1,2);
plot(filtered_signal);
title('Filtered Signal (Plotted in MATLAB)');
grid on;
"""

import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wavfile
# Matplotlib is no longer needed in this script, as MATLAB will do the plotting.

def process_audio_and_return_for_plot():
    """
    This function contains your original, unchanged logic for processing the audio file.
    It now returns the original and filtered data so MATLAB can plot it.
    """
    
    # --- YOUR ORIGINAL CODE STARTS HERE (LOGIC IS UNCHANGED) ---
    
    input_path = r'C:\Verilog Labs\FPGA\Real_Time_3Band_Audio_Equalizer\samples\orginal_samples_for_testing\audio.wav'

    # Read the input .wav file
    sample_rate, data = wavfile.read(input_path)

    # Create own sample (This code was present but commented out in your original script)
    #sample_rate = 44100
    #freq_cl = 1000
    #freq_ns = 150
    #t = np.linspace(0, 1.0, sample_rate)
    #data = 10*np.sin(2*freq_cl*np.pi*t) + 5*np.cos(2*freq_ns*np.pi*t)

    # Design a FIR bandpass filter using the Hamming window
    numtaps = 30  # Number of filter taps (adjust as needed)
    low_cutoff = 4000  # Low cutoff frequency in Hz
    high_cutoff = 20000  # High cutoff frequency in Hz
    nyquist_rate = sample_rate / 2.0
    cutoff = [low_cutoff / nyquist_rate, high_cutoff / nyquist_rate]
    fir_coeff = signal.firwin(numtaps, cutoff, window='hamming', pass_zero='bandpass')
    
    # Print the coefficients
    for i in range (0, numtaps):
        print(fir_coeff[i])

    print(f'Writing file successfully')

    # Apply the filter to the data
    filtered_data = signal.lfilter(fir_coeff, 1.0, data)

    output_path = r'C:\Verilog Labs\FPGA\Real_Time_3Band_Audio_Equalizer\samples\Matlab_Output\audio.wav'

    # Write the filtered data to a new .wav file
    wavfile.write(output_path, sample_rate, filtered_data.astype(np.int16))
    
    # --- YOUR ORIGINAL CODE ENDS HERE ---

    # Return the data needed for plotting
    return data, filtered_data
