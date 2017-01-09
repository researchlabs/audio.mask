#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

PATH_TO_AUDIO_SAMPLES 			= '../dataset/audioSamples/wavSamples/'
PATH_TO_ALIGNED_AUDIO_SAMPLES 	= '../dataset/audioSamples/alignedWavSamples/'

leftNostril  = wave.open(PATH_TO_ALIGNED_AUDIO_SAMPLES + 'left (with a tablet).wav','r')
rightNostril = wave.open(PATH_TO_ALIGNED_AUDIO_SAMPLES + 'right (with a phone).wav','r')

# Only mono allowed
if leftNostril.getnchannels() != 1 or rightNostril.getnchannels() != 1:
    print('Only mono files are allowed')
    sys.exit(0)

# Extract raw audio
leftSignal = leftNostril.readframes(-1)
leftSignal = np.fromstring(leftSignal, 'Int16')

rightSignal = rightNostril.readframes(-1)
rightSignal = np.fromstring(rightSignal, 'Int16')

# Plot
plt.figure(1)
plt.title('Simultaneous graph')

plt.plot(leftSignal)
plt.plot(rightSignal)

plt.show()
