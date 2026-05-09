# Heart Disease Prediction System (SWE485 Project)

## Motivation
Heart disease remains one of the leading causes of death worldwide, making early detection and prevention essential for improving patient outcomes. Many cardiovascular conditions develop silently over time, and patients may not recognize symptoms until serious complications occur.

Motivated by the growing potential of Artificial Intelligence in healthcare, this project aims to explore intelligent approaches for heart disease analysis and patient understanding. Using clinical and demographic data such as age, blood pressure, cholesterol levels, and exercise-related measurements, supervised learning techniques were used to predict the likelihood of heart disease, while clustering methods were applied to identify hidden patient patterns and groups. In addition, Generative AI was later integrated to transform technical prediction outputs into clear, patient-friendly explanations, helping make healthcare insights more understandable.

---

## Phase 1: Supervised Learning
In Phase 1, we developed a classification system using supervised machine learning techniques.

### Key Contributions:
- Data exploration and preprocessing
- Feature analysis and visualization
- Implementation of multiple supervised models (Random Forest, XGBoost, Extra Trees)
- Model evaluation using standard metrics (accuracy, precision, recall, etc.)
- Selection of the best-performing model for prediction

---

## Phase 2: System Enhancement

### Unsupervised Learning
Clustering techniques were applied to uncover hidden patterns in patient data.

- Investigated data clusterability using VAT, Hopkins statistic, and pairwise distribution analysis
- Applied two clustering algorithms (K-Means and HDBSCAN)
- Evaluated cluster quality using standard clustering metrics
- Interpreted clusters to better understand patient group characteristics and behavioral patterns

---

###  Generative AI Integration
Generative AI was integrated to provide clear, patient-friendly explanations of prediction results.

#### Prompt Engineering:
Four prompt templates were designed and evaluated:
- Zero-Shot Prompting
- Few-Shot Prompting
- Chain-of-Thought (CoT)
- Generated Knowledge

#### Key Outcomes:
- Each template was tested using multiple patient cases
- Outputs were evaluated based on clarity, relevance, and consistency
- Chain-of-Thought (CoT) was selected as the best-performing template due to its structured reasoning and consistent explanations

---

## Team Members
- Deema Alageefi - 444200543
- Jana Alshreef - 444200933
- Lana Alshehri - 444201143
- Layan Alhugbani - 444201214
- Loba Alyahya - 444201187
- Reem Alharbi - 444200949

