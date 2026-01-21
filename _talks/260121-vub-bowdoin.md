---
date: 2026-01-21
title: Temperature, shear and stress in Bowdoin Glacier Northwest Greenland
description: bglacier deep dive
author: |
  Julien Seguinot, Evgeny A. Podolsky, Shin Sugiyama, Ralf Greve, and Harry
  Zekollari (and Martin Funk, Andreas Bauder, Cornelius Senn, Silvan Leinss,
  Daiki Sakakibara, and Katarina Henning)
layout: slides
---

<!-- can't be moved to template -->
<section data-markdown data-separator-notes="^:::">
<textarea data-template>

# Stress and tilt in Bowdoin Glacier, Northwest Greenland
<!-- .slide: data-background-image="https://live.staticflickr.com/65535/49298829236_2546afe01d_k.jpg" -->

[Julien Seguinot](https://juseg.dev), Evgeny A. Podolsky, Shin Sugiyama, Ralf
  Greve, and Harry Zekollari, *VUB*, 21 Jan 2026
<!-- .element: class="titlebox fragment fade-out" data-fragment-index="1" -->

---
### Bowdoin Glacier drilling sites
<img class="r-stretch" src="../assets/figures/bowtem_images.png">

---
## Stress

---
### Bowdoin borehole locations
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_bores_01.png">
  <img src="../assets/figures/bowstr_bores_02.png" class="fragment">
  <img src="../assets/figures/bowstr_bores.png" class="fragment">
</div>

---
### Three-year borehole record
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_nofil_01.png">
  <img src="../assets/figures/bowstr_nofil_02.png" class="fragment">
  <img src="../assets/figures/bowstr_nofil_03.png" class="fragment">
  <img src="../assets/figures/bowstr_nofil_04.png" class="fragment">
  <img src="../assets/figures/bowstr_nofil_05.png" class="fragment">
  <img src="../assets/figures/bowstr_nofil.png" class="fragment">
</div>

---
### Stress fast Fourier transform
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_pgram_stfft_01.png">
  <img src="../assets/figures/bowstr_pgram_stfft.png" class="fragment">
</div>

---
### Stress Lomb-Scargle periodogram
<img class="r-stretch" src="../assets/figures/bowstr_pgram_stlsp.png">

---
### Moving window spectrograms
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_sgram_stfft_01.png">
  <img src="../assets/figures/bowstr_sgram_stfft.png" class="fragment">
</div>

---
### Continuous wavelet transform
<img class="r-stretch" src="../assets/figures/bowstr_sgram_stcwt.png">

---
### Band-pass filtering
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_lines_12hbp_01.png">
  <img src="../assets/figures/bowstr_lines_12hbp.png" class="fragment">
</div>

---
### Cross-correlation over a month
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_ccorr_12hbp_01.png">
  <img src="../assets/figures/bowstr_ccorr_12hbp_02.png" class="fragment">
  <img src="../assets/figures/bowstr_ccorr_12hbp.png" class="fragment">
</div>

---
### Cross-correlation of Hilbert analytic phase
<img class="r-stretch" src="../assets/figures/bowstr_ccorr_phase.png">

---
### Moving window cross-correlation
<img class="r-stretch" src="../assets/figures/bowstr_mcorr_12hbp.png">

---
## Tilt

---
### Bowdoin tilt units
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_bores_01.png">
  <img src="../assets/figures/bowstr_bores_02.png" class="fragment">
  <img src="../assets/figures/bowstr_bores.png" class="fragment">
</div>

---
### Tilt
<img class="r-stretch" src="../assets/figures/bowdef_tilts.png">

---
### Tilt rates
<img class="r-stretch" src="../assets/figures/bowdef_rates.png">

---
### Shear profile
<img class="r-stretch" src="../assets/figures/bowdef_shear.png">

---
### Tilt fast Fourier transform
<img class="r-stretch" src="../assets/figures/bowstr_pgram_tifft.png">

---
### Preliminary findings and open questions

- Stress
    - ❕ Pressure sensors frozen in the ice show clear **tidal signal**.
    - ❔ I think we can measure **stress** in glacier.
    - ❔ We could not yet find interpretation.

- Tilt
    - ❕ **Yearly shear** of 16-19 metres is 5% of surface motion.
    - ❕ Tilt rates increase during summer **speed-up events**.
    - ❔ How to isolate **daily and tidal** signals (variable rate)?
    - ❔ Link to **basal sliding** (geopositioning, satellite, cameras)?

<!-- can't be moved to template -->
</textarea>
</section>
