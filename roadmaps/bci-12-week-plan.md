# BCI: a 12-week builder plan

**Target:** a reproducible, non-clinical EEG motor-imagery analysis using public data. Budget **7–9 focused hours/week**. Do not compress difficult theory to fit the calendar; extend the calendar if needed.

| Week | Objective | Concepts | Study | Practical work | Evidence | References | Prerequisite |
|---|---|---|---:|---|---|---|---|
| 1 | Build a usable neuroscience map | neurons, synapses, systems, measurement vs inference | 7h | Draw a sensor → neural activity → behavior map and label observations vs inferences. | Explain 10 terms without notes. | `neuroscience-basics`, `course-human-brain` | Basic algebra |
| 2 | Connect physiology to measurable signals | membrane potential, action potentials, extracellular fields, volume conduction | 8h | Explain how cellular activity can contribute to measured fields; optionally simulate a leaky integrator. | Defend the assumptions in a short oral explanation. | `physiology-neural`, `paper-hodgkin-huxley` | Week 1 |
| 3 | Learn signal-processing primitives | sampling, aliasing, filtering, convolution | 8h | Generate multisine + noise signals and predict filter effects before plotting them. | Reproduce the result from a clean notebook. | `signal-processing`, `software-scipy` | Python basics + Week 2 |
| 4 | Treat EEG as a measurement system | montage, references, events, artifacts | 8h | Load one PhysioNet EEG recording and annotate visible artifacts before preprocessing. | Identify at least three artifact classes and explain their source. | `eeg-fundamentals`, `dataset-eegmmidb` | Weeks 1–3 |
| 5 | Build reproducible preprocessing | filters, bad channels, event alignment, epoching | 8h | Create a preprocessing function with a saved configuration. | Rerun from a clean environment without manual edits. | `eeg-preprocessing`, `software-mne-bids` | Week 4 |
| 6 | Understand spectra | Fourier analysis, PSD, windows, frequency resolution | 7h | Compare PSDs before and after preprocessing and vary one parameter deliberately. | Explain why the estimate changes. | `psd-analysis`, `software-mne`, `software-scipy` | Week 3 |
| 7 | Evaluate uncertainty | distributions, resampling, class balance | 7h | Bootstrap a toy metric and compare it with a point estimate. | State what the interval does and does not imply. | `statistics-inference`, `course-mit-probability` | Probability basics |
| 8 | Build a transparent decoder | features, baseline classifiers, cross-validation | 9h | Train one baseline on a predefined public-data subset. | Show that held-out data never enters fitting. | `machine-learning`, `software-scikit-learn` | Weeks 5–7 |
| 9 | Handle subject variability | subject/session splits, calibration, variance | 8h | Compare within-subject and cross-subject evaluation. | Per-subject results + split audit. | `neural-decoding`, `dataset-eegmmidb` | Week 8 |
| 10 | Turn the analysis into a system | latency, confidence, feedback, failure states | 7h | Draw and simulate a BCI state machine around the decoder. | Walk through nominal, uncertain and failure cases. | `bci-fundamentals` | Week 9 |
| 11 | Make the work reproducible | provenance, versions, seeds, limitations | 8h | Rebuild the analysis from a clean clone/environment. | Fresh-run checklist passes. | `docs/reproducibility.md` | Weeks 8–10 |
| 12 | Package competence evidence | scientific writing, critique, communication | 9h | Write the final report and record the evaluation limitations. | Second-person review against the acceptance rubric below. | `scientific-writing`, `paper-moabb-2018` | Full sequence |

## Final project acceptance

The project should identify the exact dataset/version, record preprocessing choices, define a leakage-resistant evaluation split, report subject- or session-aware results where relevant, document the software environment, include a transparent baseline, and state limitations that are no broader than the experiment supports.

## What 12 weeks does not mean

This is a builder milestone, not clinical competence, invasive-device expertise, independent research maturity, or mastery of neuroscience, signal processing and machine learning.
