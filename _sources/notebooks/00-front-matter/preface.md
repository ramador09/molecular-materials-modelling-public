# Molecular and Materials Modelling

*A Computational Materials Science Notebook Companion* — by Raymond Amador.

This is a companion to the graduate course **Molecular and Materials Modelling**,
taught at ETH Zürich. It teaches the methods of computational materials science —
Monte Carlo and molecular dynamics, electronic structure, reaction paths, and
machine-learning descriptors — *by computation and visualisation*: every idea is
something you run, plot, and check, not just read.

## How these notebooks are built

Each notebook is self-contained and follows the same shape, so the series reads as
one coherent work:

- a short **theory in brief** — a genuine review of the governing equations, not a
  textbook chapter, with full derivations deferred to the literature;
- a sequence of **guided exercises**, each stating exactly what to compute and why,
  with a labelled setup figure where a physical configuration is described;
- an independent **validation** at the end of every exercise. This is the rule that
  matters most: a result is not finished until it is checked against something the
  computation did *not* assume — an exact limit, a conservation law, a closed-form
  result (Onsager's $T_c$), or an exact enumeration. The checks print a ✓/✗ line
  and *fail the build* if the physics is wrong, so the published site is
  trustworthy by construction.

A word on reading a check: a ✗ means the output did not match what the validation
expected. That can be a real error, a different-but-valid convention, or simply
Monte Carlo noise against a tight tolerance — so treat it as a prompt to locate
the discrepancy, never an automatic verdict. We also validate only what the code
*honestly* reproduces; where a phenomenon needs physics beyond a clean, fast
implementation, we show it qualitatively and say what is missing rather than
overclaim.

Animations appear only where motion or evolution is the point; figures and
equations are numbered continuously and cross-referenced ("Fig. 7", "Eq. 12").
Where the physics is dimensionless we use natural units and say so.

## How to use them

Every page has a **download** button and **launch** buttons (Binder/Colab) in the
toolbar — take a notebook and run it yourself. The published notebooks ship
**without the worked solutions**: you see each problem, the resulting figures, and
the validation outcomes, but not the answer code. If you would like the reference
solutions — to teach from, or to check your own work — the contact is in the
footer of any page.

## Organisation, and continuity with the course

The notebooks are grouped **thematically** into volumes rather than in strict
lecture order, because related methods (say, Monte Carlo in equilibrium and in
real time) belong together. Continuity with the original course is preserved a
different way: **every notebook states the lecture it develops, with the number
explicit**, both in its banner and in its overview. The FS 2023 course numbered
its lectures and exercises together (Lecture/Exercise 1 … 13); the full map lives
in `manifest.yml`, and each volume's landing page lists the lectures it draws on.

## Acknowledgement and provenance

These materials are based on the lecture and exercise materials of *Molecular and
Materials Modelling* at **ETH Zürich and Empa (FS 2023)**, developed by
**Prof. Dr. Daniele Passerone** (lectures), **Dr. Carlo Pignedoli**, and the
author (exercises) — the author having led the exercise sessions for three years.
Each notebook is *largely, though not always verbatim,* based on that material:
where a topic was Dr. Pignedoli's, the author adopts, reimplements, and rephrases
it; elsewhere the author's exercises develop Prof. Passerone's lectures. Here it is
all synthesised, expanded, and restyled into a single companion. The same credit
appears in the footer of every page.

## Volumes

```{tableofcontents}
```
