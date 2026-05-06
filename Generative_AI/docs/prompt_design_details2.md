# Prompt Design Documentation

## 1. Thought Process Behind Each Template

### Zero-Shot
The zero-shot template was designed as a baseline to evaluate the model’s natural ability to interpret structured clinical inputs without guidance. The goal was to produce simple and direct explanations.

### Few-Shot
The few-shot template was designed to enforce a consistent tone and structure using example cases. This was particularly useful for maintaining patient-friendly language and a predictable response format.

### Chain-of-Thought (CoT)
The CoT template was designed to explicitly guide the model’s reasoning process. By encouraging the model to consider each clinical feature, the template aims to improve completeness and reduce missing information.

### Generated Knowledge
The generated knowledge template was designed to simulate a knowledge-enhanced system by retrieving additional medical context before generating the response.

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
- Generated knowledge was guided to surface cardiovascular clinical
  knowledge relevant to the patient's specific values.


---

## 3. Lessons Learned from Prompt Testing

### 1. Dependence on Examples in Few-Shot
Few-shot prompting showed strong performance in some cases but was not consistent across all test cases. This indicates that it depends heavily on similarity between test inputs and provided examples.

### 2. Importance of Structured Reasoning
The CoT template produced more consistent outputs because it forces the model to consider multiple clinical features explicitly. This reduces the chance of ignoring important inputs.

### 3. Trade-off Between Simplicity and Completeness
Zero-shot responses were simpler but often less detailed, while more structured templates provided richer explanations.


---

## 4. Prompt Engineering Best Practices Applied
**System and User Prompt Separation**
All behavioural rules, constraints, tone instructions, and structural requirements are placed in the system prompt. The user prompt carries only the patient data and a single task trigger sentence. This separation follows the Google Gemini API documentation, which provides a dedicated system_instruction parameter that separates the model's persistent behavioural rules from the variable user message. 

> Google. (2024). *Gemini API documentation: System instructions.* Google AI for Developers.
> https://ai.google.dev/gemini-api/docs/system-instructions

> Tetrate. (2025). *System prompts vs user prompts: Design patterns for LLM apps.*
> https://tetrate.io/learn/ai/system-prompts-vs-user-prompts

> Gharib, A.M., et al. (2024). *A guide to prompt design: Foundations and applications for healthcare simulationists.* Frontiers in Medicine, 11, 1504532.
> https://doi.org/10.3389/fmed.2024.1504532

> Cascella, M., Montomoli, J., Bellini, V. and Bignami, E. (2024). *Prompt Engineering in Healthcare.* Electronics, 13(15), 2961.
> https://doi.org/10.3390/electronics13152961

---

**Role Assignment**
Each template opens by assigning the model a specific professional role calibrated to the intended user. In a cardiovascular interpretation system, the assigned role directly shapes how the model interprets and explains clinical values, ensuring the output is appropriate for the intended user profile of each template.

> Google. (2024). *Introduction to prompting.* Google AI for Developers.
> https://ai.google.dev/gemini-api/docs/prompting-intro

---

**Task Identification**
Some templates includes a clear, explicit statement of the model's task. Without a precise task definition, the model may interpret the same input differently across runs, particularly in a medical context where the boundary between explanation, advice, and diagnosis is clinically significant.

> Liao, Q.V., Subramonyam, H., Wang, J. and Wortman Vaughan, J. (2023). *Designerly understanding: Information needs for model transparency to support design ideation for AI-powered user experience.* Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems.
> https://doi.org/10.1145/3560815

---

**Safety Constraints**
All four templates include explicit negative rules defining what the model must never do, regardless of the prompting technique or patient data provided. These include prohibitions against stating a diagnosis, referencing the classification model directly, and using language that implies clinical certainty. Without these explicit constraints, a model trained on medical text will produce diagnostic-sounding language by default because such language is statistically dominant in its training data.

> Amershi, S., et al. (2019). *Guidelines for human-AI interaction.* Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, 1–13.
> https://doi.org/10.1145/3290605.3300233

---

**Style Prompting and Tone Control**
Each template includes explicit tone instructions calibrated to the intended user. Tone is never left to the model's default, as a model trained on medical text will default to a clinical register that is inappropriate for non-expert patients. Research in human-computer interaction confirms that warm and conversational language builds significantly more trust in health-related contexts.

> Sahoo, P., Singh, A.K., Saha, S., Jain, V., Mondal, S. and Chadha, A. (2024). *A systematic survey of prompt engineering in large language models: Techniques and applications.*
> https://arxiv.org/pdf/2406.06608

> Bickmore, T. and Picard, R. (2005). *Establishing and maintaining long-term human-computer relationships.* ACM Transactions on Computer-Human Interaction, 12(2), 293–327.
> https://dl.acm.org/doi/10.1145/1067860.1067867

---

**Output Length Constraint**
The interpretation paragraph is constrained to a specific sentence count in some templates. This constraint is expressed in sentences rather than word count because sentence count is a more reliable length control mechanism since large language models frequently fail to follow exact word count instructions precisely. The constraint ensures the primary output remains immediately readable on a mobile screen without scrolling, regardless of which template is used.

> Google. (2024). *Introduction to prompting.* Google AI for Developers.
> https://ai.google.dev/gemini-api/docs/prompting-intro

