# Generative AI Prompt Engineering Documentation

This document presents the prompt engineering design process used in the Generative AI phase of the project. It covers the rationale behind each prompting technique, the influence of domain knowledge on template design, lessons learned during prompt evaluation and testing, and references to prompt engineering best practices and healthcare AI literature.

The document focuses on the conceptual and design-related aspects of the system. For additional implementation details, experiments, execution workflow, and testing outputs, refer to `Phase2_Generative_AI.ipynb`.



### Shared Prompt Design Principles

 **System and User Prompt Separation**

The prompt structure adopted across all four templates in this project is divided into two distinct parts: a System Instruction and a User Prompt. This design follows the Google Gemini API documentation, which provides a dedicated `system_instruction` parameter that separates the model's persistent behavioural rules from the variable user message (Google, 2024). The system instruction defines the model's role, tone, language level, and constraints, which are rules that must remain fixed for that template regardless of which patient is being assessed. The user prompt then carries the patient-specific data and the task-related description for each patient assessment.

This separation is not merely a technical convention. It reflects a fundamental principle in prompt engineering: that governance rules and task-specific content should never be mixed in the same layer, as doing so risks inconsistency, ambiguity, and unpredictable model behaviour (Tetrate, 2025). When behavioural rules are embedded within the user prompt, they become prone to being overridden, forgotten, or misinterpreted. By contrast, placing them in a dedicated system instruction ensures they are treated with higher priority by the model and remain stable across all requests.

This principle is especially critical in a medical context. In healthcare AI applications, consistency is not a preference but a safety requirement. A system that gives different analysis to similar patients, or that drops its safety constraints when the user prompt is complex, poses a direct risk to patient trust and clinical validity. As noted by Gharib et al. (2024), effective prompt design in healthcare requires that the model's behavioural boundaries are clearly established and reliably maintained across all interactions. Similarly, research on prompt engineering in clinical practice emphasises that small changes in prompt structure can significantly impact output quality and safety in medical settings (Cascella et al., 2024). By anchoring all safety rules, role definitions, and tone constraints within the system instruction, each template in this project ensures that no matter what patient data is passed through the user prompt, the model will always respond within the same controlled and medically appropriate framework.

> Google. (2024). *Gemini API documentation: System instructions.*
> Google AI for Developers.
> https://ai.google.dev/gemini-api/docs/system-instructions

> Tetrate. (2025). *System prompts vs user prompts: Design patterns
> for LLM apps.*
> https://tetrate.io/learn/ai/system-prompts-vs-user-prompts

> Gharib, A.M., et al. (2024). *A guide to prompt design: Foundations
> and applications for healthcare simulationists.* Frontiers in Medicine,
> 11, 1504532.
> https://doi.org/10.3389/fmed.2024.1504532

> Cascella, M., Montomoli, J., Bellini, V. and Bignami, E. (2024).
> *Prompt Engineering in Healthcare.* Electronics, 13(15), 2961.
> https://doi.org/10.3390/electronics13152961


**Role Definition**

The system instruction begins by assigning the model a specific
professional role aligned with the intended user of each template.
Each template defines its own role that reflects the user profile
it is designed to serve.
Establishing a clear role is a recognised best practice in prompt
engineering, as it guides the model's
vocabulary and depth of explanation (Google, 2024). By framing the model within a
health-related role, the generated responses become more consistent,
clinically relevant, and appropriate for the intended audience.
This is particularly important in a cardiovascular interpretation
system where the assigned role directly shapes how the model
interprets and explains clinical values, ensuring the output is
appropriate for the intended user profile of each template.


> Google. (2024). *Introduction to prompting.*
> Google AI for Developers.
> https://ai.google.dev/gemini-api/docs/prompting-intro

**Safety Constraints (What the Model Must Never Do)**

Safety constraints are a set of explicit negative rules that define what the model must never do, regardless of the prompting technique or patient data provided. In a cardiovascular health interpretation system, the absence of explicit safety constraints creates real clinical and ethical risk. Guidelines for human-AI interaction recommend that AI systems deployed in sensitive contexts must avoid overconfidence, remain transparent about their limitations, and use language appropriate to the user's emotional state (Amershi et al., 2019). Without an explicit prohibition, a model may produce diagnostic-sounding language because such language is statistically common in the medical text the model was trained on. The constraint must therefore be stated directly in every template, because the model will not infer it from context alone. That said, while safety constraints appear in every template, their specific form differs depending on the intended use case.

> Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P., Inkpen, K., Teevan, J., Kikin-Gil, R., and Horvitz, E. (2019). *Guidelines for human-AI interaction.* Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, 1–13.
> https://doi.org/10.1145/3290605.3300233

**Style Prompting (Tone and Language Control)**

Another component present across all templates is the explicit instruction to control tone and language style. This is formally classified as Style Prompting, a technique that modifies how the model expresses its output rather than what it reasons about or how it structures its response (Sahoo et al., 2024). Style prompting does not change the content, it shapes the way that content is delivered, including the level of formality, the emotional register, and the vocabulary choices the model makes.

In a cardiovascular health interpretation system, tone control has a direct impact on how the patient receives and acts on the information. Research in human-computer interaction confirms that in health-related contexts, warm and conversational language builds significantly more trust than clinical or detached language, and that patients are more likely to engage with recommendations delivered in a tone that feels supportive rather than authoritative (Bickmore and Picard, 2005). Without explicit style instructions, a model with access to medical training data will default to clinical register precise, impersonal, and often alarming to a non-expert reader because that is the dominant tone in the text it learned from.

However, the specific style instructions differ from one template to another based on the intended use case and user profile. The appropriate tone for one user type would be mismatched and potentially counterproductive for another, which is why style prompting must be calibrated individually for each template rather than applied uniformly across the system.

> Sahoo, P., Singh, A.K., Saha, S., Jain, V., Mondal, S. and Chadha, A. (2024). *A systematic survey of prompt engineering in large language models: Techniques and applications.*
> https://arxiv.org/pdf/2406.06608

> Bickmore, T. and Picard, R. (2005). *Establishing and maintaining long-term human-computer relationships.* ACM Transactions on Computer-Human Interaction, 12(2), 293–327.
> https://dl.acm.org/doi/10.1145/1067860.1067867

# Generated Knowledge Prompting

---
### Approach Definition
Generated Knowledge Prompting is a prompt engineering technique introduced
by Liu et al. (2022) that instructs the model to first generate relevant
knowledge about the topic before producing its final response. Rather than
asking the model to answer directly, the prompt is structured in two
internal stages within a single request: the model first surfaces and
organises what it knows about the subject, and then uses that
self-generated knowledge as the foundation for its final output.

The core idea behind this technique is that large language models contain
vast amounts of knowledge from their training, but do not always surface
the most relevant information when asked to respond directly. By explicitly
instructing the model to generate knowledge first, the prompt forces a
broader and more deliberate retrieval of relevant information before any
conclusion is produced. This generated knowledge then sits within the
model's context during the response generation phase, ensuring that the final
response is grounded in a richer and more organised understanding of the
topic (Liu et al., 2022). This approach does not require access to an
external knowledge base or any task-specific training, making it flexible
and practical for a wide range of applications.

> Liu, J., Liu, A., Lu, X., Welleck, S., West, P., Le Bras, R., Choi, Y.,
> and Hajishirzi, H. (2022). *Generated Knowledge Prompting for Commonsense
> Reasoning.* Proceedings of the 60th Annual Meeting of the Association for
> Computational Linguistics, 3154–3169.
> https://doi.org/10.18653/v1/2022.acl-long.225


---

### Relation to Medical Field
In a medical context, generating knowledge before producing a response is
particularly valuable because clinical reasoning is rarely a direct
input-to-output process. A clinician examining a patient's cardiovascular
data does not immediately jump to a conclusion. They first consider what
each measurement means, how it relates to known clinical patterns, and what
risks it might indicate, before framing an interpretation. Generated Knowledge Prompting mirrors this interpretive process
by instructing the model to first surface and organise its clinical
knowledge about the patient's specific feature values before producing
the final interpretation.

This is especially important in cardiovascular health, where the clinical
significance of a measurement depends heavily on context. A resting blood
pressure of 145 mmHg, for example, cannot be interpreted in isolation. The
model needs to draw on its knowledge of what that value means, how it
relates to cardiovascular risk, and how it interacts with other features
in the patient's profile before it can generate interpretation that is genuinely
meaningful. By explicitly instructing the model to generate this contextual
knowledge first, the prompt ensures that the final interpretation is grounded in
a deliberate clinical reasoning step rather than a surface level response.

---
### Intended Use Case
 **1- Deployment Environment**

The system is planned to be deployed as an interpretation tool within a hospital
mobile application. Patients access it from their personal smartphones
after obtaining their clinical data, either from a recent cardiovascular
test or by completing one at the hospital. The patient enters their
clinical values into the tool and receives a personalized interpretation
directly on the same screen.

 **2- The User**

The primary user of this template is a first-time patient who is
encountering the system and their clinical results for the very first
time. This patient arrives with no frame of reference for what their
numbers mean. A resting blood pressure of 145 mmHg is just a number to
them. An Oldpeak value of 2.3 carries no weight without context. A
cholesterol category label means nothing without knowing what it implies
for their health. Providing interpretation to this patient without first
establishing what their values mean would produce a response they cannot
connect to their own situation, and interpretation that cannot be connected to
is an interpretation that will not be acted on.

***Medical background:*** No medical background is assumed. The gap
between what the patient's values say and what they mean to that patient
is the primary consideration of this template. Before any interpretation
can land meaningfully, the patient needs enough foundational understanding
to connect the interpretation back to their own situation rather than
receiving it as information they must simply trust.

***Emotional state:*** First-time users often arrive uncertain and quietly
apprehensive. They may not know what they are looking for or what a
concerning result would even look like. The tone of the interpretation must
therefore be steady and educational rather than clinical or alarming.
The goal is not to reassure unconditionally or to alarm unnecessarily,
but to leave the patient feeling genuinely informed and oriented enough
to take the next right step.

**3- Inputs**

3.1- The patient heart disease classification result

3.2- The patient clinical feature values


**4- Output**

A single interpretation paragraph written in plain, accessible language.
Although the model generates clinical knowledge internally as part of
its knowledge generation process, none of this internal knowledge generation is
visible to the patient. The output reads as a clean, direct interpretation,
but because it was built on top of a deliberate knowledge generation
step, it is more grounded in the patient's specific values and more
educationally coherent than a direct response would be for someone
encountering their clinical data for the first time.

---

### Design Rationale
**Advantage 1 — Grounded knowledge generation before response:**
Generated Knowledge Prompting instructs the model to first surface and
organise relevant knowledge about the input before producing its final
response, ensuring the output is grounded in an explicit knowledge generation step
rather than a direct leap from input to answer (Liu et al., 2022). In a
heart disease interpretation system, this matters because the clinical
significance of a patient's feature values cannot be determined without
first interpreting what those values mean in a cardiovascular context.
A model that jumps directly to interpretation without first generating
knowledge about the patient's specific measurements risks producing
a generic or misaligned interpretation that does not reflect the
patient's actual clinical profile.

**Advantage 2 — Improved contextual relevance for individual patients:**
By generating knowledge that is specific to the input provided, the
technique ensures that the final response is tailored to the individual
patient rather than relying on broad generalisations (Liu et al., 2022).
In a heart disease interpretation system where two patients can share the same
prediction label but have entirely different clinical profiles, this
matters directly. A patient with a borderline resting blood pressure and
a flat ST slope requires fundamentally different explanation and interpretation from a patient
with a normal blood pressure and an asymptomatic chest pain type, even
if both are classified as No Heart Disease Detected. Generated Knowledge Prompting ensures the model generates contextual
knowledge about the specific values present before writing the interpretation,
producing a response that reflects the individual rather than the label.

**Advantage 3 — No dependency on predefined examples:**
Generated Knowledge Prompting does not require carefully crafted
input-output examples to guide the model's behaviour. The model draws
on its own clinical knowledge to reason about the patient's data, making
the technique flexible and robust across the full range of possible
patient profiles (Liu et al., 2022). In a heart disease interpretation system
where patient feature values vary continuously across a wide range,
providing representative examples that cover all meaningful combinations
is not practical. Generated Knowledge Prompting eliminates this
dependency by allowing the model to generate the contextual knowledge
it needs dynamically from the input itself.


> Liu, J., Liu, A., Lu, X., Welleck, S., West, P., Le Bras, R., Choi, Y.,
> and Hajishirzi, H. (2022). *Generated Knowledge Prompting for Commonsense
> Reasoning.* Proceedings of the 60th Annual Meeting of the Association for
> Computational Linguistics, 3154–3169.
> https://doi.org/10.18653/v1/2022.acl-long.225


# Chain-of-Thought Prompting


---

### Approach Definition

Chain-of-thought (CoT) prompting is a prompt engineering technique in which a language model is instructed to produce a series of intermediate reasoning steps before arriving at a final answer. Rather than mapping an input directly to an output in a single pass, the model externalizes its thinking process, each step builds on the previous one, and the final answer is explicitly grounded in the visible reasoning chain. IBM describes CoT as a technique that simulates human-like reasoning by breaking down elaborate problems into manageable, intermediate steps that sequentially lead to a conclusive answer (IBM, 2024). The technique is activated by including a structured reasoning directive in the prompt, most commonly the phrase "think step by step," which signals to the model that intermediate steps are required as part of the response rather than just a final conclusion.


> IBM. (2024). *What is chain of thought (CoT) prompting?* IBM Think.
> __https://www.ibm.com/think/topics/chain-of-thoughts__

---

### Relation to Medical Field


The structure of chain-of-thought prompting mirrors the way clinicians think when making a diagnosis. A doctor assessing a patient for cardiovascular disease does not jump straight from test results to a treatment decision. Patel and Groen (1986) studied how cardiologists reason through complex cases and found that accurate diagnoses were reached by moving in one direction only: from clinical findings, step by step, toward a conclusion. Each step followed from the one before it, building on the available evidence rather than starting from an assumed answer. This is exactly how chain-of-thought prompting works: the model moves forward through a series of reasoning steps, each grounded in the previous one, without going back to revise earlier conclusions, making CoT a naturally suitable technique for clinical decision-making tasks.

> Patel, V. L., & Groen, G. J. (1986). Knowledge based solution strategies in medical reasoning. *Cognitive Science*, *10*(1), 91–116.
> https://doi.org/10.1207/s15516709cog1001_4

---

### Intended Use Case


**1- Deployment Environment**

The system is planned to be deployed as an interpretation tool within a hospital
mobile application. Patients access it from their personal smartphones
after obtaining their clinical data, either from a recent cardiovascular
test or by completing one at the hospital. The patient enters their
clinical values into the tool and receives a personalized interpretation
directly on the same screen.

**2- The User**

The primary user of this template is a health-literate patient who approaches their health result with curiosity and a desire to understand rather than simply act. This patient is likely to be someone who has prior experience with cardiovascular health (either through a personal history of monitoring their health closely, a family member with heart disease, or a general habit of researching their medical information). They are comfortable reading a longer, structured response and will invest the time to follow a step-by-step explanation from beginning to conclusion.


***Medical background:*** While no formal medical background is assumed, this patient is health-literate. They are capable of understanding concepts such as blood pressure ranges, cholesterol categories, and the general relationship between lifestyle factors and cardiovascular risk. The interpretation may therefore use slightly more specific language compared to the other templates, as long as each term is explained in context.

***Emotional state:*** This patient is engaged rather than acutely anxious. They are seeking information and understanding, which means a longer, more structured response will not increase their distress. However, the tone must still remain calm and professional. The visibility of the reasoning steps must never make the output feel like a clinical verdict.

**3- Inputs**

3.1 The patient heart disease classification result

3.2 The patient clinical feature values


**4- Output**

A structured response consisting of:
- A brief per-feature assessment
- A brief synthesised final interpretation paragraph
- An actionable recommendation

The reasoning steps walk through the patient's most significant clinical
values one by one, identifying what each means and how it contributs
to the overall picture. The paragraph then synthesises these steps into
a coherent interpretation. The visible reasoning is written in plain
language throughout so that the patient can follow each step without a
medical background. Although the reasoning follows the order of the
per-value table, the output format presents the interpretation paragraph
first, followed by the per-value breakdown, so that the patient receives
the overall picture before being exposed to the granular detail of each
individual value. Scrolling is acceptable here because the patient
prefers this level of detail.


---

### Design Rationale

**Advantage 1 — Improved accuracy on complex reasoning tasks:**
Chain-of-thought improves model performance on complex tasks by breaking
them down into smaller, manageable steps, with each intermediate step
acting as a checkpoint where errors can be caught before they carry
forward into the final output (DataCamp, 2024). In a heart disease
interpretation system, this matters because an error made early (such as
misreading a borderline cholesterol value or misclassifying a resting
ECG result) will corrupt every reasoning step that follows it. By
making each step visible and sequential, chain-of-thought allows such
errors to be identified at the point they occur rather than arriving
silently embedded in a final recommendation.

**Advantage 2 — Transparency and explainability:** By generating visible
intermediate reasoning steps, chain-of-thought makes the decision-making
process auditable and easier to follow for non-expert users (IBM, 2024).
In a heart disease interpretation system where the intended users have no
medical background, this is a functional requirement. A patient who
receives only a label or a conclusion cannot understand what it
means for them personally, identify which of their values drove the
outcome, or communicate the basis of the interpretation to a doctor. By
walking through each feature in plain, step-by-step reasoning before
reaching a conclusion, chain-of-thought produces an output that a
non-specialist can follow, question, and act on, rather than simply
accept or dismiss.

**Advantage 3 — Multistep reasoning capability:** Chain-of-thought
handles tasks that require multistep reasoning by systematically working
through each component of a problem before reaching a conclusion, leading
to more reliable outputs (IBM, 2024). In cardiovascular test,
reliability is critical where a premature conclusion or a skipped step can
result in an interpretation that does not reflect the patient's actual
condition. By structuring the output as a sequence of dependent reasoning
steps, chain-of-thought encourages the model to consider all components before reaching a conclusion making the
final output consistent and reproducible regardless of how the input
values are distributed.

**Advantage 4 — Attention to detail:** The step-by-step nature of
chain-of-thought encourages detailed breakdowns of complex inputs,
ensuring each component is examined and accounted for before a conclusion
is reached (IBM, 2024). In cardiovascular test, where no
single factor is decisive on its own, this level of detail is essential.
The ACC/AHA Pooled Cohort Equations calculate cardiovascular risk from
multiple variables whose combined effect is non-additive, meaning the
contribution of any one feature depends on the values of the others
(Goff et al., 2014). Chain-of-thought ensures that no feature is skipped
or treated as insignificant, making it the most detail-preserving
technique available for this task.


> DataCamp. (2024). *Chain-of-thought prompting*.
> https://www.datacamp.com/tutorial/chain-of-thought-prompting

> IBM. (2024). *Chain of thoughts*. IBM Think.
> https://www.ibm.com/think/topics/chain-of-thoughts

> Goff, D. C., Lloyd-Jones, D. M., Bennett, G., Coady, S., D'Agostino, R. B.,  Gibbons, R., Greenland, P., Lackland, D. T., Levy, D., O'Donnell, C. J.,  Robinson, J. G., Schwartz, J. S., Shero, S. T., Smith, S. C., Sorlie, P., Stone, N. J., & Wilson, P. W. F. (2014). 2013 ACC/AHA guideline on the assessment of cardiovascular risk: A report of the American College of Cardiology/American Heart Association Task Force on Practice Guidelines. *Journal of the American College of Cardiology*, *63*(25), 2935–2959.
> https://doi.org/10.1016/j.jacc.2013.11.005

# Few-Shot Prompting

---

### Approach Definition

Few-shot prompting is a prompt engineering technique in which a language model is provided with a small number of labeled examples before being asked to perform a new but similar task. Instead of relying only on a direct instruction, the model learns the expected pattern of input-output behavior from the examples included in the prompt. These examples act as demonstrations that guide the model toward producing outputs in the required format and according to the intended logic (Brown et al., 2020).

> Brown, T. et al. (2020). *Language Models are Few-Shot Learners*. NeurIPS.
> https://arxiv.org/abs/2005.14165

---

### Relation to the Medical Field

Few-shot prompting is particularly well suited to the medical domain because when a clinician assesses a new cardiovascular patient, they do not interpret the case from scratch. Instead, they draw on previously encountered patients with similar profiles, comparing the current case against familiar patterns before reaching a conclusion. A cardiologist who has seen many patients with high blood pressure, elevated cholesterol, and chest pain will immediately recognize that combination as a risk pattern worth taking seriously, not because of a single number, but because of how the full picture matches cases seen before(Elstein, 2002).

This is exactly how few-shot prompting works(Brown et al., 2020). By placing a small number of labeled patient records inside the prompt, the model is shown how similar cardiovascular profiles have been interpreted in the past. Each example acts as a reference point, guiding the model to recognize patterns across multiple variables rather than reacting to any single measurement in isolation. In that sense, few-shot prompting functions as a lightweight case-based reasoning mechanism, one that mirrors the comparative, pattern-driven logic that underlies real clinical judgment in cardiovascular care.

> Brown, T. et al. (2020). *Language Models are Few-Shot Learners*. NeurIPS.
> https://arxiv.org/abs/2005.14165

> Elstein, A. S. (2002). *Clinical problem solving and diagnostic decision making*.
> https://pmc.ncbi.nlm.nih.gov/articles/PMC1122649/

---

### Intended Use Case

**1- Deployment Environment**

The system is designed to be deployed as a heart disease interpretation tool within a healthcare mobile application. Patients can access it through their smartphones after obtaining their clinical data, either from a hospital test or by manually entering their values into the system. The health overview is generated instantly and displayed on the same screen.



**2- The User**

The primary user of this template is a returning patient who has used the healthcare application before and has already received at least one prior health overview through the system. This user is familiar with the general style, tone, and structure of the generated response, and they return expecting a consistent and recognisable experience.
Unlike a first-time user, this patient does not need the system to introduce the format from the beginning. Instead, they benefit from receiving their health overview in a stable and predictable structure that allows them to compare their current result with previous overviews, notice changes in their condition, and follow their health status over time.

***Medical background:***

No medical expertise is assumed. However, because the user has prior experience with the system, the response does not need to introduce or justify its structure, and can instead focus directly on the interpretation content. The output should avoid complex terminology and focus on simple explanations supported by examples.

***Emotional state:***

The patient may still feel some concern when reviewing a health-related result, but they are likely to approach the output with greater familiarity than a new user. For that reason, the response should remain supportive and clear while focusing on reassurance through consistency and readability.



**3- Inputs**

3.1 The patient heart disease classification result

3.2 The patient clinical feature values




**4- Output**

A structured but concise response that follows the pattern demonstrated in the examples. The output includes:
- A short interpretation of the patient’s condition
- A brief explanation based on the most relevant features
- A clear, simple tips and suggestions

The response should remain consistent with the format shown in the examples, ensuring readability and ease of understanding.


---

### Design Rationale

**Advantage 1 —  Better adaptation to the task:**
Few-shot prompting helps the model adapt to the specific prediction task by showing it exactly how inputs and outputs should look. This is important in the heart disease dataset because the model needs to deal with structured patient attributes such as age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, and other clinical indicators. A few examples help the model understand how these features are mapped to the target class.(OpenAI, 2023)

**Advantage 2 — Improved consistency of outputs:**
When examples are included in the prompt, the model is more likely
to respond in a consistent format. In the context of this template,
consistency is particularly valuable for returning patients who may
receive multiple assessments over time. A consistent output structure
allows the patient to compare their current results with previous
ones more easily, track changes in their clinical values, and notice
patterns in their cardiovascular health without being confused by
a different presentation each time.

**Advantage 3 — Useful when labeled examples are meaningful:**
Our dataset already contains labeled cases, which makes few-shot prompting a natural choice. Since the target variable indicates the presence or absence of heart disease, example records can be selected directly from the dataset to guide the model. This allows the prompting technique to align closely with the supervised learning setting, where the model benefits from seeing representative examples before handling unseen cases.



> OpenAI. (2023). *Prompt Engineering Guide*.
> https://platform.openai.com/docs/guides/prompt-engineering

# Zero-Shot Prompting
---

### Approach Definitio
Zero-shot prompting is a prompt engineering technique in which a language model is asked to perform a task using only a direct instruction, without being given any examples of the expected input-output pattern beforehand. Instead of learning from demonstrations included in the prompt, the model relies entirely on its pretrained language understanding and the clarity of the instruction to generate an appropriate response (Kojima et al. 2022).

> Kojima, T. et al. (2022). *Large Language Models are Zero-Shot Reasoners*.
> https://arxiv.org/abs/2205.11916

---

### Relation to the Medical Field

Zero-shot prompting is relevant to the medical field because many healthcare applications need to generate useful responses from clinical information in a straightforward way. In medical settings, the ability to give clear output from a direct instruction is valuable, especially when the task requires the model to respond in a controlled format. This makes zero-shot prompting suitable for health-related systems that depend on consistency, clarity, and simple communication with users. In our project, zero-shot prompting fits the heart disease interpretation context because the system needs to produce a short and understandable message based on the patient’s result and clinical values without relying on example cases inside the prompt. This allows the prompt to remain simple while still guiding the model to generate an appropriate response (Sivarajkumar et al., 2023).

> Sivarajkumar, S. et al. (2023). *HealthPrompt: A Zero-shot Learning Paradigm for Clinical Natural Language Processing*.
> https://pmc.ncbi.nlm.nih.gov/articles/PMC10148337/

---

### Intended Use Case

**1- Deployment Environment**

The system is designed to be deployed as a heart disease interpretation tool within a healthcare mobile application. Patients can access it through their smartphones after obtaining their clinical data, either from a hospital test or by manually entering their values into the system. The health overview is generated instantly and displayed on the same screen.


**2- The User**

The primary user of this template is a patient who is likely to feel anxious when receiving health-related information and prefers communication that gives immediate reassurance. They are not looking for a deep or highly detailed explanation. Instead, they want to quickly understand the situation in simple language and feel that they are being guided clearly and gently. This user is likely to focus first on the overall meaning of the result rather than the technical details behind it. They may also read the message quickly, especially if they are worried, so information that is too dense or too long can make understanding harder.

***Medical background:***

No medical expertise is assumed. Health-related terms, measurements, and clinical concepts are understood only at a general everyday level, not at a professional or technical level.

***Emotional state:***

The patient may be worried and needs reassurance early. They are more likely to respond well to language that feels calm, supportive, and steady, and less well to wording that sounds harsh, alarming, or overly certain.


**3- Inputs**

3.1 The patient heart disease classification result

3.2 The patient clinical feature values


**4- Output**

A short personalised health overview written in clear, plain, and supportive language. It briefly presents the patient’s result, highlights only the most relevant concerning or borderline values in an accessible way, and keeps the message calm, focused, and easy to understand. The overview does not list all feature values, does not explain the reasoning process, and remains brief enough to read comfortably on a mobile screen without scrolling.

---

### Design Rationale



**Advantage 1 — Simple prompt design:**
Zero-shot prompting does not require additional example data inside the prompt, which makes it useful when supporting examples are limited, unnecessary, or difficult to prepare. In our case, the model will only need a clear instruction to generate the personalised health overview, so the template remains lightweight and practical. This reduces preparation effort and makes the approach easier to apply consistently across many patient cases (IBM, 2025).

**Advantage 2 — Speed and efficiency:**
Since zero-shot prompting does not require the model to process example cases before generating a response, it can produce outputs more quickly and with less prompt overhead (Shah, 2024).

**Advantage 3 — Flexiblity:**
Zero-shot prompts are easy to adapt when the wording, tone, or output requirements need to change. Since the template is not tied to fixed demonstrations, updating it requires little effort compared with prompts that depend on carefully chosen examples. This makes zero-shot prompting a flexible option for our system (IBM, 2025).

> IBM. (2025). *What is zero-shot prompting?*.
> https://www.ibm.com/think/topics/zero-shot-prompting

> Shah, D. (2024). Zero-Shot vs. Few-Shot Prompting: Choosing the Right Approach for Your AI Model.
> https://portkey.ai/blog/zero-shot-vs-few-shot-prompting/

## Final Prompt Selection
### Selected Template: Template 2 — Chain of Thought

After evaluating all four templates across both qualitative and
quantitative dimensions, Template 2 — Chain of Thought was selected
as the final template for deployment. The justification below walks
through the qualitative evidence first, then the quantitative
evidence, before explaining why the chain-of-thought structure is
uniquely positioned to serve the system's goals.
### Qualitative Justification

The key reason for selecting Template 2 — Chain of Thought is that it consistently satisfied all
qualitative requirements across the evaluation.
Most importantly, Template 2 was the only template that correctly
identified and handled the edge case (RestingBP = 0 mmHg). It explicitly
flagged the value as clinically invalid and advised re-measurement,
while all other templates ignored the anomaly and produced confident
responses. This behaviour is critical in a safety-sensitive healthcare
context.

### Quantitative Justification

The quantitative results provide further evidence for why Template
2 is the strongest choice for this system. Template 2 achieved
the highest medical accuracy rate at 80%, which is the most
clinically significant metric in this context. In a system where
an inaccurate clinical statement could directly contradict guidance
a patient receives from their doctor, accuracy is not a quality
preference but a safety requirement regardless of the user type
whether a nervous patient, a first-time patient, or a returning
health-literate patient.

Template 2 also achieved the highest domain keyword density at
8.36%, demonstrating that its responses are clinically grounded
and substantive enough to provide genuine value to a health-literate
or returning patient who expects their specific clinical values to
be named and discussed, while still remaining accessible enough
for a first-time or nervous patient to follow through the
interpretation paragraph.

On readability, a score of 42.66 reflects responses that are
linguistically calibrated for a health-literate patient who expects
clinical depth. Importantly, this score applies to the per-value
table which is the more detailed layer of the output. The
interpretation paragraph, which is the first thing any patient
sees regardless of their profile, is written in plain and
accessible language, making the overall output suitable for all
user types. A nervous patient can stop at the paragraph, a
first-time patient can use it as a foundation, and a returning
or health-literate patient can continue into the table for the
full clinical breakdown.

On passive voice, a rate of 14.57% demonstrates that Template 2
consistently addresses the patient in a direct and personal tone
across all scenarios, producing responses that feel patient-facing
rather than clinical report-like. This directness is equally
valuable for a nervous patient who needs reassurance, a first-time
patient who needs clarity, and a returning patient who expects
a familiar and engaging tone. Together these quantitative results
confirm that Template 2 is not only qualitatively superior but
also quantitatively well-calibrated to serve the full spectrum
of patient profiles in the intended deployment context.
### Why the Chain-of-Thought Structure Fits the System

Beyond the evaluation results, the chain-of-thought structure
offers a structural advantage that no other template can match.
The output is naturally divided into two parts: an interpretation
paragraph that provides the patient with an immediate and coherent
overview of their result, followed by a per-value table that breaks
down each clinical feature individually. This structure serves the
system in two important ways.

The interpretation paragraph appears first, giving the patient an
immediate and accessible summary of what their result means before
they engage with the detail. This ensures that even a patient who
does not explore the full table still receives a meaningful overview
of their cardiovascular assessment.


The per-value table provides a clear breakdown of each clinical
feature that patients can explore if they want more detail. Although
this structure may appear longer than other templates, this is a
deliberate trade-off that prioritizes flexibility over
brevity.
The table can also be exported as a PDF, allowing patients to save
their results, share them with their doctor, or review them later
to track changes over time. This extends the system beyond a
one-time explanation into a more persistent and useful reference.
In practice, this design adapts to different user needs. Patients
who prefer a quick understanding can rely on the initial
interpretation paragraph, while others can engage with the detailed
table or exported PDF for a more comprehensive view of their
cardiovascular profile.

Template 2 is therefore selected as the final template for the
system.


## Limitations


In addition to the limitations identified during the evaluation of
Template 2, deploying the selected approach introduces several
system-level limitations that must be taken into consideration
before deployment. These limitations are not specific to the
chain-of-thought technique itself but rather reflect broader
constraints of the system that remain relevant regardless of which
template is selected.

**1. Dependency on the XGBoost Prediction Label**
The generated insight is anchored to the XGBoost prediction label
as its primary input. This means that if the underlying model
produces an incorrect prediction, the chain-of-thought reasoning
will be built around a misleading result, and the detailed per-value
analysis will be framed incorrectly regardless of how thorough the
reasoning steps are.


**2. Non-Deterministic Output**
The template relies on a large language model whose outputs are
non-deterministic. Two identical patient inputs may produce slightly
different reasoning steps and insights across runs, which could
affect consistency and reliability in a clinical deployment context.

**3. No External Clinical Verification**
The chain-of-thought reasoning relies entirely on the model's
internal knowledge. There is no external verification mechanism to
confirm that the clinical statements produced in each reasoning
step are factually correct, which means inaccurate statements may
appear without being detected.

**4. Single Language Support**
The template is designed and evaluated in English only, which limits
its applicability in multilingual hospital settings.

**5. Binary Outcome Classification**
The XGBoost prediction model produces a binary outcome, either
Heart Disease Detected or No Heart Disease Detected. However,
heart disease is not a binary condition but rather a spectrum of
conditions with multiple types, severities, and clinical
presentations. By reducing this complexity to a binary label,
the model oversimplifies the clinical reality of cardiovascular
disease. This means that the generated insight, which is anchored
to this binary label, cannot capture the nuance of different
heart disease types or severity levels, potentially leading to
an oversimplified interpretation of the patient's cardiovascular
health that does not reflect the full clinical picture.


## Ethical Considerations



Deploying an AI-driven cardiovascular insight system in a hospital
setting raises several ethical considerations that must be carefully
addressed to ensure the system operates responsibly and in the best
interest of the patient.

**1. Risk of Misinterpretation**
The system is designed to frame all findings as probabilistic
assessments rather than confirmed diagnoses. However there is a
risk that patients may still read the generated insight as a
definitive medical conclusion. This is particularly concerning
because the system is deployed for patients who may be encountering
their clinical data for the very first time and may not have the
medical literacy to distinguish between what the assessment
suggests and what a licensed clinician would confirm. Unlike a
face-to-face clinical consultation where a doctor can rely on
voice, tone, body language, and real-time feedback to ensure the
patient has understood the information correctly, a text-based
AI system has none of these communication channels available.
This gap in understanding could lead to unnecessary anxiety if
the result suggests a risk, or to false reassurance if the result
appears favourable.

**2. Patient Autonomy and Informed Consent**
The system generates personalised health insights based on the
patient's clinical data using an artificial intelligence model.
For patient autonomy to be preserved, patients must be made aware
before interacting with the system that the insight they receive
is AI-generated and does not constitute professional medical
advice. This informed consent is essential because a patient who
is unaware of the AI-driven nature of the system may treat the
generated insight with the same level of trust they would place
in a licensed clinician, which could directly influence the
decisions they make about their own health and care.


**3. Data Privacy**
The system processes sensitive patient clinical data including
blood pressure, cholesterol, fasting blood sugar, and ECG
findings. Appropriate data protection measures must be in place
to ensure that patient data is handled securely and in compliance
with relevant healthcare data privacy regulations.

**4. Over-Reliance on AI**
There is a risk that patients may treat the generated insight as
a final conclusion and fail to take the necessary next step of
consulting a medical professional. A patient who receives a
reassuring insight may feel that visiting a doctor is no longer
needed, while a patient who receives a concerning insight may
delay seeking care while waiting for further AI-generated
clarification. In both cases the system's output becomes a
substitute for professional medical consultation rather than a
prompt to seek it, which represents a direct risk to patient
safety in a clinical deployment context.

**5. Dataset Representativeness and Geographical Bias**
The XGBoost prediction model was trained on the Heart Failure
Prediction Dataset, which combines five datasets sourced from
Cleveland, Hungary, Switzerland, Long Beach VA, and the Stalog
Heart Dataset. None of these datasets originate from Saudi Arabia
or the broader Middle Eastern population. Since cardiovascular
risk profiles, lifestyle factors, and clinical presentations can
vary significantly across different populations and ethnicities,
deploying a model trained exclusively on Western datasets in a
Saudi Arabian hospital setting raises concerns about the
generalisability and fairness of the predictions. The generated
insights produced by Template 2 are anchored to these predictions,
meaning that any population-level bias in the underlying model
will directly propagate into the patient-facing output

**6. Underrepresentation of Female Patients**
The dataset used to train the XGBoost prediction model is
significantly imbalanced in terms of gender. The dataset contains
724 male observations compared to 193 female observations, with
63.1% of male patients having heart disease compared to only 25.9%
of female patients. This imbalance means the model has been trained
predominantly on male cardiovascular patterns, which may result in
less accurate predictions for female patients. Since the generated
insights produced by Template 2 are directly anchored to the
model's prediction, female patients may receive insights that do
not fully reflect their individual cardiovascular risk profile,
raising concerns about gender fairness and equitable care in the
deployed system.