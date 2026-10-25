# PBAC Master Concept Paper

Version 0.2 (Draft) · Pakistan Biomedical AI Consortium

## 1. Executive summary

PBAC will build Pakistan's first AI-driven cellular intelligence platform: label-free 3D/4D imaging of living cells, read by open-source AI that segments, tracks and forecasts cell behaviour. The long-term moonshot is the PBAC Intelligent Cellular Scanner, a whole-body, cell-level diagnostic machine. The near-term product is achievable today: a low-cost "sample-to-insight" system that images living cells from a blood draw, biopsy or patient-derived culture without stains, and turns them into quantitative, predictive readouts.

## 2. The problem

- Cell-level diagnostics in Pakistan depend on stained slides, manual microscopy and imported, expensive instruments.
- Imaging that sees living cells in 3D over time exists, but is priced for wealthy labs and needs specialist operators.
- Data from these instruments is mostly analysed by hand, so most of it is never used.

## 3. Core thesis

Cheap optics + open AI = cell intelligence at a fraction of current cost.

- **Label-free quantitative phase imaging / holotomography** measures each cell's refractive index in 3D (sub-cellular resolution, about 200 nm lateral) with no dyes and minimal phototoxicity, so the same living cells can be followed for hours to weeks.
- **Light-sheet fluorescence microscopy (LSFM)** images whole embryos, organoids and cleared tissue in 3D at high speed. Open-hardware builds (OpenSPIM, descSPIM) cost roughly $20,000 to $50,000 against commercial systems costing several times more.
- **Open AI stack**: Cellpose and Segment Anything for Microscopy (micro-SAM) for segmentation; Ultrack and Trackastra for 3D tracking and lineage; the CC0 Biohub zebrafish dataset and MIT-licensed winning solutions as a validated starting point.

## 4. The PBAC pipeline

Scan → Track → Analyze → Predict → Act

| Stage | Today's tool | PBAC agent |
|---|---|---|
| Scan | Holotomography / LSFM | Data Agent: acquisition, QC, curation |
| Track | Cellpose, micro-SAM, Ultrack, Trackastra | Tracking Agent |
| Analyze | Morphology, refractive-index and dynamics features | Analysis Agent |
| Predict | Models trained on outcome-labelled data | Prediction Agent |
| Validate | Specialist review, cross-checking against reference assays | Validation Agent |
| Act | Report for a clinician or researcher | Action Agent (advisory only) |

## 5. Flagship applications (achievable first)

1. **Label-free blood and cell analysis**: cell counts, morphology and abnormality flags from a drop of blood, without stains.
2. **Phenotypic drug response**: watch patient-derived or cultured cells respond to a compound in real time (cytotoxicity, mitochondrial change, death and division).
3. **Scientific validation of Tibb formulations**: run traditional preparations through label-free cell assays under the National Council for Tibb umbrella. This is a niche no other consortium owns, and it turns NCT's role into evidence generation.
4. **Developmental and organoid research** with light-sheet imaging for university partners.

## 6. Roadmap

| Phase | Goal | Indicative cost |
|---|---|---|
| 0. Software proof (0–6 months) | Reproduce top Biohub solutions; build the Scan→Predict pipeline on public data; publish code | Near zero (Kaggle/Colab GPUs) |
| 1. Partner-lab data (6–12 months) | Image local samples on an existing university microscope; first label-free assay; ethics approval | Low; access agreements |
| 2. Low-cost device (12–24 months) | Build a PBAC open-hardware QPI or light-sheet unit; benchmark it against commercial systems | ~$20k–50k |
| 3. Validation (2–4 years) | Prospective studies with hospital partners; regulatory pathway with DRAP | Grant-funded |
| 4. Moonshot (long term) | Research into in-vivo cellular-scale imaging, combining advances in MRI, optics and AI | International consortium |

## 7. Partners and roles

- **National Council for Tibb**: institutional umbrella, Tibb validation track.
- **HPC Labs Lahore/Karachi**: compute for training and 4D data.
- **Universities (NUST, LUMS, PU)**: microscopes, biology expertise, students.
- **HEC**: research funding and recognition.
- **Hospitals**: samples, clinical questions, validation.

## 8. Risks and honest limits

- Optical microscopes see samples, not the inside of a living body: light scatters beyond about 1 mm of tissue. The whole-body scanner stays a research goal, not a product claim.
- Forecasting disease or mutations needs long-term, outcome-labelled patient data. That dataset, not the AI, is the main bottleneck.
- Cell shape is not genome: genetic mutation claims need sequencing as a reference.
- Medical use requires ethics approval, patient consent, data protection and DRAP clearance. Early outputs are research-use only.
- Open hardware carries hidden costs: build time, alignment and trained operators.

## 9. Governance and openness

Code and non-patient data are open-licensed; patient data stays under consented, access-controlled governance. Results are published openly and reproducibly.

## 10. Immediate next steps

1. Reproduce one winning Biohub solution under the PBAC GitHub.
2. Sign one partner-lab access agreement.
3. Complete one proposal (HEC or one university) using the Phase 0 results.
