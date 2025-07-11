# AI Student Data Analysis

A Python-based machine learning project that analyzes student performance data using logistic regression to predict student outcomes.

## Overview

This project demonstrates the use of machine learning techniques to analyze student academic performance and behavior patterns. It uses a dataset containing student grades in multiple subjects, behavior assessments, and outcome indicators to build predictive models.

## Dataset

The project uses a student dataset (`student_data.csv`) with the following features:

- **students**: Student names
- **grades_math**: Mathematics grades (0-100)
- **grades_science**: Science grades (0-100)
- **grades_english**: English grades (0-100)
- **behavior**: Behavior assessment (good/bad)
- **passed**: Whether the student passed (1) or failed (0)
- **issues**: Whether the student has disciplinary issues (1) or not (0)

### Sample Data

The dataset includes 10 students with their respective academic and behavioral records.

## Technologies Used

- **Python 3.x**
- **NumPy**: For numerical computations
- **Pandas**: For data manipulation and analysis
- **Matplotlib**: For data visualization
- **Scikit-learn**: For machine learning algorithms
  - Logistic Regression
  - Train-test split
  - Label Encoder

## Project Structure

```
ai-v1/
├── main.py              # Main Python script
├── student_data.csv     # Student dataset
└── README.md           # Project documentation
```

## Features

- **Data Loading**: Automated dataset creation and CSV export
- **Data Processing**: DataFrame manipulation using Pandas
- **Machine Learning**: Logistic regression model setup
- **Data Preprocessing**: Label encoding for categorical variables
- **Model Training**: Train-test split functionality

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Muhmmedmedhat0/ai-v1.git
cd ai-v1
```

2. Install required dependencies:

```bash
pip install numpy pandas matplotlib scikit-learn
```

## Usage

Run the main script to execute the data analysis:

```bash
python main.py
```

The script will:

1. Load the student dataset
2. Create a pandas DataFrame
3. Export data to CSV format
4. Display the dataset information

## Requirements

```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
scikit-learn>=1.0.0
```

## Future Enhancements

- [ ] Implement complete logistic regression model training
- [ ] Add data visualization charts
- [ ] Perform feature analysis and correlation studies
- [ ] Add model evaluation metrics (accuracy, precision, recall)
- [ ] Implement cross-validation
- [ ] Add predictive functionality for new student data

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Muhmmedmedhat0**

## Contact

For questions or suggestions, please open an issue in the GitHub repository.
