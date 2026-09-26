# I want to learn BCI

Learners who want an end-to-end, non-clinical understanding of BCI systems, with EEG as the main entry modality.

## Destination

- Explain the sensing–decoding–feedback loop and its assumptions.
- Build and evaluate a reproducible non-clinical EEG decoder.
- Read BCI studies by task, data, evaluation design and limitations.

## Starting assumptions

- Basic algebra and one programming language help, but the default path fills the main gaps.
- Use public datasets and simulation rather than collecting data.

## Entry prerequisites

- [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml)
- [Python and scientific computing](../nodes/foundations/python-scientific.yml)
- [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml)

## Time budgets

- **Explorer:** 8–15
- **Builder:** 90–140
- **Researcher:** 180–300+

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
18. [BCI systems fundamentals](../nodes/bci/bci-fundamentals.yml) — `bci-fundamentals`

## Optional branches

- [P300 event-related potential analysis](../nodes/eeg/p300-analysis.yml)
- [SSVEP analysis](../nodes/eeg/ssvep-analysis.yml)
- [Motor-imagery decoding pipeline](../nodes/bci/motor-imagery-pipeline.yml)
- [Deep learning for neural data](../nodes/foundations/deep-learning.yml)

## Minimum viable path

Reach EEG preprocessing, PSD analysis and a transparent decoder on public data with subject-aware evaluation; stop there before adding deep learning.

## Deeper path

Add multiple paradigms, cross-session/cross-subject evaluation, uncertainty, adaptive interaction and primary-literature critique.

## Projects

- [Signal visualization](../projects/beginner/signal-visualization.yml)
- [Reproducible EEG preprocessing](../projects/intermediate/eeg-preprocessing.yml)
- [Power spectral density analysis](../projects/beginner/psd-analysis.yml)
- [Motor imagery pipeline](../projects/intermediate/motor-imagery-pipeline.yml)
- [Neural interface software simulation](../projects/advanced/neural-interface-software-simulation.yml)
- [Deep-learning neural decoding benchmark](../projects/advanced/deep-learning-neural-decoding.yml)
- [P300 analysis](../projects/intermediate/p300-analysis.yml)
- [SSVEP analysis](../projects/intermediate/ssvep-analysis.yml)

## Paper sequence

- [Brain-computer interfaces for communication and control](../papers/paper-guides/paper-wolpaw-bci.yml)
- [BCI2000: A General-Purpose Brain-Computer Interface (BCI) System](../papers/paper-guides/paper-bci2000.yml)
- [Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials](../papers/paper-guides/paper-p300-speller.yml)
- [Common spatio-time-frequency patterns for motor imagery-based brain machine interfaces](../papers/paper-guides/paper-higashi-tanaka-cstfp.yml)
- [MOABB: trustworthy algorithm benchmarking for BCIs](../papers/paper-guides/paper-moabb-2018.yml)

## Resources

- **MNE-Python documentation** — https://mne.tools/stable/
- **MNE-BIDS documentation** — https://mne.tools/mne-bids/stable/index.html
- **MOABB documentation** — https://moabb.neurotechx.com/docs/
- **scikit-learn user guide** — https://scikit-learn.org/stable/user_guide.html
- **EEG Motor Movement/Imagery Dataset** — https://physionet.org/content/eegmmidb/1.0.0/
- **OpenNeuro EEG datasets** — https://openneuro.org/search/modality/eeg
- **BCI Competition II datasets** — https://www.bbci.de/competition/ii/

## Common misconceptions

- BCI is not synonymous with reading thoughts; the decoder is trained for a defined target under defined conditions.
- Within-subject accuracy is not evidence of generalization to new people.

## Typical failure modes

- Leakage through preprocessing or split design, unclear event definitions, and treating a classifier score as a system-level performance measure.

## Research directions

- Cross-subject generalization, calibration reduction, uncertainty, adaptive BCIs, multimodal interfaces and long-term robustness.

## Safety

Use public data and simulation. Invasive or clinical BCI work requires appropriate professional, institutional and regulatory structures.

## Ethics

Keep autonomy, agency, accessibility, participant burden and neural-data governance explicit when evaluating a BCI.

## What to learn next

Use the 12-week plan as the builder entry point, then choose a P300, SSVEP or motor-imagery branch.
