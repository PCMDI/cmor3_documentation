# CMOR Documentation
Hosted at [cmor.llnl.gov](cmor.llnl.gov)

## Building and displaying the doc

This documentation is made with [Jekyll](https://jekyllrb.com/).

### Creating a Jekyll environment with Conda on MacOS

Our preferred method of installing Jekyll is through a Conda environment.

Download and install [Miniforge](https://conda-forge.org/download), and then use the following commands.

```
mamba create -n jekyll_env -c conda-forge ruby clang_osx-64 clangxx_osx-64
mamba activate jekyll_env
bundle install
bundle exec jekyll serve
```

## Contributors

[![Contributors](https://contrib.rocks/image?repo=PCMDI/cmor3_documentation)](https://github.com/PCMDI/cmor3_documentation/graphs/contributors)

## Acknowledgement

Content in this repository is developed by climate and computer scientists from the Program for Climate Model Diagnosis and Intercomparison ([PCMDI][PCMDI]) at Lawrence Livermore National Laboratory ([LLNL][LLNL]). This work is sponsored by the Regional and Global Model Analysis ([RGMA][RGMA]) program, of the Earth and Environmental Systems Sciences Division ([EESSD][EESSD]) in the Office of Biological and Environmental Research ([BER][BER]) within the [Department of Energy][DOE]'s [Office of Science][OS]. The work is performed under the auspices of the U.S. Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344.

<p>
    <img src="https://github.com/PCMDI/assets/blob/main/DOE/480px-DOE_Seal_Color.png?raw=true"
         width="65"
         style="margin-right: 30px"
         title="United States Department of Energy"
         alt="United States Department of Energy"
    >&nbsp;
    <img src="https://github.com/PCMDI/assets/blob/main/LLNL/212px-LLNLiconPMS286-WHITEBACKGROUND.png?raw=true"
         width="65"
         title="Lawrence Livermore National Laboratory"
         alt="Lawrence Livermore National Laboratory"
    >
</p>

[PCMDI]: https://pcmdi.llnl.gov/
[LLNL]: https://www.llnl.gov/
[RGMA]: https://climatemodeling.science.energy.gov/program/regional-global-model-analysis
[EESSD]: https://science.osti.gov/ber/Research/eessd
[BER]: https://science.osti.gov/ber
[DOE]: https://www.energy.gov/
[OS]: https://science.osti.gov/

## Release

The code of CMOR is released under the BSD 3-Clause License. For more details, see the [LICENSE](LICENSE) File.

LLNL-CODE-2005936
