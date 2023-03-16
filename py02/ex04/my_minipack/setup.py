from setuptools import setup
# Configurando
setup(
		# el nombre debe coincidir con el nombre de la carpeta   
		#'modulomuysimple'
		name="my_minipack",
		version=1.0,
		summary="Howto create a package in python.",
		author="jofernan",
		author_email="<jofernan@student.42.com>",
		metadata_version=2.1,
		installer="pip",
		keywords=['python', 'primer paquete'],
		classifiers= [
			"Development Status :: 3 - Alpha",
			"Intended Audience :: Developers",
			"Intended Audience :: Students",
			"Topic :: Education",
			"License :: :: OSI Approved :: GNU General Public License v3 (GPLv3)",
			"Programming Language :: Python :: 2",
			"Programming Language :: Python :: 3 :: Only",
			"Operating System :: MacOS :: MacOS X",
			"Operating System :: Microsoft :: Windows",
		]
)