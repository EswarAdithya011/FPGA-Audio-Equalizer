## Clock signal
## Maps the `clk` port in your Verilog module to the 100 MHz clock input pin (E3) on the Nexys 4 board.
set_property PACKAGE_PIN E3 [get_ports clk]							
set_property IOSTANDARD LVCMOS33 [get_ports clk]
create_clock -add -name sys_clk_pin -period 10.00 -waveform {0 5} [get_ports clk]

## Audio Interface
## Maps the `aud_pwm` port to the A11 pin, which is the PWM input for the audio amplifier.
set_property PACKAGE_PIN A11 [get_ports aud_pwm]					
set_property IOSTANDARD LVCMOS33 [get_ports aud_pwm]

## Maps the `aud_sd` port to the D12 pin, which is the shutdown/enable pin for the audio amplifier.
set_property PACKAGE_PIN D12 [get_ports aud_sd]						
set_property IOSTANDARD LVCMOS33 [get_ports aud_sd]

## Generated Clock for Audio BRAM
## This is the corrected command for the generated clock.
create_generated_clock -name {audio_clk_pin} -source [get_ports clk] -divide_by 2268 [get_pins audio_bram_inst/clka]

## Additional Constraints to Resolve Warnings

# Set the relationship between the two clocks as asynchronous.
# This tells the tool not to analyze timing paths between the main clock and the audio clock.
set_clock_groups -asynchronous -group [get_clocks sys_clk_pin] -group [get_clocks audio_clk_pin]

# Exclude the `aud_pwm` output port from timing analysis.
# This is done because it's a simple I/O pin and not part of a critical timing path.
set_false_path -to [get_ports aud_pwm]