### Periodic Spectral Modulations Arise from Non-random Spacing of Spectral Absorption Lines

The code in this repository (``make_figure.py``) reads a synthetic solar spectrum, performs a spectral Fourier transform, and outputs the Figure shown below. It is intended to accompany the paper and allow for reproducible science.

![Logo](https://github.com/hippke/pulses/blob/master/1.png)

(a): Spectral Fourier Transform of the synthetic solar spectrum by [Kurucz (2005)](https://ui.adsabs.harvard.edu/#abs/2005MSAIS...8..189K/abstract). A sliding median with a boxcar width of 3 % (red line) is fitted to the spectral flux (black line). (b): After subtracting the median from the flux, a Lomb-Scargle periodogram is calculated (black). The highest peak coincides with one of the claimed pulse spacings (dashed red). (c): The median-subtracted flux (black) is shown together with the best-fit sine derived from the periodogram. (d): A zoom to show the fit of the sine to the data.



## Attribution
Please cite Hippke (2019, PASP in press, [ADS](https://ui.adsabs.harvard.edu/#abs/2019arXiv190100523H/abstract), [PDF](https://arxiv.org/pdf/1901.00523.pdf)) if you find this code useful in your research. The BibTeX entry for the paper is:

```
@ARTICLE{2019arXiv190100523H,
       author = {{Hippke}, Michael},
        title = "{Periodic Spectral Modulations Arise from Non-random Spacing of Spectral Absorption Lines}",
      journal = {arXiv e-prints},
     keywords = {Astrophysics - Instrumentation and Methods for Astrophysics},
         year = 2019,
        month = Jan,
          eid = {arXiv:1901.00523},
        pages = {arXiv:1901.00523},
archivePrefix = {arXiv},
       eprint = {1901.00523},
 primaryClass = {astro-ph.IM},
       adsurl = {https://ui.adsabs.harvard.edu/\#abs/2019arXiv190100523H},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

## Contributing Code, Bugfixes, or Feedback
I welcome and encourage contributions. If you have any trouble, [open an issue](https://github.com/hippke/pulses/issues).

Copyright 2019 Michael Hippke
