---
date: 2025-06-04
title: Global glacial inception threshold from positive degree-day modelling
description: bglacier deep dive
author: Julien Seguinot, Marijke Van Cappellen, Etienne Legrain, Rodrigo Aguayo, Lander Van Tricht, Andreas Born, and Harry Zekollari
layout: slides
---

<!-- can't be moved to template -->
<section data-markdown data-separator-notes="^:::">
<textarea data-template>

# Global glacial inception threshold <br> from positive degree-day modelling

<!-- .element: style="padding-top: 2em; text-shadow: 0 0 100px #000;" -->

<div class="titlebox" >

<!-- .slide: data-background-image="https://live.staticflickr.com/65535/48968011203_c9c640445c_k.jpg" -->

<!-- **Global glacial inception threshold from positive degree-day modelling.** -->
[J. Seguinot](https://juseg.dev), M. Van Cappellen, E. Legrain, R. Aguayo, L.
Van Tricht, A. Born, and H. Zekollari. VUB, 4 Jun 2025.

</div>

---

### Glaciers and paleoglaciers

<div class="r-stack">
  <img src="../assets/figures/worldmap_glaciers.png">
  <img src="../assets/figures/worldmap_paleoglaciers.png" class="fragment">
</div>
<div>
  <span style="font-size: 1.5em">-4.8±2.5°C</span></br>
  <span style="font-size: 0.75em">(Kageyama et al., 2021)</span>
</div>

<!-- .element: class="blue fragment" style="bottom: 0; margin: 0; padding: 3em; position: absolute" -->

---

### Global degree-day modelling

- CHELSA-W5E5 ca. 1 km input climate (T, P, σ)
- Temperature offset +5.0, +4.8, ..., -20.0 K
- Postive degree-day mass balance  model

~

→ Global **glacial inception threshold**<br>
(temperature change needed to begin glacier growth)

---

### Input climatology

<img class="r-stretch" src="../assets/figures/glopdd_input_cw5e5.png">

---

### Glacial inception threshold

<img class="r-stretch" src="../assets/figures/glopdd_world_cw5e5.png">

---

### Glacial inception threshold

<img class="r-stretch" src="../assets/figures/glopdd_local_cw5e5.png">

---

### Glacial inception threshold

<img class="r-stretch" src="../assets/figures/glopdd_japan_cw5e5.png">

---

### Glacial inception areas

<img class="r-stretch" src="../assets/figures/glopdd_areas_cw5e5.png">

---

### Vs. current equilibrium lines

<div class="r-stack r-stretch">
  <img src="../assets/figures/glopdd_zonal_oggm.png">
  <img src="../assets/figures/glopdd_zonal_elas.png" class="fragment">
  <img src="../assets/figures/glopdd_zonal_cw5e5.png" class="fragment">
</div>

---

### Vs. PMIP4 and LGM equilibrium lines

<img class="r-stretch" src="../assets/figures/glopdd_pmip4_cw5e5.png">

See also poster **EGU25-6672** by Van Cappellen et al.

---

### Glacial inception on the Austria Center

<div class="multicol">
  <div class="column">
    <img src="../assets/figures/glopdd_vienna_cw5e5.png">
  </div>
  <div class="column">
    <p>(but glaciers from the Alps would flow here first)</p>
    <div style="background: white; display: flex; justify-content: space-around; padding: 0.5em 1em">
      <img height="100px" src="../assets/logos/logo_fwo.png">
      <img height="120px" src="../assets/logos/logo_egu_plain_blue.png">
    </div>
    <div style="background: white; padding: 0.5em 1em">
      <img src="../assets/logos/logo_bglacier.png">
    </div>
  </div>
</div>

---

### Glacial inception in Belgium

<img class="r-stretch" src="../assets/figures/glopdd_belux_cw5e5.png">

---

### Sensitivity to precipitation

<img class="r-stretch" src="../assets/figures/glopdd_world_pdiff.png">

---

### Sensitivity to PDD factor

<img class="r-stretch" src="../assets/figures/glopdd_world_fdiff.png">

---

### Sensitivity to input climate

<img class="r-stretch" src="../assets/figures/glopdd_world_sdiff.png">

---

### Open questions

<div class="multicol">
  <div class="column">

- Include warmer climates (a.k.a
glacial deception threshold)?
- CHELSA-ERA5 vs -W5E5?
- Calibrate degree-day factor?
- More validation against PMIP4?

</div>
  <div class="column">
    <img src="../assets/figures/glopdd_areas_cw5e5_log.png">
  </div>
</div>


<!-- can't be moved to template -->
<!-- can't be moved to template -->
</textarea>
</section>
