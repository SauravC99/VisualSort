import numpy as np

class GenerateSoundData():

    def __init__(self, fps, samplerate=44100, oversample=2) -> None:
        self.FPS = fps
        self.FREQ_SAMPLE = samplerate
        self.OVERSAMPLE = oversample
    
    def generate(self, arr):

        #map the value to a frequency between 360 and 1320 Hz
        def frequency_map(x, x_min=50, x_max=1000, frequency_min=360, frequency_max=1320):
            return np.interp(x, [x_min, x_max], [frequency_min, frequency_max])

        def frequency_sample(frequency, dt=1.0/self.FPS, samplerate=44100, oversample=2):
            middle_samples = int(dt * samplerate)
            padded_samples = int((middle_samples * (oversample - 1) / 2))
            total_samples = middle_samples + 2 * padded_samples

            sin_wave = np.sin(2 * np.pi * frequency * np.linspace(0, dt, total_samples))

            sin_wave[0:padded_samples] = sin_wave[0:padded_samples] * np.linspace(0, 1, padded_samples)
            sin_wave[-padded_samples: ] = sin_wave[len(sin_wave)-padded_samples: ] * np.linspace(1, 0, padded_samples)

            return sin_wave

        wav_data = np.zeros(int(self.FREQ_SAMPLE * len(arr.values) * 1.0 / self.FPS), dtype=float)
        #num of values in a chunk (sample length)
        dN = int(self.FREQ_SAMPLE * 1.0 / self.FPS)

        for i, value in enumerate(arr.values):
            freq = frequency_map(value)
            sample = frequency_sample(freq, 1.0 / self.FPS, self.FREQ_SAMPLE, oversample=self.OVERSAMPLE)

            index_0 = int((i + 0.5) * dN - len(sample) / 2)
            index_1 = index_0 + len(sample)

            try:
                wav_data[index_0 : index_1] += sample
            except ValueError:
                pass

        return wav_data
    
    def getFreqSample(self):
        return self.FREQ_SAMPLE