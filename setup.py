#!/usr/bin/env python

from distutils.core import setup

long_description = """
A Pure-Python library built as a PDF toolkit.  It is capable of:
    
- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encrypting and decrypting PDF files.

By being Pure-Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.
"""

ext_modules = []

ext_modules.append(Extension("pyPdf.generic", ["pyPdf\\generic.py"], include_dirs=["."]))
ext_modules.append(Extension("pyPdf.utils", ["pyPdf\\utils.py"], include_dirs=["."]))
ext_modules.append(Extension("pyPdf.filters", ["pyPdf\\filters.py"], include_dirs=["."]))
ext_modules.append(Extension("pyPdf.pdf", ["pyPdf\\pdf.py"], include_dirs=["."]))
#ext_modules.append(Extension("pyPdf.xmp", ["pyPdf\\xmp.py"], include_dirs=["."]))

setup(
        name="pyPdf",
        cmdclass     = {"build_ext": build_ext},
        script_args  = ["build_ext", "--compiler=mingw32", "--inplace"],
        ext_modules  = ext_modules
    )

setup(
        name="pyPdf",
        version="1.13",
        description="PDF toolkit",
        long_description=long_description,
        author="Mathieu Fenniak",
        author_email="biziqe@mathieu.fenniak.net",
        url="http://pybrary.net/pyPdf/",
        download_url="http://pybrary.net/pyPdf/pyPdf-1.13.tar.gz",
        classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        packages=["pyPdf"],
    )

