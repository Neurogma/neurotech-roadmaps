# I want to build neural interfaces

Software, electronics, embedded and biomedical learners who want to integrate neural sensing with feedback and control.

## Destination

- Specify a bounded interface from sensing to user feedback.
- Trace timing, uncertainty and failure modes across the system.
- Build a software-only prototype that exposes state, confidence and safe stop behavior.

## Starting assumptions

- The core path stays in simulation or public-data replay; hardware is treated as an engineering reference, not a clinical device.

## Entry prerequisites

- [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml)
- [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml)
- [Python and scientific computing](../nodes/foundations/python-scientific.yml)

## Time budgets

- **Explorer:** 8–15
- **Builder:** 90–150
- **Researcher:** 180–300+

## Core path

1. [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml) — `neuroscience-basics`
2. [Neural physiology and electrical signaling](../nodes/foundations/physiology-neural.yml) — `physiology-neural`
3. [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml) — `math-linear-algebra`
4. [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml) — `math-calculus`
5. [Python and scientific computing](../nodes/foundations/python-scientific.yml) — `python-scientific`
6. [Digital signal processing](../nodes/foundations/signal-processing.yml) — `signal-processing`
7. [Biological signals](../nodes/domains/biological-signals.yml) — `biological-signals`
8. [Electronics for biosignal acquisition](../nodes/electronics/electronics-biosignals.yml) — `electronics-biosignals`
9. [Control systems](../nodes/foundations/control-systems.yml) — `control-systems`
10. [Embedded systems for neural devices](../nodes/foundations/embedded-systems.yml) — `embedded-systems`
11. [Human-machine interaction for neural systems](../nodes/neural-interfaces/human-machine-interaction.yml) — `human-machine-interaction`
12. [Neural interface engineering](../nodes/neural-interfaces/neural-interfaces.yml) — `neural-interfaces`

## Optional branches

- [Robotics for neurotechnology](../nodes/foundations/robotics.yml)

## Minimum viable path

Implement a replayable software interface with timestamps, confidence, explicit states and a manual override.

## Deeper path

Add real-time constraints, fault injection, multimodal sensing, adaptive control and formalized human-factors evaluation.

## Projects

- [Biosignal acquisition simulation](../projects/intermediate/biosignal-acquisition-simulation.yml)
- [Closed-loop control simulation](../projects/intermediate/closed-loop-control-simulation.yml)
- [Neural interface software simulation](../projects/advanced/neural-interface-software-simulation.yml)

## Paper sequence

- [BCI2000: A General-Purpose Brain-Computer Interface (BCI) System](../papers/paper-guides/paper-bci2000.yml)
- [Brain-computer interfaces for communication and control](../papers/paper-guides/paper-wolpaw-bci.yml)
- [A high-performance speech neuroprosthesis](../papers/paper-guides/paper-speech-neuroprosthesis.yml)

## Resources

- **BrainFlow documentation** — https://brainflow.org/
- **OpenBCI documentation** — https://docs.openbci.com/
- **MNE-Python documentation** — https://mne.tools/stable/
- **EEG Motor Movement/Imagery Dataset** — https://physionet.org/content/eegmmidb/1.0.0/
- **DANDI Archive** — https://dandiarchive.org/

## Common misconceptions

- A prototype that produces the desired output once is not evidence that the system is safe or robust.

## Typical failure modes

- Directly mapping uncertain model output to actuation, hiding state transitions, and failing to log timing or recovery behavior.

## Research directions

- Closed-loop adaptation, multimodal interfaces, uncertainty-aware control, low-latency systems and robust human-machine interaction.

## Safety

Do not use this path to justify clinical, invasive or stimulation experiments. Physical interfaces require appropriate engineering and safety review.

## Ethics

User control, consent, accessibility, data minimization and recovery from erroneous system decisions should be explicit design concerns.

## What to learn next

Branch into BCI, robotics/control or neuroprosthetics according to the intended sensing and actuation problem.
