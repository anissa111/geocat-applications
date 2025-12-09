.. geocat-applications documentation main file
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. module:: geocat.applications

.. meta::
   :description: geocat-applications
   :keywords: geocat, geocat-applications,
              geocat applications,
              wrf, python, wrf-python, weather research and forecasting,
              weather research and forecasting model, model, weather,
              numerical weather prediction, model, matplotlib, cartopy,
              wrf-arw, arw, ncar, ucar, cisl, ncl, ncar command language,
              national center for atmospheric research,
              university corporation for atmospheric research,
              pynio, pyngl, interpolation





GeoCAT Applications
===================

GeoCAT Applications is a community resource managed by the GeoCAT team. Inspired by the
`NCL Applications <https://www.ncl.ucar.edu/Applications/>`_ page, GeoCAT Applications is
designed to be a quick reference guide demonstrating capabilities within the scientific
Python ecosystem that may be relevant to your geoscience workflows.

New to Python or GeoCAT Applications? Check out the `Getting Started <GETTING_STARTED.md>`_ guide!

Python Applications
-------------------

.. grid:: 3
    :gutter: 2

    .. grid-item::

        .. grid:: 1
            :gutter: 1

            .. card:: Time

                - `Dates and times <./applications/datetime.ipynb>`__

    .. grid-item::

        .. grid:: 1
            :gutter: 1

            .. card:: Math

                - `General applied math <./applications/general_applied_math.ipynb>`__
                - `Spectral analysis <./applications/spectral_analysis.ipynb>`__

    .. grid-item::

        .. grid:: 1
            :gutter: 1

            .. card:: Geoscience

                - `Climatology <./applications/climatology.ipynb>`_
                - `Humid heat metrics <./applications/humid_heat_metrics.ipynb>`__

.. TIP::
    If you're looking for NCL to Python examples, please visit :ref:`ncl_applications`.


.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Overview

    Getting Started <GETTING_STARTED.md>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Python

    Applications <applications/applications>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: NCL to Python

    NCL Index <ncl/ncl_index/ncl_index>
    Applications <ncl/ncl_entries/ncl_entries>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Contributing

    Code of Conduct <CODE_OF_CONDUCT.md>
    Contributor Guide <CONTRIBUTING.md>

.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: Support

    GitHub Issues <https://github.com/NCAR/geocat-applications/issues>
    Suggestion Box <https://forms.gle/6DTo3ELLri4DAGfG8>
