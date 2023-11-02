import subprocess

scripts = ["Audio Recorder.py", ".WAV - Morse Code.py"]

# Run scripts in parallel
processes = [subprocess.Popen(["python", script]) for script in scripts]

# Wait for all processes to finish
for process in processes:
    process.wait()
