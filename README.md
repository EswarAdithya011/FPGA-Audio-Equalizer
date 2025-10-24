# FPGA Audio Equalizer

## Abstract

This report details the design and implementation of a digital audio playback system on a Xilinx Artix-7 FPGA, specifically using the Digilent Nexys 4 development board. The project demonstrates a complete software-to-hardware workflow for rendering audio without the need for an external Digital-to-Analog Converter (DAC). The core methodology involves pre-processing a digital audio file in a software environment (MATLAB/Python), where digital filtering techniques (FIR/IIR) can be applied. The processed audio samples are then converted into a Xilinx Coefficient File (.coe) and used to initialize an on-chip Block RAM (BRAM).

A custom hardware module, designed in Verilog, is implemented on the FPGA to read the audio samples sequentially from the BRAM at a standard audio sampling rate of 44.1 kHz. The digital samples are then converted into an analog-equivalent signal using Pulse-Width Modulation (PWM). The Verilog design includes a clock divider to generate the precise audio sampling clock from the board's 100 MHz system clock, an address counter for BRAM access, and a PWM generator. The resulting PWM signal is output through the FPGA's pins to an audio jack, enabling playback on standard speakers or headphones. The project successfully validates the use of FPGAs for direct digital audio synthesis and demonstrates the efficacy of PWM as a simple, resource-efficient DAC.


### Features

* Complete **software-to-hardware** audio playback pipeline.
* Supports **MATLAB/Python** preprocessing for FIR/IIR filtering.
* Converts `.wav` files to **Xilinx .coe** format for BRAM initialization.
* Implements **PWM-based DAC** for analog signal reconstruction.
* Achieves **real-time audio playback** at 44.1 kHz sampling rate.

### Repository Structure

```
FPGA-Audio-Equalizer/
├── Audio_jack/                # FPGA project folder for the audio jack interface
│   ├── Audio_jack.xpr
│   ├── Audio_jack.cache/
│   ├── Audio_jack.gen/
│   ├── Audio_jack.ip_user_files/
│   ├── Audio_jack.runs/
│   └── …other Vivado project files…
├── Imgs/                       # Images/screenshots/diagrams
│   ├── Audio Filtering.png
│   ├── Block Diagram.png
│   ├── Power Usage.png
│   ├── Timing Summary.png
│   └── …etc…
├── coe/                        # Coefficient files for BRAM / audio samples
│   ├── GoodMorning.coe
│   ├── sine_8s_65536.coe
│   └── voice_output.coe
├── docs/                       # Documentation & report files
│   ├── 3 - Band Audio Equalizer.docx
│   ├── 3 - Band Audio Equalizer.pdf
│   └── 3 - Band Audio Equalizer.pptx
├── matlab/                     # MATLAB scripts for audio / coe conversion
│   └── wav_to_coe.m
├── py/                         # Python scripts (processing, filtering, FFT)
│   ├── fir.py
│   ├── iir.py
│   └── view_fft.py
├── wav/                        # Raw/sample wav files for testing
│   └── GoodMorning_trimmed.wav
├── .gitignore
├── README.md
└── LICENSE                     # (if present)

```

### How It Works

1. **Preprocess Audio**: Filter the audio using MATLAB or Python (FIR/IIR).
2. **Generate .COE File**: Convert the filtered `.wav` file into a hexadecimal `.coe` file.
3. **Vivado Design**: Initialize BRAM with `.coe` file and integrate Verilog logic.
4. **Synthesize & Implement**: Generate the FPGA bitstream using Vivado.
5. **Program & Test**: Load the bitstream, connect an audio jack to the PWM output, and verify playback.

### Hardware Setup

* **Board**: Digilent Nexys 4 (Artix-7 XC7A100TCSG324-1)
* **Audio Output**: 3.5mm audio jack connected to PWM output pin
* **System Clock**: 100 MHz onboard clock divided to 44.1 kHz
* **Tools Used**: Xilinx Vivado 2024.1, Matlab R2021a, VS Code

### Key Modules

* **Clock Divider**: Generates precise 44.1 kHz sampling clock.
* **BRAM Controller**: Sequentially reads preloaded audio samples.
* **PWM Generator**: Converts digital samples into analog-equivalent waveform.

### Results Summary

* Synthesized successfully on Artix-7 FPGA.
* Minimal resource utilization (tiny fraction of LUTs/FFs).
* Clear audio playback achieved on hardware.

### Future Improvements

* Stereo playback support.
* Real-time audio streaming via UART/SPI.
* Integration of digital equalizer filters directly on FPGA.

## 👥 Team Members

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/EswarAdithya011">
        <img src="https://github.com/EswarAdithya011.png" width="100px;" alt=""/>
        <br /><sub><b>Korrapolu Eswar Adithya</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SudaSarath66">
        <img src="https://github.com/SudaSarath66" width="100px;" alt=""/>
        <br /><sub><b>Sarath Kumar Suda</b></sub>
      </a>
    </td>
  </tr>
</table>

---

> **Note:** Ensure the sampling rate of the `.wav` file matches 44.1 kHz for accurate playback. Adjust `DIVIDER_VALUE` in `top_audio.v` if using a different rate.
