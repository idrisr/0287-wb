from setuptools import setup

setup(name='wb',
        version='0.1.0',
        py_modules=['runner'],
        install_requires=[
            'Click',
            'wandb',
            ],
        entry_points={
            'console_scripts': [
                'runner=runner:log',
                'projects=runner:projects',
                ]
            },
        )
