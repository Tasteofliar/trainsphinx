# steps

## install package
1. install sphinx and ``read the docs`` theme

    ``pip install -U sphinx, sphinx_rtd_theme``
---
## folder structure example
```
module/
    src/
        foo.py
        bar.py
    docs/
        build/
        source/
            conf.py
            index.rst
            src.rst
            modules.rst
```
---
## sphinx
1. initial sphinx 
    ``sphinx-quickstart docs``

2. setup conf.py

    - เพิ่มโค๊ดชุดนี้ในหัวไฟล์ เพื่อเพิ่ม module path ให้ sphinx รู้จัก
        ```python
        import os
        import sys

        sys.path.insert(0, os.path.abspath('../..'))
        ```

    - เพิ่ม extensions เข้าไปใน list
        ```python
        extensions = [
            'sphinx.ext.autodoc'
        ]
        ```
    - เปลี่ยน value ของตัวแปร ``html_theme`` เป็น ``sphinx_rtd_theme``
        ```python
        html_theme = 'sphinx_rtd_theme'
        ```
3. แก้ไขไฟล์ docs/source/index.rst โดยกรเพิ่ม ``modules`` เข้าไปภายใต้ ``.. toctree::``

        
        .. trainsphinx documentation master file, created by
        sphinx-quickstart on Fri Nov 10 15:07:20 2023.
        You can adapt this file completely to your liking, but it should at least
        contain the root `toctree` directive.

        Welcome to trainsphinx's documentation!
        =======================================

        .. toctree::
        :maxdepth: 2
        :caption: Contents:

        modules


        Indices and tables
        ==================

        * :ref:`genindex`
        * :ref:`modindex`
        * :ref:`search`

4. ``sphinx-apidoc -o docs/source <module>``

5. ``sphinx-build -M html docs/source docs/build``

---