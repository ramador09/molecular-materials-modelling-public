# Chapter VII — Data and Descriptors

The methods of the earlier chapters each compute a property from a structure directly:
solve for the electrons, integrate the equations of motion, sum the hills. Machine
learning proposes instead to *fit* that map from examples — which changes the central
question from how to compute the property to how to present the structure.

These three notebooks restore Lectures 10 and 11, which the original exercise set
announced but never delivered. The first builds a **descriptor**: a representation of an
atomic environment that is invariant to translation, rotation and relabelling by
construction, and whose blind spots can be established by proof rather than discovered
later in a model that quietly cannot represent what it was asked to. The second takes
those descriptors as data and asks the questions that follow — how to project a
high-dimensional set of environments down to something a person can look at, and how to
choose a small, representative subset of a large ensemble to compute expensively. The
third closes the loop and **fits a potential**: a curated dataset, kernel ridge
regression by exact linear algebra, the learning curve that prices every training
label, and a precise measurement of where the fitted model fails silently — and of the
one cheap number that flags the failure before it is used.

Unlike the rest of this course these notebooks use no committed calculation. Every
structure is built from its lattice definition, so every number can be re-derived from
scratch.

```{admonition} Source lectures
:class: note
This chapter develops **Lectures 10 and 11** of *Molecular and Materials
Modelling* (FS 2023) — *machine learning for atomistic systems* and
*dimensionality reduction and sampling* — as new exercises designed by the
author, the original exercise set having announced these lectures without
delivering them. Each notebook repeats its provenance in its overview; the full
lecture map is in `manifest.yml`.
```

```{tableofcontents}
```
