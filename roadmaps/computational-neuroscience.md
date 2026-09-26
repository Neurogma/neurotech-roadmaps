# I want to become a computational neuroscientist

Learners interested in mathematical and computational models of neural dynamics, from simplified neurons to population data.

## Destination

- Implement and inspect dynamical models of neural activity.
- Explain what model parameters mean and how assumptions limit interpretation.
- Analyze simulated or public neural data with explicit uncertainty.

## Starting assumptions

- Basic algebra helps; calculus and linear algebra are taught explicitly before modeling.

## Entry prerequisites

- [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml)
- [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml)
- [Python and scientific computing](../nodes/foundations/python-scientific.yml)
- [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml)

## Time budgets

- **Explorer:** 10–18
- **Builder:** 80–130
- **Researcher:** 200–350+

## Core path

1. [Linear algebra for neurotechnology](../nodes/foundations/math-linear-algebra.yml) — `math-linear-algebra`
2. [Calculus for dynamical signals](../nodes/foundations/math-calculus.yml) — `math-calculus`
3. [Probability foundations](../nodes/foundations/probability.yml) — `probability`
4. [Statistics and inference](../nodes/foundations/statistics-inference.yml) — `statistics-inference`
5. [Python and scientific computing](../nodes/foundations/python-scientific.yml) — `python-scientific`
6. [Neuroscience fundamentals](../nodes/foundations/neuroscience-basics.yml) — `neuroscience-basics`
7. [Neural physiology and electrical signaling](../nodes/foundations/physiology-neural.yml) — `physiology-neural`
8. [Computational neuroscience](../nodes/computational-neuroscience/computational-neuroscience.yml) — `computational-neuroscience`
9. [Spike-train analysis](../nodes/computational-neuroscience/spike-train-analysis.yml) — `spike-train-analysis`
10. [Biophysical neuron models](../nodes/computational-neuroscience/biophysical-models.yml) — `biophysical-models`

## Minimum viable path

Implement a leaky integrate-and-fire or comparable simple neuron model, sweep parameters and explain the dynamics in a short technical note.

## Deeper path

Compare model classes, parameter identifiability, population dynamics, data-model comparison and reproducible simulation studies.

## Projects

- [Computational neuron simulation](../projects/beginner/computational-neuron-simulation.yml)
- [Spike train analysis](../projects/intermediate/spike-train-analysis.yml)
- [Neural data science analysis](../projects/research/neural-data-science-analysis.yml)

## Paper sequence

- [A quantitative description of membrane current and its application to conduction and excitation in nerve](../papers/paper-guides/paper-hodgkin-huxley.yml)
- [MOABB: trustworthy algorithm benchmarking for BCIs](../papers/paper-guides/paper-moabb-2018.yml)

## Resources

- **NEURON simulator documentation** — https://nrn.readthedocs.io/en/latest/index.html
- **NumPy documentation** — https://numpy.org/doc/
- **SciPy documentation** — https://docs.scipy.org/doc/scipy/index.html
- **DANDI Archive** — https://dandiarchive.org/

## Common misconceptions

- A model that reproduces one phenomenon is not automatically an explanation of all neural behavior.

## Typical failure modes

- Choosing model complexity before defining the phenomenon, hiding parameters, and confusing simulation output with measured data.

## Research directions

- Population dynamics, latent-variable models, mechanistic/statistical hybrids and model-data comparison.

## What to learn next

Move toward neural data science, neural decoding or a specific mechanistic modeling literature.
