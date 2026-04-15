## Ramachandran Plot of Alanine Dipeptide

---

### Objective

To generate and analyze the Ramachandran plot (φ vs ψ) for alanine dipeptide.

---

## Approaches

### 1. OpenMM + MDTraj (Attempt)

* Used molecular dynamics simulation
* Goal: generate trajectory and extract φ/ψ

Issues:

* Residue labeled as `UNL`
* Forcefield could not recognize molecule
* Simulation failed

---

### 2. Analytical Energy Model (Final)

* Generated φ/ψ values across full range
* Modeled energy landscape using mathematical function
* Visualized using contour plot

✔ Successfully reproduced:

* α-helix region
* β-sheet region

---

## Challenges

* Forcefield incompatibility with non-standard residues
* MDTraj requires protein-like backbone

---

## Output

* Energy contour Ramachandran plot
* Clear conformational basins

---

## Run Final Version

```id="run1"
pip install -r requirements.txt
python ramachandran_model.py
```

---

## Key Learning

* Ramachandran plots require multiple conformations
* MD simulation depends on correct residue templates
* Analytical models can approximate conformational space

---

## Files

* `ramachandran_openmm.py` → initial simulation attempt
* `ramachandran_model.py` → final working solution

---

