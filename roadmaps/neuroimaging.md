# I want to work on neuroimaging

Learners interested in MRI/fMRI, PET, MEG, fNIRS and related brain-measurement workflows.

## Destination

- Compare measurement principles and resolution trade-offs across modalities.
- Use a public BIDS-organized dataset with documented provenance.
- Interpret imaging findings with attention to preprocessing, confounding and inference.

## Starting assumptions

- The path is research-analysis oriented, not radiological or clinical training.

## Entry prerequisites

- [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml)
- [Neuroanatomy for neurotechnology](../nodes/foundations/neuroanatomy-basics.yml)
- [Statistics and inference](../nodes/foundations/statistics-inference.yml)
- [Python and scientific computing](../nodes/foundations/python-scientific.yml)

## Time budgets

- **Explorer:** 8–15
- **Builder:** 80–130
- **Researcher:** 180–320+

## Core path

1. [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml) — `neuroscience-basics`
2. [Neuroanatomy for neurotechnology](../nodes/foundations/neuroanatomy-basics.yml) — `neuroanatomy-basics`
3. [Probability foundations](../nodes/foundations/probability.yml) — `probability`
4. [Statistics and inference](../nodes/foundations/statistics-inference.yml) — `statistics-inference`
5. [Python and scientific computing](../nodes/foundations/python-scientific.yml) — `python-scientific`
6. [Neuroimaging fundamentals](../nodes/domains/neuroimaging-fundamentals.yml) — `neuroimaging-fundamentals`
7. [Scientific writing and reporting](../nodes/foundations/scientific-writing.yml) — `scientific-writing`
8. [Research methodology](../nodes/foundations/research-methodology.yml) — `research-methodology`

## Optional branches

- [fNIRS](../nodes/domains/fnirs.yml)

## Minimum viable path

Select one public BIDS dataset, document its acquisition and metadata, reproduce a basic QC/summary analysis and state inferential limits.

## Deeper path

Add modality-specific preprocessing, group analysis, source modeling or multimodal fusion with appropriate validation.

## Projects

- [Neuroimaging modality comparison](../projects/intermediate/neuroimaging-comparison.yml)
- [Neural data science analysis](../projects/research/neural-data-science-analysis.yml)

## Paper sequence

- [The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments](../papers/paper-guides/paper-bids.yml)
- [EEG-BIDS, an extension to the brain imaging data structure for electroencephalography](../papers/paper-guides/paper-eeg-bids.yml)

## Resources

- **BIDS specification** — https://bids-specification.readthedocs.io/en/stable/index.html
- **MNE-Python documentation** — https://mne.tools/stable/
- **MNE-BIDS documentation** — https://mne.tools/mne-bids/stable/index.html
- **OpenNeuro EEG datasets** — https://openneuro.org/search/modality/eeg
- **DANDI Archive** — https://dandiarchive.org/

## Common misconceptions

- A brain image does not directly reveal a mental state; interpretation requires a chain of measurement and inference.
- Resolution is multidimensional and cannot be reduced to one number.

## Typical failure modes

- Untracked preprocessing, unplanned multiple comparisons and ignoring dataset-specific access or consent constraints.

## Research directions

- Multimodal fusion, individual differences, computational imaging and reproducible group analysis.

## Safety

Clinical image interpretation and patient data require appropriate professional and institutional context.

## Ethics

Imaging data can remain sensitive after de-identification; follow dataset access, consent and sharing terms.

## What to learn next

Choose a modality or move deeper into neural data science.
