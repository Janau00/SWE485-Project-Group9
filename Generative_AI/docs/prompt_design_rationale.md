# Prompt Design Rationale

This document explains the rationale behind the four prompt templates: Zero-Shot, Few-Shot, Chain-of-Thought (CoT), and Generated Knowledge, based on experimental results.

## Zero-Shot Prompting
The zero-shot template was designed as a baseline to evaluate the model’s ability to generate explanations without guidance.

From testing, zero-shot responses were generally simple and easy to read. However, they often lacked depth and did not consistently reflect all relevant clinical features. This made the explanations less informative compared to other templates.

## Few-Shot Prompting
The few-shot template used example input-output pairs to guide structure and tone.

Quantitatively, few-shot achieved high accuracy in some cases (TC1 and TC2 = 100%). However, results showed instability:
- One test case dropped to 0% accuracy
- Performance depended heavily on similarity to examples

This indicates that few-shot relies on pattern matching rather than robust reasoning.

## Chain-of-Thought (CoT) Prompting
The CoT template was designed to guide the model through step-by-step reasoning based on each clinical feature.

Results showed:
- Consistent performance across all test cases
- Better coverage of features (no missing values in explanation)
- Strong alignment with domain keywords (avg ~8.36%)
- Stable readability scores (avg ~42.66)

Unlike few-shot, CoT does not depend on similarity to examples, making it more reliable.

## Generated Knowledge Prompting
This template attempted to enrich responses by introducing additional medical knowledge.

While this approach improved clinical grounding, the medical accuracy score of 70.84% reveals that internally generated knowledge does not guarantee factual correctness. Even when the model actively retrieves clinical information before responding, a portion of that information can still be inaccurate or misaligned with the patient's actual values.

## Final Decision
Chain-of-Thought was selected because it provided:
- Stable performance across all test cases
- Better reasoning transparency
- Strong alignment with clinical features

This makes it the most suitable template for real-world use.



---------------------------OR-------------------------------------
# Prompt Design Rationale

This document explains the rationale behind the four prompt templates: Zero-Shot, Few-Shot, Chain-of-Thought (CoT), and Generated Knowledge, based on the experimental results presented in the notebook.

## Zero-Shot Prompting
The zero-shot template was designed as a baseline to evaluate the model’s ability to generate explanations without guidance or examples.

From testing, zero-shot responses were generally simple and easy to read. However, they often lacked depth and did not consistently reflect all relevant clinical features. This made the explanations less informative compared to other templates.

## Few-Shot Prompting
The few-shot template used example input-output pairs to guide the model’s tone, structure, and reasoning.

The results showed that few-shot can achieve high performance when the test input is similar to the provided examples. However, the evaluation revealed instability across test cases, where performance varied depending on how closely the new input matched the examples. This indicates that the model relies heavily on pattern matching rather than consistent reasoning.

## Chain-of-Thought (CoT)
The Chain-of-Thought template was designed to guide the model through a structured reasoning process by explicitly considering each clinical feature.

The results demonstrated that CoT provides more consistent outputs across different test cases. It ensures that multiple clinical features are considered in the explanation and reduces the likelihood of missing important information. This leads to clearer and more reliable responses compared to zero-shot and few-shot.

## Generated Knowledge
The generated knowledge template aimed to enrich responses by incorporating additional medical context before generating the explanation.

While this approach sometimes improved the completeness of the response, it also introduced the risk of including information that is not directly related to the patient’s input. This occasionally reduced the clarity and focus of the explanation.

## Final Decision
Based on the overall comparison, the Chain-of-Thought template was selected as the best-performing approach. It provides a balance between clarity, consistency, and feature-level reasoning, making it the most suitable for generating patient-friendly explanations in a healthcare context.