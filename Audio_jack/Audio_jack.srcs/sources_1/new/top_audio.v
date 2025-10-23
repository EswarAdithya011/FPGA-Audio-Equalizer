`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 10.09.2025 00:45:46
// Design Name: 
// Module Name: top_audio
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module top_audio (
    input wire clk,       // Nexys 4's 100 MHz system clock
    output wire aud_pwm,   // PWM output to the audio amplifier
    output wire aud_sd     // Audio amplifier shutdown/enable pin
);

    // --- Internal Signal Declarations ---
    // These signals connect the different logic blocks and the IP core.
    reg [15:0] audio_addr = 0;       // 16-bit address counter for the BRAM
    wire [7:0] audio_sample;         // 8-bit audio data read from the BRAM
    
    reg audio_clk_reg = 0;           // A slow clock signal for sampling audio
    reg [31:0] clk_divider_counter = 0; // Counter to generate the audio clock
    
    reg [7:0] pwm_counter = 0;       // Counter for the PWM generator

    // --- Parameters for Clock Division ---
    // Calculates the division ratio to get a 44.1 kHz sample rate from 100 MHz.
    // The division value is for a toggling clock, so we divide by 2.
    parameter AUDIO_SAMPLE_RATE = 44100;
    parameter SYSTEM_CLOCK_RATE = 100_000_000;
    parameter DIVIDER_VALUE = (SYSTEM_CLOCK_RATE / AUDIO_SAMPLE_RATE) / 2;

    // --- Instance of the Block Memory IP ---
    // This is where your IP core is connected to the top-level module.
    audio_bram audio_bram_inst (
        .clka(audio_clk_reg),
        .ena(1'b1),
        .wea(1'b0),
        .addra(audio_addr),
        .dina(8'd0),
        .douta(audio_sample)
    );

    // --- Behavioral Logic ---
    // All the sequential logic driven by the main system clock.
    always @(posedge clk) begin
        // Clock Divider Logic: Generates the 44.1 kHz audio clock.
        if (clk_divider_counter == DIVIDER_VALUE) begin
            audio_clk_reg <= ~audio_clk_reg;
            clk_divider_counter <= 0;
        end else begin
            clk_divider_counter <= clk_divider_counter + 1;
        end

        // Address Counter Logic: Reads samples from the BRAM on each audio clock edge.
        if (audio_clk_reg) begin
            audio_addr <= audio_addr + 1;
            // Loop the audio by resetting the address at the end of the memory.
            // 65536 samples is 16'hFFFF
            if (audio_addr == 16'hFFFF) begin 
                audio_addr <= 16'h0000;
            end
        end

        // PWM Counter Logic: Continuously counts up to 255.
        // This counter is the basis for the pulse width.
        pwm_counter <= pwm_counter + 1;
    end

    // --- Combinational Logic ---
    // These assignments are always active and happen instantaneously.

    // PWM Output: The heart of the DAC.
    // The PWM signal is high as long as the PWM counter value is less than the audio sample value.
    assign aud_pwm = (pwm_counter < audio_sample);
    
    // Audio Amplifier Enable: Drives the `aud_sd` pin high to enable the audio output.
    assign aud_sd = 1'b1;

endmodule