# I want to learn EEG

Learners who want practical competence with scalp EEG data and the reasoning needed to analyze it responsibly.

## Destination

- Explain what scalp EEG measures and what it does not directly reveal.
- Build a reproducible preprocessing and spectral-analysis workflow.
- Identify major artifact sources and evaluate their effect on downstream results.

## Starting assumptions

- The path is analysis-first and does not require hardware acquisition.

## Entry prerequisites

- [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml)
- [Python and scientific computing](../nodes/foundations/python-scientific.yml)
- [Digital signal processing](../nodes/foundations/signal-processing.yml)

## Time budgets

- **Explorer:** 8–15
- **Builder:** 60–100
- **Researcher:** 140–240+

## Core path

1. [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml) — `neuroscience-basics`
2. [Neuroanatomy for neurotechnology](../nodes/foundations/neuroanatomy-basics.yml) — `neuroanatomy-basics`
3. [Neural physiology and electrical signaling](../nodes/foundations/physiology-neural.yml) — `physiology-neural`
4. [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml) — `math-linear-algebra`
5. [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml) — `math-calculus`
6. [Python and scientific computing](../nodes/foundations/python-scientific.yml) — `python-scientific`
7. [Digital signal processing](../nodes/foundations/signal-processing.yml) — `signal-processing`
8. [Biological signals](../nodes/domains/biological-signals.yml) — `biological-signals`
9. [EEG fundamentals](../nodes/eeg/eeg-fundamentals.yml) — `eeg-fundamentals`
10. [EEG preprocessing](../nodes/eeg/eeg-preprocessing.yml) — `eeg-preprocessing`
11. [Probability foundations](../nodes/foundations/probability.yml) — `probability`
12. [Statistics and inference](../nodes/foundations/statistics-inference.yml) — `statistics-inference`
13. [Machine learning for neural data](../nodes/foundations/machine-learning.yml) — `machine-learning`
14. [Scientific writing and reporting](../nodes/foundations/scientific-writing.yml) — `scientific-writing`
15. [Research methodology](../nodes/foundations/research-methodology.yml) — `research-methodology`
16. [Experimental design for neurotechnology](../nodes/foundations/experimental-design.yml) — `experimental-design`
17. [Neural decoding fundamentals](../nodes/ml/neural-decoding.yml) — `neural-decoding`

## Optional branches

- [P300 event-related potential analysis](../nodes/eeg/p300-analysis.yml)
- [SSVEP analysis](../nodes/eeg/ssvep-analysis.yml)
- [Deep learning for neural data](../nodes/foundations/deep-learning.yml)

## Minimum viable path

Load public EEG, document the montage and events, create a reproducible preprocessing pipeline, inspect a PSD and annotate artifacts.

## Deeper path

Add event-related analysis, time-frequency methods, cross-session evaluation, source modeling or modality comparisons.

## Projects

- [Signal visualization](../projects/beginner/signal-visualization.yml)
- [Reproducible EEG preprocessing](../projects/intermediate/eeg-preprocessing.yml)
- [Power spectral density analysis](../projects/beginner/psd-analysis.yml)
- [Artifact analysis lab](../projects/intermediate/artifact-analysis.yml)
- [P300 analysis](../projects/intermediate/p300-analysis.yml)
- [SSVEP analysis](../projects/intermediate/ssvep-analysis.yml)

## Paper sequence

- [EEG-BIDS, an extension to the brain imaging data structure for electroencephalography](../papers/paper-guides/paper-eeg-bids.yml)
- [Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials](../papers/paper-guides/paper-p300-speller.yml)
- [Common spatio-time-frequency patterns for motor imagery-based brain machine interfaces](../papers/paper-guides/paper-higashi-tanaka-cstfp.yml)

## Resources

- **MNE-Python documentation** — https://mne.tools/stable/
- **MNE-BIDS documentation** — https://mne.tools/mne-bids/stable/index.html
- **BIDS specification** — https://bids-specification.readthedocs.io/en/stable/index.html
- **EEG Motor Movement/Imagery Dataset** — https://physionet.org/content/eegmmidb/1.0.0/
- **OpenNeuro EEG datasets** — https://openneuro.org/search/modality/eeg
- **BCI Competition II datasets** — https://www.bbci.de/competition/ii/

## Common misconceptions

- A spectral peak is not automatically a biomarker, diagnosis or direct readout of a cognitive state.

## Typical failure modes

- Ignoring reference choice, treating artifact rejection as purely automatic, and changing preprocessing after seeing the test result.

## Research directions

- Robust preprocessing, cross-subject generalization, source-informed analysis, calibration reduction and multimodal EEG.

## Safety

Use public datasets for self-directed work. Human acquisition introduces electrical, privacy and consent considerations.

## Ethics

Do not infer sensitive traits from EEG outside the evidence supported by the task and study design.

## What to learn next

Choose P300, SSVEP or motor imagery after the baseline analysis is reproducible.
