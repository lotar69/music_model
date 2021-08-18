from setuptools import setup, find_packages

setup(
    author="Julie & Loic",
    description="Find the music style",
    name="music_model",
    version="0.1.0",
    packages=find_packages(include=["music_model", "music_model.*"]),
    package_data={"": ["*.csv"]},
    include_package_data=True,
    instal_requires=[
        "pandas",
        "scikit-learn",
        "numpy",
        "streamlit",
        "matplotlib",
        "setuptools",
    ]
)