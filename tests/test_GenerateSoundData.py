import pytest
import numpy as np
from sound.GenerateSoundData import GenerateSoundData
from ArrayTracker import ArrayTracker

# Test initialization
def test_initialization():
    data = GenerateSoundData(fps=60)
    assert data.FPS == 60
    assert data.FREQ_SAMPLE == 44100
    assert data.OVERSAMPLE == 2

# Test get method
def test_getFreqSample():
    sound = GenerateSoundData(fps=60)
    assert sound.getFreqSample() == 44100

# Test sound generation
def test_generate():
    data = GenerateSoundData(fps=60)
    arr = np.array([50, 200, 500, 1000])
    array = ArrayTracker(arr)

    soundData = data.generate(array)

    assert isinstance(soundData, np.ndarray)
    # Expected length = sample rate * (number of tracked values / fps)
    expectedLen = int(44100 * len(array.values) / 60)
    assert len(soundData) == expectedLen
    assert soundData.dtype == float