---
date: 2023-03-27
title: Modelling last glacial cycle ice dynamics in the Alps and beyond
description: From the Alps to global mountains
author: Julien Seguinot
layout: slides
---

<!-- can't be moved to template -->
<section data-markdown data-separator-notes="^:::">
<textarea data-template>

<!-- .slide: data-background-image="https://live.staticflickr.com/65535/50742648113_564f982ebc_k_d.jpg" -->

<div class="titlebox fragment fade-out">

**Modelling last glacial cycle ice dynamics** in the Alps and beyond,
[J Seguinot](https://juseg.github.io), 27 Mar 2023

</div>

---

### Kluane ice field

<!-- .slide: data-background-image="https://live.staticflickr.com/8560/28938896344_afcf0c23c1_o.jpg" -->

Photo: [R. Droker, 2013](
    https://www.flickr.com/photos/29750062@N06/28938896344/)
<!-- .element: class="credit" -->

---

### The Alps during the Last Glacial Maximum
<!-- .element: style="display: none" -->

<!-- .slide: data-background-image="https://www.glaciers-climat.com/wp-content/uploads/LGM-Alpes-Glaciers-Web.jpeg" -->

Figure: [S. Coutterand, 2023](
    https://www.glaciers-climat.com/cg/le-quaternaire-dans-les-alpes/)
<!-- .element: class="credit" -->

---

### Open questions

- What glacial **history** lead to LGM,
- was ice **flow** controlled by topography,
- what caused differences in **timing**,
- how high above trimlines was the **surface**, and
- where was glacier **erosion** significant?

~

Tool: **Parallel** Ice Sheet Model (PISM) <br><small>
 (3D energy balance, polythermal SIA, pseudo-plastic till SSA, <br>
 PDD mass balance, viscous-modulated bedrock deformation) </small>
<!-- .element class="fragment" -->

Method: simulation of the **last glacial cycle** <br><small>
 (120--0 ka, 1x1 km x 20 m, 576 processors, 33 days) </small>
<!-- .element class="fragment" -->

<!-- ### Parallel ice sheet model -->
<!-- - Shallow Shelf Approximation on pseudo-pastic till -->
<!-- - Polythermal Shallow Ice Approximation -->
<!-- - Viscous-modulated elastic lithosphere -->
<!-- - Bedrock temperature model to 3 km depth -->
<!-- - Snow precipitation before 0--2 $^\circ$C -->
<!-- - Weekly resolved positive Degree Day melt model -->
<!-- After: PISM documentation (https://pism.io). -->

---

### Present-based spatial inputs

![](https://tc.copernicus.org/articles/12/3265/2018/tc-12-3265-2018-f01-web.png)

<!-- Data: WorldClim; ERA-Interim; Goutorbe et al., 2011. -->

---

### Paleoclimate inputs

- Time-dependent **temperature** change from
  - <span class="blue">GRIP</span> Greenland ice $\delta^{18}O$
  - <span class="red">EPICA</span> Antarctic ice $\delta^{18}O$
  - <span class="green">MD01-2444</span> sediment $U^{K'}_{37}$
  - linearly scaled to LGM ice extent

- Two **precipitation** parametrizations
  - Constant in time
  - Decreased with temperature

---

### Temperature forcing and modelled ice volume

![](https://tc.copernicus.org/articles/12/3265/2018/tc-12-3265-2018-f02-web.png)

<!-- Ice volume fluctuations are **rapid**, but smaller with *EPICA* forcing. -->
<!-- These fluctuations are **smoothed**, in **reduced** precipitation runs. -->

<!-- Data: Dansgaard et al., 1993; Jouzel et al., 2007; Martrat et al., 2007 -->

---

### Visualization for outreach
<!-- .element: style="display: none" -->

<!-- .slide: data-background-iframe="https://player.vimeo.com/video/313723261?autoplay=1&loop=1&color=ffffff&title=0&byline=0&portrait=0" -->

---

### More on the Alps

- J. Seguinot, S. Ivy-Ochs, G. Jouvet, M. Huss, M. Funk, and F. Preusser.
  Modelling last glacial cycle ice dynamics in the Alps.
  [The Cryosphere](https://doi.org/10.5194/tc-12-3265-2018), 2018.

- J. Seguinot and I. Delaney.
  Last-glacial-cycle glacier erosion potential in the Alps.
  [ESurf](https://doi.org/10.5194/esurf-9-923-2021), 2021.

- Datasets
  ([aggregated](https://doi.org/10.5281/zenodo.1423159),
   [continuous](https://doi.org/10.5281/zenodo.1423175),
   [erosion](https://doi.org/10.5281/zenodo.4495418))

https://juseg.github.io/publications/

Please download, re-use, and disprove!

<!-- FIXME how much text on this slide? Acknowledge co-authors. -->

---

### Going global

<div class="r-stack">
  <img src="../assets/figures/worldmap_countries.png">
  <img src="../assets/figures/worldmap_glaciers.png" class="fragment">
  <img src="../assets/figures/worldmap_paleoglaciers.png" class="fragment">
</div>

::: Sea level equivalents:
- Antarctica: 58.3 m s.l.e. (Fretwell et al., 2013)
- Greenland: 7.3 m s.l.e. (Bamber et al., 2013)
- Additional 120 to 135 m s.l.e. (Clark and Mix, 2002)

---

<!-- .slide: data-auto-animate -->
### Alps modelling workflow

<div class='flex'>
 <div class='box flex' data-id='hyoga' style='border: none'>
  <div>
   <div class='box' data-id='t'>T</div>
   <div class='box' data-id='p'>P</div>
   <div class='box' data-id='z'>z</div>
  </div>
  <div data-id='arrow1'>→</div>
  <div>
   <div class='box blue'>Python
    <pre>pism-palseries</pre>
   </div>
   <div class='box green'>GRASS GIS
    <pre>r.in.worldclim.py</pre>
    <pre>r.out.pism.py</pre>
    <pre>...</pre>
   </div>
  </div>
  <div>
   <div class='box pink' data-id='pism'>PISM
    <pre>pism-palwrapper</pre>
   </div>
   <div>↓</div>
   <div class='box blue'>Python
    <pre>cartowik</pre>
    <pre>iceplotlib</pre>
    <pre>...</pre>
   </div>
  </div>
 </div>
 <div data-id='arrow2'>→</div>
 <div>
  <div class='box' data-id='nc'>.nc</div>
  <div class='box' data-id='pdf'>.pdf</div>
  <div class='box' data-id='mp4'>.mp4</div>
 </div>
</div>

---

<!-- .slide: data-auto-animate data-auto-animate-duration="2s" -->
### Global modelling workflow

<div class='flex'>
 <div class='box blue flex' data-id='hyoga'>
  <div>
   <div class='box' data-id='t'>T</div>
   <div class='box' data-id='p'>P</div>
   <div class='box' data-id='z'>z</div>
  </div>
  <div data-id='arrow1' style='padding: 0.5em'>→</div>
  <div class='box purple' data-id='pism'>PISM</div>
  <div style='align-self: start; padding: 1em'>hyoga</div>
 </div>
 <div data-id='arrow2' style='padding: 0.5em'>→</div>
 <div>
  <div class='box' data-id='nc'>.nc</div>
  <div class='box' data-id='pdf'>.pdf</div>
  <div class='box' data-id='mp4'>.mp4</div>
 </div>
</div>

---


### Hyoga paleoglacier modelling framework

```python [4-7|9-11|13-14|16-17]
import hyoga
import xarray

# coordinate system and bounds
domain = dict(
    crs='epsg:32632',
    bounds=[150e3, 4820e3, 1050e3, 5420e3])

# input files
hyoga.open.bootstrap(**domain).to_netcdf('boot.nc')
hyoga.open.atmosphere(**domain).to_netcdf('atm.nc')

# TODO run PISM
# pismr -i boot.nc [...] -o out.nc

# plot output
xarray.open_dataset('out.nc').hyoga.plot.ice_margin()
```

---

### Online documentation

<iframe data-src="https://hyoga.readthedocs.io" width="960" height="540"></iframe>

---

### Modelling domains

![](https://hyoga.readthedocs.io/en/world/_images/sphx_glr_plot_modelling_domains_001.png)

<!-- can't be moved to template -->
</textarea>
</section>
