### Periodic Spectral Modulations Arise from Non-random Spacing of Spectral Absorption Lines

The code in this repository ("make_figure.py") reads a synthetic solar spectrum, performs a spectral Fourier transform, and outputs the Figure shown below. It is intended to accompany the paper and allow for reproducible science.

![Logo](https://github.com/hippke/pulses/blob/master/1.png)

(a): Spectral Fourier Transform of the synthetic solar spectrum by [Kurucz (2005)](https://ui.adsabs.harvard.edu/#abs/2005MSAIS...8..189K/abstract). A sliding median with a boxcar width of 3 % (red line) is fitted to the spectral flux (black line). (b): After subtracting the median from the flux, a Lomb-Scargle periodogram is calculated (black). The highest peak coincides with one of the claimed pulse spacings (dashed red). (c): The median-subtracted flux (black) is shown together with the best-fit sine derived from the periodogram. (d): A zoom to show the fit of the sine to the data.

## Attribution
Please cite [Hippke (2019)](https://ui.adsabs.harvard.edu/#abs/2019MNRAS.482.2442H/abstract) if you find this code useful in your research. The BibTeX entry for the paper is:

```
@ARTICLE{2019MNRAS.482.2442H,
       author = {{Hippke}, Michael},
        title = "{The spectral Petersen diagram as a new tool to map pulsation modes in variable stars}",
      journal = {\mnras},
     keywords = {methods: numerical, surveys, stars: variables: RR Lyrae, Astrophysics - Solar and Stellar Astrophysics},
         year = 2019,
        month = Jan,
       volume = {482},
        pages = {2442-2446},
          doi = {10.1093/mnras/sty2790},
archivePrefix = {arXiv},
       eprint = {1810.06084},
 primaryClass = {astro-ph.SR},
       adsurl = {https://ui.adsabs.harvard.edu/\#abs/2019MNRAS.482.2442H},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

## Contributing Code, Bugfixes, or Feedback
I welcome and encourage contributions.

Copyright 2018 Michael Hippke
