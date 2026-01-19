---
date: 2025-10-29
title: Can we measure stress in glaciers?
description: 8th International Symposium on Arctic Research
author: Julien Seguinot, Evgeny A. Podolskiy, Shin Sugiyama, Harry Zekollari
layout: slides
---

<!-- can't be moved to template -->
<section data-markdown data-separator-notes="^:::">
<textarea data-template>

# Can we measure stress in glaciers?
<!-- .slide: data-background-image="https://live.staticflickr.com/65535/49298829236_2546afe01d_k.jpg" -->

[Julien Seguinot](https://juseg.dev), Evgeny A. Podolskiy, Shin Sugiyama,
Harry Zekollari. **Return of the Bowdoin Glacier: measuring the dark side of
the force**. *ISAR-8*, 29 Oct 2025.
<!-- .element: class="titlebox fragment fade-out" data-fragment-index="1" -->

::: TODO
- partial figures for boreholes, timeseries, etc?
- highpass filter cut-off frequencies are different

---
### Bowdoin Glacier drilling site
<!-- .slide: data-background-image="https://live.staticflickr.com/65535/49298343083_3bfbd1cc01_k.jpg" -->

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
### Fast Fourier transform
<div class="r-stack r-stretch">
  <img src="../assets/figures/bowstr_pgram_stfft_01.png">
  <img src="../assets/figures/bowstr_pgram_stfft.png" class="fragment">
</div>

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
### Can we measure stress in glaciers?
I think so.

---
### Please come see my poster
<!-- .slide: data-background-image="https://live.staticflickr.com/65535/54855949773_43d970b093_k.jpg" -->
<img class="r-stretch" style="float: right"
  src="../assets/figures/poster-251029-isar8-inception.jpg">

---
### Appendix -- rolling-window spectrograms
<img class="r-stretch" src="../assets/figures/bowstr_sgram_stfft.png">

---
### Appendix -- wavelet transforms
<img class="r-stretch" src="../assets/figures/bowstr_sgram_stcwt.png">

---
### Appendix -- rolling-window cross-correlation
<img class="r-stretch" src="../assets/figures/bowstr_mcorr_12hbp.png">

<!-- can't be moved to template -->
</textarea>
</section>
