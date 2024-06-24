---
date: 2024-06-25
title: Last-glacial-cycle glacier erosion potential in the Alps.
author: Julien Seguinot, Ian Delaney
layout: slides
---

<!-- can't be moved to template -->
<section data-markdown data-separator-notes="^:::">
<textarea data-template>

<!-- 1. EROSION IN THE ALPS ------------------------------------------------->

<!-- .slide: data-background-image="https://live.staticflickr.com/65535/48844296952_0d9aa1b952_k.jpg" -->

<div class="titlebox fragment fade-out" data-fragment-index="1" >

**Last-glacial-cycle glacier erosion potential in the Alps**,
[J. Seguinot](https://juseg.dev), I. Delaney, 25 Apr 2024.

</div>

---

### Empirical glacier erosion laws

<div class="flex">
  <div>
    $$ \dot{e} = K_\mathrm{g} u_\mathrm{b}^l $$
  </div>
  <div class="fragment">
$$ e =  K_\mathrm{g} \int u_\mathrm{b}^l dt $$
  </div>
</div>

K        | l        | Reference
-------- | -------- | -----------
1e-4     | 1        | [Humphrey & Raymond (1994)](https://doi.org/10.3189/s0022143000012429)
2.7e-7   | 2.02     | [Herman et al. (2015)](https://doi.org/10.1126/science.aab2386)
5.2e-11  | 2.34     | [Koppes et al. (2015)](https://doi.org/10.1038/nature15385) <strong class="fragment">< today</span>
1.665e-4 | 0.6459   | [Cook et al. (2020)](https://doi.org/10.1038/s41467-020-14583-8)

---

### Erosion rate animation
<!-- .element: style="display: none" -->

<!-- .slide: data-background-iframe="https://player.vimeo.com/video/503162771?autoplay=1&loop=1&color=ffffff&title=0&byline=0&portrait=0" -->

---

### Cumulative erosion potential

![alpero-f01](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f01-web.png) <!-- .element: height="540" -->

---

### Erosion volumes animation
<!-- .element: style="display: none" -->

<!-- .slide: data-background-iframe="https://player.vimeo.com/video/512478926?autoplay=1&loop=1&color=ffffff&title=0&byline=0&portrait=0" -->

---

### Potential erosion volumes

![alpero-f02](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f02-web.png) <!-- .element: height="540" -->

---

### Climate control on erosion

![alpero-f07](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f07-web.png) <!-- .element: height="540" -->

---

### Erosion spatial migration

![alpero-f03](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f03-web.png)

---

### Erosion altitude animation
<!-- .element: style="display: none" -->

<!-- .slide: data-background-iframe="https://player.vimeo.com/video/512479008?autoplay=1&loop=1&color=ffffff&title=0&byline=0&portrait=0" -->

---

### Potential erosion "hypsogram"

![alpero-f04](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f04-web.png)

---

### Conclusions

- Very strong localization of rapid erosion.
- Gravity accelerates erosion during ice retreat.
- Erosion slowdown counterbalances ice expansion.
- Rapid erosion migrates with glacier fluctuations.
- Alpine landscape carved in varied glacial stages.

![alpero-f08](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f08-web.jpg)

---

### More on glacial erosion

- J. Seguinot and I. Delaney.
  Last-glacial-cycle glacier erosion potential in the Alps.
  [ESurf](https://doi.org/10.5194/esurf-9-923-2021), 2021.

- Datasets
  ([aggregated](https://doi.org/10.5281/zenodo.1423159),
   [continuous](https://doi.org/10.5281/zenodo.1423175),
   [erosion](https://doi.org/10.5281/zenodo.4495418))

https://juseg.dev/publications/

---

<!-- 2. GOING GLOBAL -------------------------------------------------------->

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
  <div class='box purple' data-id='pism'>CF-ISM</div>
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


<!-- .slide: data-visibility="uncounted" -->
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

<iframe data-src="https://hyoga.io" width="960" height="540"></iframe>

---

### Made on Anafi <!-- .element style="top: 1em" -->

<!-- .slide: data-background-image="https://live.staticflickr.com/65535/53812749789_bc7d5994b9_k.jpg" -->

![EGU](https://www.earth-surface-dynamics.net/graphic_egu_logo_white.png)
![Copernicus](https://www.earth-surface-dynamics.net/template_logo_copernicus_publications_177x22_white.png)

<!-- .element style="float:right; margin-top: 1em; height: var(--r-heading3-size)" -->

---

<!-- 3. APPENDIX SLIDES ----------------------------------------------------->

<!-- .slide: data-visibility="uncounted" -->
### Modelling setup

Tool: **Parallel** Ice Sheet Model ([PISM](https://pism.io)) <br><small>
 (3D enthalpy balance, polythermal SIA, pseudo-plastic till SSA, <br>
 PDD mass balance, bedrock heat diffusion, viscoelastic lithosphere) </small>

Method: simulation of the **last glacial cycle** <br><small>
 (120--0 ka, 1x1 km x 20 m, 576 processors, 33 days) </small>

---

<!-- .slide: data-visibility="uncounted" -->
### Present-based spatial inputs

![alpcyc-f01](https://tc.copernicus.org/articles/12/3265/2018/tc-12-3265-2018-f01-web.png)

<!-- Data: WorldClim; ERA-Interim; Goutorbe et al., 2011. -->

---

<!-- .slide: data-visibility="uncounted" -->
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

<!-- .slide: data-visibility="uncounted" -->
### Temperature forcing and modelled ice volume

![alpcyc-f02](https://tc.copernicus.org/articles/12/3265/2018/tc-12-3265-2018-f02-web.png)

<!-- Ice volume fluctuations are **rapid**, but smaller with *EPICA* forcing. -->
<!-- These fluctuations are **smoothed**, in **reduced** precipitation runs. -->

<!-- Data: Dansgaard et al., 1993; Jouzel et al., 2007; Martrat et al., 2007 -->

---

<!-- .slide: data-visibility="uncounted" -->
### Sensitivity to paleoclimate

![alpero-f05](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f05-web.png)

---

<!-- .slide: data-visibility="uncounted" -->
### Sensitivity to erosion law

![alpero-f06](https://esurf.copernicus.org/articles/9/923/2021/esurf-9-923-2021-f06-web.png) <!-- .element: height="540" -->

---

<!-- .slide: data-visibility="uncounted" -->
### Modelling domains

![Hyoga domains](https://hyoga.readthedocs.io/en/world/_images/sphx_glr_plot_modelling_domains_001.png)

<!-- can't be moved to template -->
</textarea>
</section>
