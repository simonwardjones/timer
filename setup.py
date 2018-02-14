from setuptools import setup

setup(
	name='Timer',
	version='1.0.0',
	py_modules='timer',
	install_requires=['Click'],
	entry_points={
		'console_scripts':[
			'timer=timer_click:cli'
		]
	},
)

