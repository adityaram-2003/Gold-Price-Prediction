# Gold Price Prediction Project

This project aims to predict gold prices using machine learning techniques and provide a user-friendly interface to interact with the prediction model through a web application built with Flask. The machine learning model implemented in this project is a Random Forest Classifier.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Gold prices are influenced by various factors such as economic conditions, geopolitical events, and investor sentiment. Predicting gold prices accurately can be challenging due to the complexity of these factors. Machine learning models provide a promising approach to forecast gold prices based on historical data and relevant features.

This project leverages a Random Forest Classifier, a popular ensemble learning algorithm, to predict gold prices. The model is trained on historical gold price data and relevant features extracted from various sources. The trained model is then integrated into a Flask web application, allowing users to upload datasets and obtain gold price predictions.

## Features

- Prediction of gold prices using a Random Forest Classifier
- Data pre-processing techniques such as feature splitting and correlation analysis
- Integration with Flask to create a user-friendly web interface
- Visualization of predicted vs. actual gold prices
- Simple and intuitive user experience

## Getting Started

To get started with the Gold Price Prediction project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies.
3. Run the Flask application.
4. Upload a dataset containing gold price data.
5. Obtain predictions for gold prices.

## Installation

To install the required dependencies, follow these steps:

```bash
pip install -r requirements.txt
```

## Usage

After installing the dependencies, you can run the Flask application by executing the following command:

```bash
python app.py
```

Once the Flask application is running, you can access it through a web browser. Upload a dataset containing gold price data using the provided interface. After uploading the dataset, click on the "Evaluate Model" button to obtain predictions for gold prices.

## Contributing

Contributions to the Gold Price Prediction project are welcome. You can contribute by:

- Reporting bugs and issues
- Suggesting new features or enhancements
- Submitting pull requests with bug fixes or improvements

Please follow the established code style and guidelines when contributing to this project.

## License

This project is licensed under the [MIT License](LICENSE).

---
