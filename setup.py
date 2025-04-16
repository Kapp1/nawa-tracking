from setuptools import setup, find_packages

setup(
    name="nawa-tracking",
    version="0.1.0",
    description="NAWA – Smart Pilgrim Tracking & AI Toolkit",
    author="Khalid Al-...",
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=[
    "fpdf2==2.7.7"
],
    python_requires=">=3.8",
    url="https://github.com/Kapp1/nawa-smart-hajj",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
