This repository contains datasets used in the paper: 
**"Generating Comprehensive and Balanced User Review Summaries with Large Language Models"** by Loris Belcastro, Cristian Cosentino, and Fabrizio Marozzo from the DIMES Department, University of Calabria.

# Overview

The paper introduces a novel methodology that leverages Large Language Models (LLMs) such as BERT and GPT to create comprehensive and balanced summaries of user-generated reviews. Unlike conventional summarization methods, which often highlight positive aspects to encourage purchases, this approach aims to present an unbiased perspective by covering both positive and negative aspects of the reviews.


# Datasets

The repository includes the following datasets:

##    Amazon Product Reviews:
    Content: Reviews of 50 selected products, primarily in the electronics category. Each product has hundreds of reviews, totaling approximately 10,000 entries.
    Features: Review text, rating, title, review reactions, user verification status, location, and date of the review.
    Distribution: Balanced across all possible ratings (1 to 5 stars).
##    Tripadvisor Hotel Reviews:
    Content: Reviews of 150 hotels in New York.
    Features: Review title, user rating, language, travel date, type of trip.
    Trip Types: Couples, solo, family, business, friends, and not specified.


# How to Cite

If you use the datasets or the methodology described in this paper, please cite it as follows:

```bibtex
@InProceedings{ecml-pkdd-marozzo-2025,
  author    = {Loris Belcastro and Cristian Cosentino and Pietro Lio and Fabrizio Marozzo},
  title     = {Balanced and Token-Efficient Summarization of User Reviews via Stratified Sampling and Large Language Models},
  booktitle = {Proceedings of the European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML PKDD)},
  year      = {2025}
}

# Contact

For questions or feedback, please reach out to lbelcastro@dimes.unical.it, ccosentino@dimes.unical.it, or fmarozzo@dimes.unical.it.
