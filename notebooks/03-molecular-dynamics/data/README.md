# Data provenance — Chapter III — Molecular Dynamics

Every file committed here, with its origin and the licence under which this
course redistributes it. The gate `tools/check_provenance.py` requires each
file to appear below on a row naming a licence, so this ledger cannot drift
out of date silently.

All entries below are **the course's own calculations** from the ETH Zürich
course *Molecular and Materials Modelling* (FS 2023, Amador / Passerone /
Pignedoli). Nothing here is third-party data, so the course redistributes it
under its own content licence, CC BY 4.0 (`LICENSE-CONTENT`). The tools that
produced it are separately licensed and are not redistributed here; output
produced by running a GPL program belongs to whoever ran it (GPLv3 section 2).

| File | What it is | Produced with | Source | Licence |
|---|---|---|---|---|
| `38atoms.xyz` | Starting configuration of the 38-atom cluster, in Å | CP2K | FS 2023 ETHZ MMM course | CC-BY-4.0 |
| `thermalization_38.inp` | Thermalisation input deck | CP2K | FS 2023 ETHZ MMM course | CC-BY-4.0 |
| `production_38.inp` | Production molecular-dynamics input deck | CP2K | FS 2023 ETHZ MMM course | CC-BY-4.0 |
| `replica-exchange.lammps` | Parallel-tempering input script | LAMMPS | FS 2023 ETHZ MMM course | CC-BY-4.0 |
| `replica-logs` | Directory of replica-exchange swap logs (`swap.log`) | LAMMPS | FS 2023 ETHZ MMM course | CC-BY-4.0 |
