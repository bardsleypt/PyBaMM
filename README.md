![PyBaMM_logo](https://user-images.githubusercontent.com/20817509/107091287-8ad46a80-67cf-11eb-86f5-7ebef7c72a1e.png)

#
<div align="center">

[![Build](https://github.com/pybamm-team/PyBaMM/workflows/PyBaMM/badge.svg)](https://github.com/pybamm-team/PyBaMM/actions?query=workflow%3APyBaMM+branch%3Adevelop)
[![readthedocs](https://readthedocs.org/projects/pybamm/badge/?version=latest)](https://pybamm.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/pybamm-team/PyBaMM/branch/main/graph/badge.svg)](https://codecov.io/gh/pybamm-team/PyBaMM)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop/)
[![DOI](https://zenodo.org/badge/DOI/10.5334/jors.309.svg)](https://doi.org/10.5334/jors.309)
[![release](https://img.shields.io/github/v/release/pybamm-team/PyBaMM?color=yellow)](https://github.com/pybamm-team/PyBaMM/releases)
[![black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-43-orange.svg)](#-contributors)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

</div>

# PyBaMM

PyBaMM (Python Battery Mathematical Modelling) solves physics-based electrochemical DAE models by using state-of-the-art automatic differentiation and numerical solvers. The Doyle-Fuller-Newman model can be solved in under 0.1 seconds, while the reduced-order Single Particle Model and Single Particle Model with electrolyte can be solved in just a few milliseconds. Additional physics can easily be included such as thermal effects, fast particle diffusion, 3D effects, and more. All models are implemented in a flexible manner, and a wide range of models and parameter sets (NCA, NMC, LiCoO2, ...) are available. There is also functionality to simulate any set of experimental instructions, such as CCCV or GITT, or specify drive cycles.

## 💻 Using PyBaMM

The easiest way to use PyBaMM is to run a 1C constant-current discharge with a model of your choice with all the default settings:
```python3
import pybamm
model = pybamm.lithium_ion.DFN()  # Doyle-Fuller-Newman model
sim = pybamm.Simulation(model)
sim.solve([0, 3600])  # solve for 1 hour
sim.plot()
```
or simulate an experiment such as CCCV:
```python3
import pybamm
experiment = pybamm.Experiment(
    [
        ("Discharge at C/10 for 10 hours or until 3.3 V",
        "Rest for 1 hour",
        "Charge at 1 A until 4.1 V",
        "Hold at 4.1 V until 50 mA",
        "Rest for 1 hour")
    ]
    * 3,
)
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, experiment=experiment, solver=pybamm.CasadiSolver())
sim.solve()
sim.plot()
```
However, much greater customisation is available. It is possible to change the physics, parameter values, geometry, submesh type,  number of submesh points, methods for spatial discretisation and solver for integration (see DFN [script](https://github.com/pybamm-team/PyBaMM/blob/develop/examples/scripts/DFN.py) or [notebook](https://github.com/pybamm-team/PyBaMM/blob/develop/examples/notebooks/models/DFN.ipynb)).

For new users we recommend the [Getting Started](https://github.com/pybamm-team/PyBaMM/tree/develop/examples/notebooks/Getting%20Started) guides. These are intended to be very simple step-by-step guides to show the basic functionality of PyBaMM, and can either be downloaded and used locally, or used online through [Google Colab](https://colab.research.google.com/github/pybamm-team/PyBaMM/blob/develop).

Further details can be found in a number of [detailed examples](https://github.com/pybamm-team/PyBaMM/blob/develop/examples/notebooks/README.md), hosted here on
github. In addition, there is a [full API documentation](http://pybamm.readthedocs.io/),
hosted on [Read The Docs](https://readthedocs.org/).
Additional supporting material can be found
[here](https://github.com/pybamm-team/pybamm-supporting-material/).

Note that the examples on the default `develop` branch are tested on the latest `develop` commit. This may sometimes cause errors when running the examples on the pybamm pip package, which is synced to the `main` branch. You can switch to the `main` branch on github to see the version of the examples that is compatible with the latest pip release.

<!-- For further examples, see the list of repositories that use PyBaMM [here](https://github.com/pybamm-team/pybamm-example-results). -->

## 🚀 Installing PyBaMM

PyBaMM is available on GNU/Linux, MacOS and Windows.
We strongly recommend to install PyBaMM within a python virtual environment, in order not to alter any distribution python files.
For instructions on how to create a virtual environment for PyBaMM, see [the documentation](https://pybamm.readthedocs.io/en/latest/install/GNU-linux.html#user-install).

### Using pip
[![pypi](https://img.shields.io/pypi/v/pybamm?color=blue)](https://pypi.org/project/pybamm/)
[![downloads](https://img.shields.io/pypi/dm/pybamm?color=blue)](https://pypi.org/project/pybamm/)

```bash
pip install pybamm
```

### Using conda
PyBaMM is available as a conda package through the conda-forge channel.

[![conda_forge](https://img.shields.io/conda/vn/conda-forge/pybamm?color=green)](https://anaconda.org/conda-forge/pybamm)
[![downloads](https://img.shields.io/conda/dn/conda-forge/pybamm?color=green)](https://anaconda.org/conda-forge/pybamm)

```bash
conda install -c conda-forge pybamm
```

### Optional solvers
Following GNU/Linux and macOS solvers are optionally available:
- [scikits.odes](https://scikits-odes.readthedocs.io/en/latest/)-based solver, see [the documentation](https://pybamm.readthedocs.io/en/latest/install/GNU-linux.html#optional-scikits-odes-solver).
- [jax](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html)-based solver, see [the documentation](https://pybamm.readthedocs.io/en/latest/install/GNU-linux.html#optional-jaxsolver).

## 📖 Citing PyBaMM

If you use PyBaMM in your work, please cite our paper

> Sulzer, V., Marquis, S. G., Timms, R., Robinson, M., & Chapman, S. J. (2021). Python Battery Mathematical Modelling (PyBaMM). _Journal of Open Research Software, 9(1)_.

You can use the bibtex

```
@article{Sulzer2021,
  title = {{Python Battery Mathematical Modelling (PyBaMM)}},
  author = {Sulzer, Valentin and Marquis, Scott G. and Timms, Robert and Robinson, Martin and Chapman, S. Jon},
  doi = {10.5334/jors.309},
  journal = {Journal of Open Research Software},
  publisher = {Software Sustainability Institute},
  volume = {9},
  number = {1},
  pages = {14},
  year = {2021}
}
```

We would be grateful if you could also cite the relevant papers. These will change depending on what models and solvers you use. To find out which papers you should cite, add the line

```python3
pybamm.print_citations()
```

to the end of your script. This will print bibtex information to the terminal; passing a filename to `print_citations` will print the bibtex information to the specified file instead. A list of all citations can also be found in the [citations file](https://github.com/pybamm-team/PyBaMM/blob/develop/pybamm/CITATIONS.txt). In particular, PyBaMM relies heavily on [CasADi](https://web.casadi.org/publications/).
See [CONTRIBUTING.md](https://github.com/pybamm-team/PyBaMM/blob/develop/CONTRIBUTING.md#citations) for information on how to add your own citations when you contribute.

## 🛠️ Contributing to PyBaMM

If you'd like to help us develop PyBaMM by adding new methods, writing documentation, or fixing embarrassing bugs, please have a look at these [guidelines](https://github.com/pybamm-team/PyBaMM/blob/develop/CONTRIBUTING.md) first.

## 📫 Get in touch

For any questions, comments, suggestions or bug reports, please see the [contact page](https://www.pybamm.org/contact).

## 📃 License

PyBaMM is fully open source. For more information about its license, see [LICENSE](https://github.com/pybamm-team/PyBaMM/blob/develop/LICENSE.txt).

## ✨ Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://sites.google.com/view/valentinsulzer"><img src="https://avatars3.githubusercontent.com/u/20817509?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Valentin Sulzer</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Atinosulzer" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tinosulzer" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tinosulzer" title="Documentation">📖</a> <a href="#example-tinosulzer" title="Examples">💡</a> <a href="#ideas-tinosulzer" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-tinosulzer" title="Maintenance">🚧</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3Atinosulzer" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tinosulzer" title="Tests">⚠️</a> <a href="#tutorial-tinosulzer" title="Tutorials">✅</a> <a href="#blog-tinosulzer" title="Blogposts">📝</a></td>
    <td align="center"><a href="http://www.robertwtimms.com"><img src="https://avatars1.githubusercontent.com/u/43040151?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Robert Timms</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Artimms" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=rtimms" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=rtimms" title="Documentation">📖</a> <a href="#example-rtimms" title="Examples">💡</a> <a href="#ideas-rtimms" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-rtimms" title="Maintenance">🚧</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3Artimms" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=rtimms" title="Tests">⚠️</a> <a href="#tutorial-rtimms" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/Scottmar93"><img src="https://avatars1.githubusercontent.com/u/22661308?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Scott Marquis</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3AScottmar93" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=Scottmar93" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=Scottmar93" title="Documentation">📖</a> <a href="#example-Scottmar93" title="Examples">💡</a> <a href="#ideas-Scottmar93" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-Scottmar93" title="Maintenance">🚧</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3AScottmar93" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=Scottmar93" title="Tests">⚠️</a> <a href="#tutorial-Scottmar93" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/martinjrobins"><img src="https://avatars3.githubusercontent.com/u/1148404?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Martin Robinson</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Amartinjrobins" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=martinjrobins" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=martinjrobins" title="Documentation">📖</a> <a href="#example-martinjrobins" title="Examples">💡</a> <a href="#ideas-martinjrobins" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3Amartinjrobins" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=martinjrobins" title="Tests">⚠️</a> <a href="#tutorial-martinjrobins" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://www.brosaplanella.com"><img src="https://avatars3.githubusercontent.com/u/28443643?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ferran Brosa Planella</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3Abrosaplanella" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Abrosaplanella" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=brosaplanella" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=brosaplanella" title="Documentation">📖</a> <a href="#example-brosaplanella" title="Examples">💡</a> <a href="#ideas-brosaplanella" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-brosaplanella" title="Maintenance">🚧</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=brosaplanella" title="Tests">⚠️</a> <a href="#tutorial-brosaplanella" title="Tutorials">✅</a> <a href="#blog-brosaplanella" title="Blogposts">📝</a></td>
    <td align="center"><a href="https://github.com/TomTranter"><img src="https://avatars3.githubusercontent.com/u/7068741?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tom Tranter</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3ATomTranter" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=TomTranter" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=TomTranter" title="Documentation">📖</a> <a href="#example-TomTranter" title="Examples">💡</a> <a href="#ideas-TomTranter" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3ATomTranter" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=TomTranter" title="Tests">⚠️</a> <a href="#tutorial-TomTranter" title="Tutorials">✅</a></td>
    <td align="center"><a href="http://tlestang.github.io"><img src="https://avatars3.githubusercontent.com/u/13448239?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Thibault Lestang</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Atlestang" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tlestang" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tlestang" title="Documentation">📖</a> <a href="#example-tlestang" title="Examples">💡</a> <a href="#ideas-tlestang" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3Atlestang" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tlestang" title="Tests">⚠️</a> <a href="#infra-tlestang" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/research-software-engineering/"><img src="https://avatars1.githubusercontent.com/u/6095790?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Diego</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Adalonsoa" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3Adalonsoa" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=dalonsoa" title="Code">💻</a> <a href="#infra-dalonsoa" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/felipe-salinas"><img src="https://avatars2.githubusercontent.com/u/64426781?v=4?s=100" width="100px;" alt=""/><br /><sub><b>felipe-salinas</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=felipe-salinas" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=felipe-salinas" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/suhaklee"><img src="https://avatars3.githubusercontent.com/u/57151989?v=4?s=100" width="100px;" alt=""/><br /><sub><b>suhaklee</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=suhaklee" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=suhaklee" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/viviantran27"><img src="https://avatars0.githubusercontent.com/u/6379429?v=4?s=100" width="100px;" alt=""/><br /><sub><b>viviantran27</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=viviantran27" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=viviantran27" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/gyouhoc"><img src="https://avatars0.githubusercontent.com/u/60714526?v=4?s=100" width="100px;" alt=""/><br /><sub><b>gyouhoc</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Agyouhoc" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=gyouhoc" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=gyouhoc" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/YannickNoelStephanKuhn"><img src="https://avatars0.githubusercontent.com/u/62429912?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Yannick Kuhn</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=YannickNoelStephanKuhn" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=YannickNoelStephanKuhn" title="Tests">⚠️</a></td>
    <td align="center"><a href="http://batterymodel.co.uk"><img src="https://avatars2.githubusercontent.com/u/39409226?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jacqueline Edge</b></sub></a><br /><a href="#ideas-jedgedrudd" title="Ideas, Planning, & Feedback">🤔</a> <a href="#eventOrganizing-jedgedrudd" title="Event Organizing">📋</a> <a href="#fundingFinding-jedgedrudd" title="Funding Finding">🔍</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.rse.ox.ac.uk/"><img src="https://avatars3.githubusercontent.com/u/3770306?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Fergus Cooper</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=fcooper8472" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=fcooper8472" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/jonchapman1"><img src="https://avatars1.githubusercontent.com/u/28925818?v=4?s=100" width="100px;" alt=""/><br /><sub><b>jonchapman1</b></sub></a><br /><a href="#ideas-jonchapman1" title="Ideas, Planning, & Feedback">🤔</a> <a href="#fundingFinding-jonchapman1" title="Funding Finding">🔍</a></td>
    <td align="center"><a href="https://github.com/colinplease"><img src="https://avatars3.githubusercontent.com/u/44977104?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Colin Please</b></sub></a><br /><a href="#ideas-colinplease" title="Ideas, Planning, & Feedback">🤔</a> <a href="#fundingFinding-colinplease" title="Funding Finding">🔍</a></td>
    <td align="center"><a href="https://github.com/cwmonroe"><img src="https://avatars.githubusercontent.com/u/92099819?v=4?s=100" width="100px;" alt=""/><br /><sub><b>cwmonroe</b></sub></a><br /><a href="#ideas-cwmonroe" title="Ideas, Planning, & Feedback">🤔</a> <a href="#fundingFinding-cwmonroe" title="Funding Finding">🔍</a></td>
    <td align="center"><a href="https://github.com/gjo97"><img src="https://avatars.githubusercontent.com/u/18349157?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Greg</b></sub></a><br /><a href="#ideas-gjo97" title="Ideas, Planning, & Feedback">🤔</a> <a href="#fundingFinding-gjo97" title="Funding Finding">🔍</a></td>
    <td align="center"><a href="https://faraday.ac.uk"><img src="https://avatars2.githubusercontent.com/u/42166506?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Faraday Institution</b></sub></a><br /><a href="#financial-FaradayInstitution" title="Financial">💵</a></td>
    <td align="center"><a href="https://github.com/bessman"><img src="https://avatars3.githubusercontent.com/u/1999462?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexander Bessman</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Abessman" title="Bug reports">🐛</a> <a href="#example-bessman" title="Examples">💡</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/dalbamont"><img src="https://avatars1.githubusercontent.com/u/19659095?v=4?s=100" width="100px;" alt=""/><br /><sub><b>dalbamont</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=dalbamont" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/anandmy"><img src="https://avatars1.githubusercontent.com/u/34894671?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Anand Mohan Yadav</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=anandmy" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/weilongai"><img src="https://avatars1.githubusercontent.com/u/41424174?v=4?s=100" width="100px;" alt=""/><br /><sub><b>WEILONG AI</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=weilongai" title="Code">💻</a> <a href="#example-weilongai" title="Examples">💡</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=weilongai" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/lonnbornj"><img src="https://avatars2.githubusercontent.com/u/35983543?v=4?s=100" width="100px;" alt=""/><br /><sub><b>lonnbornj</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=lonnbornj" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=lonnbornj" title="Tests">⚠️</a> <a href="#example-lonnbornj" title="Examples">💡</a></td>
    <td align="center"><a href="https://github.com/priyanshuone6"><img src="https://avatars.githubusercontent.com/u/64051212?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Priyanshu Agarwal</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=priyanshuone6" title="Tests">⚠️</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=priyanshuone6" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Apriyanshuone6" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3Apriyanshuone6" title="Reviewed Pull Requests">👀</a> <a href="#maintenance-priyanshuone6" title="Maintenance">🚧</a> <a href="#tutorial-priyanshuone6" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/DrSOKane"><img src="https://avatars.githubusercontent.com/u/42972513?v=4?s=100" width="100px;" alt=""/><br /><sub><b>DrSOKane</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=DrSOKane" title="Code">💻</a> <a href="#example-DrSOKane" title="Examples">💡</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=DrSOKane" title="Documentation">📖</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=DrSOKane" title="Tests">⚠️</a> <a href="#tutorial-DrSOKane" title="Tutorials">✅</a></td>
    <td align="center"><a href="https://github.com/Saransh-cpp"><img src="https://avatars.githubusercontent.com/u/74055102?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Saransh Chopra</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=Saransh-cpp" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=Saransh-cpp" title="Tests">⚠️</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=Saransh-cpp" title="Documentation">📖</a> <a href="#tutorial-Saransh-cpp" title="Tutorials">✅</a> <a href="https://github.com/pybamm-team/PyBaMM/pulls?q=is%3Apr+reviewed-by%3ASaransh-cpp" title="Reviewed Pull Requests">👀</a> <a href="#maintenance-Saransh-cpp" title="Maintenance">🚧</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/DavidMStraub"><img src="https://avatars.githubusercontent.com/u/10965193?v=4?s=100" width="100px;" alt=""/><br /><sub><b>David Straub</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3ADavidMStraub" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=DavidMStraub" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/maurosgroi"><img src="https://avatars.githubusercontent.com/u/37576773?v=4?s=100" width="100px;" alt=""/><br /><sub><b>maurosgroi</b></sub></a><br /><a href="#ideas-maurosgroi" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/asinghgaba"><img src="https://avatars.githubusercontent.com/u/77078706?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Amarjit Singh Gaba</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=asinghgaba" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/KennethNwanoro"><img src="https://avatars.githubusercontent.com/u/78538806?v=4?s=100" width="100px;" alt=""/><br /><sub><b>KennethNwanoro</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=KennethNwanoro" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=KennethNwanoro" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/alibh95"><img src="https://avatars.githubusercontent.com/u/65511923?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ali Hussain Umar Bhatti</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=alibh95" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=alibh95" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/molel-gt"><img src="https://avatars.githubusercontent.com/u/81125862?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Leshinka Molel</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=molel-gt" title="Code">💻</a> <a href="#ideas-molel-gt" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/tobykirk"><img src="https://avatars.githubusercontent.com/u/42966045?v=4?s=100" width="100px;" alt=""/><br /><sub><b>tobykirk</b></sub></a><br /><a href="#ideas-tobykirk" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tobykirk" title="Code">💻</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=tobykirk" title="Tests">⚠️</a> <a href="#tutorial-tobykirk" title="Tutorials">✅</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/chuckliu1979"><img src="https://avatars.githubusercontent.com/u/13491954?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Chuck Liu</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Achuckliu1979" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=chuckliu1979" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/partben"><img src="https://avatars.githubusercontent.com/u/88316576?v=4?s=100" width="100px;" alt=""/><br /><sub><b>partben</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=partben" title="Documentation">📖</a></td>
    <td align="center"><a href="https://gavinw.me"><img src="https://avatars.githubusercontent.com/u/6828967?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Gavin Wiggins</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Awigging" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=wigging" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/dion-w"><img src="https://avatars.githubusercontent.com/u/91852142?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dion Wilde</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Adion-w" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=dion-w" title="Code">💻</a></td>
    <td align="center"><a href="https://www.ehtec.co"><img src="https://avatars.githubusercontent.com/u/48386220?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Elias Hohl</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=ehtec" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/KAschad"><img src="https://avatars.githubusercontent.com/u/93784399?v=4?s=100" width="100px;" alt=""/><br /><sub><b>KAschad</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3AKAschad" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Vaibhav-Chopra-GT"><img src="https://avatars.githubusercontent.com/u/92637595?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vaibhav-Chopra-GT</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/commits?author=Vaibhav-Chopra-GT" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/bardsleypt"><img src="https://avatars.githubusercontent.com/u/54084289?v=4?s=100" width="100px;" alt=""/><br /><sub><b>bardsleypt</b></sub></a><br /><a href="https://github.com/pybamm-team/PyBaMM/issues?q=author%3Abardsleypt" title="Bug reports">🐛</a> <a href="https://github.com/pybamm-team/PyBaMM/commits?author=bardsleypt" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
