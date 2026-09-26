# Reproducibility checklist

For a serious technical project, document enough that another learner can identify exactly what data, code and settings produced the reported result.

- Record the Python and major package versions; pin dependencies where appropriate.
- Record dataset name/version, provenance, license and any preprocessing assumptions.
- Keep configuration values separate from analysis code when practical.
- Set and report random seeds when stochastic procedures are used.
- Keep raw/source data distinct from derived files.
- Use version control and a README with exact commands.
- Report train/validation/test or cross-session/cross-subject splits explicitly.
- Avoid fitting preprocessing steps on held-out data.
- Save enough metadata to identify the analysis environment and result files.
- Record limitations and deviations from the planned analysis.

Reproducibility is not the same as scientific validity: a perfectly reproducible leakage-prone analysis is still invalid.
