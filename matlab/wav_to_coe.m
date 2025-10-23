% Input file (full path)
[data, fs] = audioread('C:\Verilog Labs\FPGA\Audio_jack\audio_4s.wav');

% If stereo, take only one channel
if size(data,2) > 1
    data = data(:,1);
end

% === Convert to 16-bit signed integer ===
% audioread gives normalized [-1,1], so scale to int16 range [-32768, 32767]
data16 = int16(data * (2^15 - 1));

% Output file (same folder as input)
fid = fopen('C:\Verilog Labs\FPGA\Audio_jack\audio_4s.coe','w');

if fid == -1
    error('❌ Cannot create COE file. Check path or permissions.');
end

% Write COE header
fprintf(fid, 'memory_initialization_radix=16;\n');
fprintf(fid, 'memory_initialization_vector=\n');

% Write samples in hex (4 hex digits = 16 bits)
for i = 1:length(data16)
    v = data16(i);
    if v < 0
        v = v + 2^16;  % convert to two's complement
    end
    fprintf(fid, '%04X', v);   % 4-digit uppercase hex
    
    if i ~= length(data16)
        fprintf(fid, ',\n');
    else
        fprintf(fid, ';\n');
    end
end

fclose(fid);
disp('✅ 16-bit COE file "audio16.coe" generated successfully');
