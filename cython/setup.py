from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("benchmarkCsv", ["benchmarkCsv.pyx"])]

setup(
	name = "Benchmark CSV",
	cmdclass = {"build_ext": build_ext},
	ext_modules = ext_modules
	)