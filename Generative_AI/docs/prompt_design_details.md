# Prompt Design Documentation

## 1. Thought Process Behind Each Template

### Zero-Shot
The zero-shot template was designed as a baseline to evaluate the model’s natural ability to interpret structured clinical inputs without guidance. The goal was to produce simple and direct explanations.

### Few-Shot
The few-shot template was designed to enforce a consistent tone and structure using example cases. This was particularly useful for maintaining patient-friendly language and a predictable response format.

### Chain-of-Thought (CoT)
The CoT template was designed to explicitly guide the model’s reasoning process. By encouraging the model to consider each clinical feature, the template aims to improve completeness and reduce missing information.

### Generated Knowledge
The generated knowledge template was designed to simulate a knowledge-enhanced system by introducing additional medical context before generating the response.

---

## 2. How Domain Knowledge Influenced Design

The healthcare domain imposed several important constraints on prompt design:

- Avoid making medical diagnoses
- Use clear and simple language for non-expert users
- Base explanations only on the provided clinical features
- Avoid misleading or unsupported medical claims

These constraints influenced the templates as follows:
- Few-shot examples were written in a patient-friendly tone
- CoT was structured to reflect feature-by-feature medical reasoning
- Generated knowledge was controlled to avoid excessive or irrelevant information


---

## 3. Lessons Learned from Prompt Testing

### 1. Dependence on Examples in Few-Shot
Few-shot prompting showed strong performance in some cases but was not consistent across all test cases. This indicates that it depends heavily on similarity between test inputs and provided examples.

### 2. Importance of Structured Reasoning
The CoT template produced more consistent outputs because it forces the model to consider multiple clinical features explicitly. This reduces the chance of ignoring important inputs.

### 3. Trade-off Between Simplicity and Completeness
Zero-shot responses were simpler but often less detailed, while more structured templates provided richer explanations.

### 4. Need for Input Validation
Testing revealed that unrealistic or edge-case inputs were not handled explicitly. This suggests the need for a validation layer before passing data to the model.

---

## 4. Prompt Engineering Best Practices

Based on the experiment, the following best practices were identified:

- Use structured prompts (such as CoT) for tasks that require reasoning
- Avoid over-reliance on few-shot examples
- Ensure responses are grounded in the input features
- Maintain simple and clear language for end users
- Limit the introduction of external or unnecessary knowledge
- Validate inputs before generating responses

---

## 5. Conclusion

The Chain-of-Thought template was selected because it provides consistent, clear, and feature-aware explanations. It aligns well with the requirements of a healthcare system, where accuracy, clarity, and safety are essential.