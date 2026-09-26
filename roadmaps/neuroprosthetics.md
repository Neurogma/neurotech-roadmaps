# I want to work on neuroprosthetics

Biomedical, robotics, neuroscience and engineering learners interested in assistive or restorative systems.

## Destination

- Model the sensing–inference–control–actuation loop and its failure modes.
- Evaluate latency, uncertainty and user override in a simulated assistive system.
- Distinguish research demonstrations from clinically validated devices.

## Starting assumptions

- You can follow basic programming and quantitative reasoning.
- The default work is simulation and public data.

## Entry prerequisites

- [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml)
- [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml)
- [Python and scientific computing](../nodes/foundations/python-scientific.yml)

## Time budgets

- **Explorer:** 10–18
- **Builder:** 100–160
- **Researcher:** 220–400+

## Core path

1. [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml) — `neuroscience-basics`
2. [Neuroanatomy for neurotechnology](../nodes/foundations/neuroanatomy-basics.yml) — `neuroanatomy-basics`
3. [Neural physiology and electrical signaling](../nodes/foundations/physiology-neural.yml) — `physiology-neural`
4. [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml) — `math-linear-algebra`
5. [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml) — `math-calculus`
6. [Python and scientific computing](../nodes/foundations/python-scientific.yml) — `python-scientific`
7. [Digital signal processing](../nodes/foundations/signal-processing.yml) — `signal-processing`
8. [Biological signals](../nodes/domains/biological-signals.yml) — `biological-signals`
9. [Electronics for biosignal acquisition](../nodes/electronics/electronics-biosignals.yml) — `electronics-biosignals`
10. [Biomedical engineering for neurotechnology](../nodes/foundations/biomedical-engineering.yml) — `biomedical-engineering`
11. [Control systems](../nodes/foundations/control-systems.yml) — `control-systems`
12. [Robotics for neurotechnology](../nodes/foundations/robotics.yml) — `robotics`
13. [Embedded systems for neural devices](../nodes/foundations/embedded-systems.yml) — `embedded-systems`
14. [Human-machine interaction for neural systems](../nodes/neural-interfaces/human-machine-interaction.yml) — `human-machine-interaction`
15. [Neural interface engineering](../nodes/neural-interfaces/neural-interfaces.yml) — `neural-interfaces`
16. [Neuroprosthetics systems fundamentals](../nodes/neuroprosthetics/neuroprosthetics-fundamentals.yml) — `neuroprosthetics-fundamentals`

## Optional branches

- [EEG fundamentals](../nodes/eeg/eeg-fundamentals.yml)
- [Intracortical interface concepts](../nodes/domains/intracortical-interfaces.yml)
- [Computational neuroscience](../nodes/computational-neuroscience/computational-neuroscience.yml)

## Minimum viable path

Build a simulated intent-to-actuation loop with explicit idle, uncertain and manual-override states and measure control latency.

## Deeper path

Study modality-specific devices, adaptation, long-term stability, human factors, clinical endpoints and regulatory evidence.

## Projects

- [Biosignal acquisition simulation](../projects/intermediate/biosignal-acquisition-simulation.yml)
- [Closed-loop control simulation](../projects/intermediate/closed-loop-control-simulation.yml)
- [Neural interface software simulation](../projects/advanced/neural-interface-software-simulation.yml)
- [Neuroprosthetic control simulation](../projects/advanced/neuroprosthetic-control-simulation.yml)

## Paper sequence

- [A high-performance speech neuroprosthesis](../papers/paper-guides/paper-speech-neuroprosthesis.yml)
- [Brain-computer interfaces for communication and control](../papers/paper-guides/paper-wolpaw-bci.yml)

## Resources

- **BrainFlow documentation** — https://brainflow.org/
- **OpenBCI documentation** — https://docs.openbci.com/
- **MNE-Python documentation** — https://mne.tools/stable/
- **EEG Motor Movement/Imagery Dataset** — https://physionet.org/content/eegmmidb/1.0.0/
- **DANDI Archive** — https://dandiarchive.org/

## Common misconceptions

- A good decoder is not automatically a validated assistive device.
- Clinical usefulness requires evidence beyond an offline algorithm benchmark.

## Typical failure modes

- Bypassing human-factors analysis, treating uncertain intent as ground truth, and ignoring drift or maintenance burden.

## Research directions

- Long-term stability, multimodal decoding, shared control, adaptation, embodiment and real-world robustness.

## Safety

Keep self-directed work in simulation and public datasets. Implantation, stimulation, patient-facing devices and clinical evaluation require qualified settings.

## Ethics

Treat user agency, informed consent, accessibility, maintenance burden and benefit/risk as system requirements.

## What to learn next

Choose a sensing modality branch or move deeper into robotics/control and translational evidence.
