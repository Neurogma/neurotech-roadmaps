# I want to learn neural signal processing

Learners who want a strong signal-processing foundation for EEG and other neural measurements.

## Destination

- Reason about sampling, filters, spectra and time-frequency estimates mathematically.
- Quantify how analysis choices change a signal estimate.
- Select methods based on the question rather than a default software pipeline.

## Starting assumptions

- The path assumes basic programming or willingness to learn enough Python to work through the exercises.

## Entry prerequisites

- [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml)
- [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml)
- [Probability foundations](../nodes/foundations/probability.yml)
- [Python and scientific computing](../nodes/foundations/python-scientific.yml)

## Time budgets

- **Explorer:** 8–15
- **Builder:** 80–130
- **Researcher:** 170–300+

## Core path

1. [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml) — `neuroscience-basics`
2. [Neural physiology and electrical signaling](../nodes/foundations/physiology-neural.yml) — `physiology-neural`
3. [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml) — `math-linear-algebra`
4. [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml) — `math-calculus`
5. [Python and scientific computing](../nodes/foundations/python-scientific.yml) — `python-scientific`
6. [Digital signal processing](../nodes/foundations/signal-processing.yml) — `signal-processing`
7. [Probability foundations](../nodes/foundations/probability.yml) — `probability`
8. [Statistics and inference](../nodes/foundations/statistics-inference.yml) — `statistics-inference`
9. [Neural signal processing](../nodes/domains/neural-signal-processing.yml) — `neural-signal-processing`

## Minimum viable path

Predict how sampling, filtering and windowing affect synthetic signals, then reproduce those effects on one public EEG segment.

## Deeper path

Study time-frequency methods, spatial filtering, source estimation and method-specific uncertainty.

## Projects

- [Signal visualization](../projects/beginner/signal-visualization.yml)
- [Power spectral density analysis](../projects/beginner/psd-analysis.yml)
- [Reproducible EEG preprocessing](../projects/intermediate/eeg-preprocessing.yml)
- [Artifact analysis lab](../projects/intermediate/artifact-analysis.yml)

## Paper sequence

- [Common spatio-time-frequency patterns for motor imagery-based brain machine interfaces](../papers/paper-guides/paper-higashi-tanaka-cstfp.yml)
- [MOABB: trustworthy algorithm benchmarking for BCIs](../papers/paper-guides/paper-moabb-2018.yml)

## Resources

- **SciPy documentation** — https://docs.scipy.org/doc/scipy/index.html
- **MNE-Python documentation** — https://mne.tools/stable/
- **NumPy documentation** — https://numpy.org/doc/
- **EEG Motor Movement/Imagery Dataset** — https://physionet.org/content/eegmmidb/1.0.0/

## Common misconceptions

- A cleaner-looking signal is not necessarily a more valid signal; preprocessing can remove task-relevant information.

## Typical failure modes

- Selecting filter settings by habit, reporting spectral results without windowing details, and ignoring phase or edge effects.

## What to learn next

Move into neural decoding, modality-specific analysis or neural data science.
