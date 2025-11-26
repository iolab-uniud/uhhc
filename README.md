[![DOI](https://zenodo.org/badge/1066923342.svg)](https://zenodo.org/badge/latestdoi/1066923342)

# UHHC Problem Repository: Unified Home Healthcare Routing and Scheduling Datasets and Toolbox

The UHHC is a complex optimization problem that involves planning and scheduling home healthcare services, considering constraints such as caregiver availability, patient requirements, time windows, and routing logistics.

This repository is intended for researchers and practitioners working on optimization problems in the domain of home healthcare logistics providing instances, solutions, an instance generation and solution validation toolbox.

The content refers to the [paper](#cite).

## Content Index

- `instances`: contains the instances used in the paper.
- `toolbox`: is a git submodule pointing to the software toolbox
- `managerial-insights`: contains the analysis of selected instances used to get managerial insights
- `solutions`: contains the solutions of the instances as reported in the paper

## Installation
   
**Note:** This repository uses submodules for the `toolbox`. To clone with all dependencies:
```bash
   git clone --recursive https://github.com/iolab-uniud/uhhc.git
```
   
Or if you've already cloned:
```bash
   git submodule update --init --recursive
```

As for the specific instructions for the toolbox refer to the [uhhc-toolbox](https://github.com/iolab-uniud/uhhc-toolbox) GitHub repository.

## Cite

If you use this repository in your research, please cite our paper:

#### BibTeX

```bibtex
@article{ceschia2026unified,
  title        = {A Unified Formulation for Home Healthcare Routing and Scheduling Problems},
  author       = {Ceschia, Sara and Da Ros, Francesca and Di Gaspero, Luca and Mancini, Simona and Maniezzo, Vittorio and Montemanni, Roberto and Rosati, Roberto Maria and Schaerf, Andrea},
  journal      = {International Transactions in Operational Research},
  year         = {2026},
  volume       = {TBD},
  number       = {TBD},
  pages        = {1--43},
  doi          = {10.xxxx/xxxxx},
  url          = {https://doi.org/10.xxxx/xxxxx}
}
```
