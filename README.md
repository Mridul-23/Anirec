# ANIREC: Anime Recommender System
ANIREC is a hybrid anime recommender system utilizing a multi-armed bandit algorithm. This project aims to provide personalized anime recommendations by combining content-based filtering and collaborative filtering techniques.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

ANIREC is a sophisticated recommender system designed to provide accurate and relevant recommendations based on user preferences. This project combines multiple techniques, including content-based filtering and reinforcement learning, to deliver high-quality recommendations. 

The recommender system is implemented as a command-line interface and integrates Word2Vec embeddings for semantic similarity, along with a similarity matrix and a reinforcement learning algorithm for further optimization. 

## Features

- **Content-Based Filtering:** Utilizes Word2Vec embeddings to understand and compute similarities between items.
- **Similarity Matrix:** Employs cosine similarity to determine item relevance based on embeddings.
- **Hybrid Approach:** Combines content-based and collaborative filtering techniques.
- **Multi-Armed Bandit Algorithm:** Uses the Upper Confidence Bound (UCB) method to refine recommendations based on user interactions.
- **Command-Line Interface:** Operates through a CLI for ease of use and integration with other systems.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Mridul-23/Anirec.git
   cd Anirec
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Data:**

   Ensure that your dataset is in the required format. Place your data files in the appropriate directory or update the paths in the notebooks and script.

2. **Run the Notebooks:**

   Execute the following Jupyter notebooks in order to prepare and process the data, train the embeddings, and compute similarity:

   - **Data Preprocessing:** `Data_Preprocessing.ipynb`
   - **Word2Vec Training:** `w2v model.ipynb`
   - **Similarity Matrix Computation:** `similarity_matrix.ipynb`

   You can run these notebooks in a Jupyter environment.

3. **Run the Recommender System:**

   After preparing and processing the data, run the recommender system logic using:

   ```bash
   python model.py
   ```

   Follow the on-screen instructions to interact with the recommender system.

## Code Structure

- **`Data_Preprocessing.ipynb`:** Contains data preprocessing logic.
- **`w2v model.ipynb`:** Handles Word2Vec embeddings training.
- **`similarity_matrix.ipynb`:** Computes item similarity using a similarity matrix.
- **`model.py`:** Contains the Multi-Armed Bandit final recommender system logic and model.
- **`requirements.txt`:** Lists Python dependencies required to run the project.

## How It Works

1. **Data Preparation:** Data is preprocessed and converted into a format suitable for the recommender system.
2. **Embedding Generation:** Word2Vec embeddings are generated to capture semantic similarities between items.
3. **Similarity Computation:** A similarity matrix is created using cosine similarity.
4. **Recommendation Generation:** The Multi-Armed Bandit algorithm with UCB refines recommendations based on user interactions and item similarities.

## Contributing

Contributions to the ANIREC recommender system are welcome! Please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to:

- **Author:** Mridul Narula
- **GitHub:** [Mridul-23](https://github.com/Mridul-23)
