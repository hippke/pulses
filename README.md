### Periodic Spectral Modulations arise from non-random spacing of spectral absorption lines

The code in this repository ("make_figure.py") reads the solar spectrum by [Kurucz (2005)](https://ui.adsabs.harvard.edu/#abs/2005MSAIS...8..189K/abstract), performs a spectral Fourier transform, and outputs the Figure shown below. It is intended to accompany the paper and allow for reproducible science.

![Logo](https://github.com/hippke/pulses/blob/master/1.png)

(a): Spectral Fourier Transform of the synthetic solar spectrum by \citet{2005MSAIS...8..189K,2005MSAIS...8...73K}. A sliding median with a boxcar width of 3\,\% (red line) is fitted to the spectral flux (black line). (b): After subtracting the median from the flux, a Lomb-Scargle periodogram is calculated (black). The highest peak coincides with one of the claimed pulse spacings (dashed red). (c): The median-subtracted flux (black) is shown together with the best-fit sine derived from the periodogram. (d): A zoom to show the fit of the sine to the data.

## Attribution
Please cite [Hippke (2018)](http://www.) if you find this code useful in your research. The BibTeX entry for the paper is:

```
@article{abc,
   author = {},
    title = {},
  journal = {},
     year = ,
   volume = ,
    pages = {},
   eprint = {},
      doi = {}
}
```

## Contributing Code, Bugfixes, or Feedback
I welcome and encourage contributions.

Copyright 2018 Michael Hippke
