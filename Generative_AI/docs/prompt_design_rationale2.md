# Prompt Design Rationale

This document explains the rationale behind the four prompt templates designed for the heart disease interpretation system: Generated Knowledge, Chain-of-Thought, Few-Shot, and Zero-Shot. Each template follows the same structured documentation approach used in the notebook: Define, Justify, Design Explanation, Build, Test, Evaluate, and Reflect. The rationale here summarises the key decisions made at each stage.

---

## Generated Knowledge Prompting

**What it is and why it suits the medical field**
Generated Knowledge Prompting instructs the model to first surface relevant clinical knowledge about the patient's specific values before writing the final interpretation. In a cardiovascular context, this means the model builds a knowledge base from the patient's individual measurements before producing interpretation, grounding the response in context rather than jumping directly from the prediction label to a conclusion.

**Intended user and rationale**
This template serves a first-time patient who has never seen or interpreted their cardiovascular values before and has no frame of reference for what their measurements mean. The knowledge-generation step was chosen because a first-time patient cannot connect interpretations to their situation without first understanding what their values represent. 

**What testing revealed**
Generated Knowledge produced clinically grounded and personalized responses across all test cases and maintained non-zero accuracy across all scenarios (unlike few-shot and zero-shot which each recorded a 0% accuracy in one case). However, the medical accuracy score of 70.84% revealed that internally generated knowledge does not guarantee factual correctness. The model occasionally surfaced plausible but misaligned clinical content.

---

## Chain-of-Thought Prompting

**What it is and why it suits the medical field**
Chain-of-Thought Prompting requires the model to examine each clinical value individually before synthesising a final interpretation. This makes the entire reasoning process visible to the patient. In a cardiovascular context, this structure forces the model to confront each value on its own terms before forming a conclusion, which prevents implausible values from being silently absorbed into a generic response.

**Intended user and rationale**
This template serves a health-literate, detail-oriented patient who wants to understand the reasoning behind their result rather than simply receive a conclusion. The chain-of-thought structure was chosen because visible reasoning directly serves this user's preference. The technique also produces a clinical safety benefit that was confirmed during testing.

**What testing revealed**
Chain-of-Thought was the only template to flag the implausible RestingBP value of 0 mmHg as clinically impossible, both in the per-value table and in the interpretation. This was not the result of an explicit rule in the prompt, it was a structural consequence of the per-value reasoning format. It achieved the highest medical accuracy at 80%, a readability score of 42.66 appropriate for its health-literate user. Its primary trade-off is output length, which can be addressed by delivering the per-value tables as a downloadable PDF while keeping the interpretation paragraph concise on the mobile screen.

---

## Few-Shot Prompting

**What it is and why it suits the medical field**
Few-Shot Prompting embeds carefully selected example input-output pairs in the prompt to anchor the model's output to a stable format, tone, and level of clinical detail. In a cardiovascular context, this approach ensures that the model's responses follow a recognizable pattern, which is particularly valuable for returning patients who expect consistency across visits.

**Intended user and rationale**
This template serves a returning patient who has used the system before and expects a consistent and familiar response structure. The few-shot approach was chosen because format anchoring through examples directly meets this user's expectation, they are not seeking a new experience but a reliable continuation of a familiar one.

**What testing revealed**
Few-shot showed the most variable performance of all four templates. It achieved acceptable accuracy when the patient's profile closely resembled a provided example, but recorded a 0% accuracy in one test case (a complete disconnection from the patient's actual clinical values). It also produced the lowest readability score at 20.66, which is a concern even for a returning patient who knows the system's format but is not a medical expert. The pattern-matching mechanism that enables consistency also limits the template's ability to reason independently when the live input diverges from the examples.

---

## Zero-Shot Prompting

**What it is and why it suits the medical field**
Zero-Shot Prompting provides the model with only a direct instruction and the patient's data. The model relies entirely on its pretrained knowledge and the clarity of the prompt to generate an appropriate response. In a cardiovascular context, this approach produces a concise and immediately accessible output, which suits patients who need a brief, warm message rather than a detailed analysis.

**Intended user and rationale**
This template serves an anxious patient who needs immediate reassurance and clear, accessible guidance delivered as quickly and calmly as possible. Zero-shot was chosen because the absence of scaffolding keeps the output short and emotionally focused which is exactly what an anxious patient needs. Adding reasoning steps, examples, or knowledge-generation to this template would produce an output that is too long and too clinical for a user in an emotionally vulnerable state.

**What testing revealed**
Zero-shot produced the highest readability score at 54.55 and the lowest passive voice rate at 8.34%, both consistent with its design goal of producing direct, patient-addressed language. However, it showed inconsistency in its safety constraint where several responses drifted toward diagnostic phrasing, and recorded a 0% accuracy in one test case, reflecting the risk of a direct response approach when no reasoning structure is in place.

---

## Final Decision

Chain-of-Thought was selected as the best template for the final system. The primary reason is clinical safety: it was the only template to identify and flag an impossible input value, which is a fundamental requirement for a system deployed in a hospital context where patient-entered data cannot be guaranteed to be valid. Beyond safety, it achieved the highest medical accuracy at 80%, the strongest personalization through its two-layer structure, and an appropriate readability. Its longer output is addressed by design where the per-value tables can be delivered as a downloadable PDF while the interpretation paragraph remains the primary visible output on the mobile screen.