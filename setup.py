from setuptools import setup, find_packages

setup(
    name='pca_pwa',
    version='1.0.5',
    description='A package for PCA analysis with Flask application',
    author='Dany Mukesha',
    author_email='danymukesha@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'scikit-learn',
        'numpy',
        'matplotlib',
        'pandas',
        'seaborn',
        'adjustText',
        'scipy',
    ],
    entry_points={
        'console_scripts': [
            'pca_pwa_run=pca_pwa:main',
        ],
    },
)
