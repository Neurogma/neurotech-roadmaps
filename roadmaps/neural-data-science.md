# I want to enter neural data science

Python-capable learners who want research-grade habits for neural datasets rather than a modality-specific specialization first.

## Destination

- Build an analysis with explicit provenance and subject-aware evaluation.
- Use statistical and machine-learning baselines without leakage.
- Communicate uncertainty, dataset limitations and reproducibility details.

## Starting assumptions

- The core route assumes basic Python; learners who lack it should start at python-scientific.

## Entry prerequisites

- [Python and scientific computing](../nodes/foundations/python-scientific.yml)
- [Statistics and inference](../nodes/foundations/statistics-inference.yml)
- [Digital signal processing](../nodes/foundations/signal-processing.yml)

## Time budgets

- **Explorer:** 8–15
- **Builder:** 70–120
- **Researcher:** 160–280+

## Core path

1. [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml) — `math-linear-algebra`
2. [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml) — `math-calculus`
3. [Python and scientific computing](../nodes/foundations/python-scientific.yml) — `python-scientific`
4. [Probability foundations](../nodes/foundations/probability.yml) — `probability`
5. [Statistics and inference](../nodes/foundations/statistics-inference.yml) — `statistics-inference`
6. [Digital signal processing](../nodes/foundations/signal-processing.yml) — `signal-processing`
7. [Machine learning for neural data](../nodes/foundations/machine-learning.yml) — `machine-learning`
8. [Scientific writing and reporting](../nodes/foundations/scientific-writing.yml) — `scientific-writing`
9. [Research methodology](../nodes/foundations/research-methodology.yml) — `research-methodology`
10. [Neural data science](../nodes/neural-data-science/neural-data-science.yml) — `neural-data-science`

## Optional branches

- [Deep learning for neural data](../nodes/foundations/deep-learning.yml)

## Minimum viable path

Take one public neural dataset from provenance to analysis, using a held-out evaluation design and a short reproducibility report.

## Deeper path

Add cross-dataset validation, uncertainty analysis, model comparison and multimodal data integration.

## Projects

- [Power spectral density analysis](../projects/beginner/psd-analysis.yml)
- [Simple neural decoding](../projects/intermediate/simple-neural-decoding.yml)
- [Neural data science analysis](../projects/research/neural-data-science-analysis.yml)

## Paper sequence

- [MOABB: trustworthy algorithm benchmarking for BCIs](../papers/paper-guides/paper-moabb-2018.yml)
- [The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments](../papers/paper-guides/paper-bids.yml)

## Resources

- **MNE-Python documentation** — https://mne.tools/stable/
- **scikit-learn user guide** — https://scikit-learn.org/stable/user_guide.html
- **BIDS specification** — https://bids-specification.readthedocs.io/en/stable/index.html
- **EEG Motor Movement/Imagery Dataset** — https://physionet.org/content/eegmmidb/1.0.0/
- **OpenNeuro EEG datasets** — https://openneuro.org/search/modality/eeg
- **DANDI Archive** — https://dandiarchive.org/

## Common misconceptions

- A large model does not rescue poor dataset definition or a leaky evaluation design.

## Typical failure modes

- Optimizing the test set, ignoring subject/session structure, and reporting only aggregate metrics.

## Research directions

- Dataset shift, uncertainty, multimodal integration, scalable provenance and subject-aware evaluation.

## Ethics

Treat data provenance, consent, access control and potential inferences as part of the analysis design.

## What to learn next

Specialize in EEG/BCI, neuroimaging or computational neuroscience once the analysis workflow is stable.
