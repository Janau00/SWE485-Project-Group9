### Test Case 1 — Heart Disease Detected

#### Input
| Feature | Value |
|---------|-------|
| Age | 55 |
| Sex | Male |
| ChestPainType | ATA |
| RestingBP | 140 |
| Cholesterol | 240 |
| FastingBS | 160 |
| RestingECG | Normal |
| MaxHR | 150 |
| ExerciseAngina | Yes |
| Oldpeak | 2.3 |
| STSlope | Flat |
| Prediction | Heart Disease |

#### Response
> Your assessment suggests the presence of heart disease, which is indicated by several key values. Your resting blood pressure of 140 mmHg and cholesterol level of 240 mg/dL are higher than recommended, indicating increased strain on your heart and arteries. Additionally, your fasting blood sugar of 160 mg/dL is elevated, which can impact your blood vessels over time. You also reported typical chest pain, especially during exercise, along with significant changes on your exercise ECG, specifically a 2.3 mm ST depression and a flat ST slope, which are strong indicators of reduced blood flow to your heart during physical activity. Taking steps to manage your blood pressure, cholesterol, and blood sugar, such as adopting a balanced diet and regular physical activity, can be beneficial. Given these results, it's important to consult with a medical professional to discuss these findings further and explore appropriate next steps for your heart health.

---

### Test Case 2 — No Heart Disease (All Healthy)

#### Input
| Feature | Value |
|---------|-------|
| Age | 35 |
| Sex | Female |
| ChestPainType | NAP |
| RestingBP | 110 |
| Cholesterol | 180 |
| FastingBS | 80 |
| RestingECG | Normal |
| MaxHR | 175 |
| ExerciseAngina | No |
| Oldpeak | 0.0 |
| STSlope | Up |
| Prediction | No Heart Disease |

#### Response
> Your assessment suggests no heart disease, which is a very positive indication for your cardiovascular health. Your blood pressure of 110 mmHg is well within a healthy range, meaning your heart and blood vessels are not under undue strain. Similarly, your cholesterol level of 180 mg/dL and fasting blood sugar of 80 mg/dL are both healthy, which helps prevent blockages in your arteries and supports overall well-being. Additionally, your resting ECG is normal, and during exercise, you showed no signs of angina or concerning changes like ST depression, indicating your heart functions well under stress. Continuing to maintain these healthy habits through a balanced diet and regular physical activity will further support your excellent heart health.

---

### Test Case 3 — No Heart Disease (Borderline Values)

#### Input
| Feature | Value |
|---------|-------|
| Age | 45 |
| Sex | Male |
| ChestPainType | NAP |
| RestingBP | 128 |
| Cholesterol | 210 |
| FastingBS | 100 |
| RestingECG | Normal |
| MaxHR | 160 |
| ExerciseAngina | No |
| Oldpeak | 0.8 |
| STSlope | Up |
| Prediction | No Heart Disease |

#### Response
> Based on your assessment, it suggests no heart disease was detected, which is generally reassuring. We observed that your resting ECG is normal, you don't experience chest pain indicating angina, and your blood sugar is within a healthy range, all of which are positive signs for your heart health. However, your resting blood pressure of 128 mmHg is considered elevated, meaning it's a bit higher than ideal, and your cholesterol at 210 mg/dL is slightly above the healthy target. While these values are not in the high-risk category, keeping your blood pressure and cholesterol levels in check through lifestyle choices like a balanced diet and regular physical activity can help support your long-term cardiovascular health. We recommend discussing these values with a healthcare professional to understand them better and determine if any steps are needed.

---

### Test Case 4 — Edge Case

#### Input
| Feature | Value |
|---------|-------|
| Age | 45 |
| Sex | Male |
| ChestPainType | ATA |
| RestingBP | 0 |
| Cholesterol | 210 |
| FastingBS | 100 |
| RestingECG | Normal |
| MaxHR | 150 |
| ExerciseAngina | No |
| Oldpeak | 0.8 |
| STSlope | Up |
| Prediction | No Heart Disease |

#### Response
> Your assessment suggests no heart disease detected, which is reassuring news. Looking at your results, your Resting ECG is normal and you did not experience any chest pain during exercise, which are positive indicators for your heart health. However, a couple of your values are on the borderline side. Your total cholesterol is 210 mg/dL, which is slightly above the ideal range and can be a factor in heart health over time. Your fasting blood sugar, at 100 mg/dL, is at the upper end of the healthy range, sometimes called pre-diabetes, and keeping it in check is important for long-term well-being. Additionally, while the overall assessment is reassuring, you reported a type of chest pain (ATA) that is sometimes associated with heart conditions, though it can also have other causes. Focusing on a balanced diet rich in fruits, vegetables, and whole grains, along with regular physical activity, can help manage both cholesterol and blood sugar levels effectively. Given these borderline values, it would be beneficial to discuss these results with your doctor to understand them further and explore any personalized recommendations they might have for you.

---