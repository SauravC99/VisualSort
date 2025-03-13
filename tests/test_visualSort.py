import os
import pytest
import visualSort
from InterfaceSortAlgo import InterfaceSortAlgo


class DummySort(InterfaceSortAlgo):
    def sort(self, arr):
        arr.arr.sort()

    def getName(self):
        return "DummySort"
    

def test_precheck(monkeypatch, tmp_path):
    def fake_exists(path):
        if path == "frames/":
            return False
        return os.path.exists(path)
    
    monkeypatch.setattr(os.path, "exists", fake_exists)
    
    # When precheck is called, it should call subprocess.call with ["mkdir", "frames"]
    visualSort.precheck()
    assert ["mkdir", "frames"] in dummy_subprocess_calls

def test_setGlobalVariables():
    visualSort.setGlobalVariables(20, 30, True)
    assert visualSort.N == 20
    assert visualSort.FPS == 30
    assert visualSort.RAINBOW is True

def test_run(capsys):
    visualSort.setGlobalVariables(10, 60, False)
    dummy_algo = DummySort()
    
    visualSort.run(dummy_algo)
    
    captured = capsys.readouterr().out
    assert "DummySort" in captured

    # Check that wav was written
    assert len(dummy_wav_write_calls) > 0

    # Make sure that an ffmpeg command was called
    assert any("ffmpeg" in " ".join(cmd) for cmd in dummy_subprocess_calls)

def test_cleanup(capsys):
    # Set a dummy soundFile name for cleanup()
    visualSort.soundFile = "DummySound.wav"
    visualSort.cleanup()
    
    expected = [
        ["rm", "DummySound.wav"],
        ["rm", "-r", "frames"],
        ["mkdir", "frames"]
    ]

    for cmd in expected:
        assert cmd in dummy_subprocess_calls
        
    output = capsys.readouterr().out
    assert "deleting sound file" in output
    assert "deleting frames folder" in output
    assert "making folder" in output

# Dummy functions to record external calls
dummy_subprocess_calls = []
def fake_subprocess_call(cmd):
    dummy_subprocess_calls.append(cmd)
    return 0

dummy_wav_write_calls = []
def fake_wavfile_write(filename, samplerate, data):
    dummy_wav_write_calls.append((filename, samplerate, data))

dummy_savefig_calls = []
def fake_savefig(self, filename, **kwargs):
    dummy_savefig_calls.append(filename)


@pytest.fixture(autouse=True)
def reset_globals_and_calls(monkeypatch):
    dummy_subprocess_calls.clear()
    dummy_wav_write_calls.clear()
    dummy_savefig_calls.clear()
    
    monkeypatch.setattr(visualSort.subprocess, "call", fake_subprocess_call)
    monkeypatch.setattr(visualSort.sp.io.wavfile, "write", fake_wavfile_write)
    monkeypatch.setattr(visualSort.plt.Figure, "savefig", fake_savefig)