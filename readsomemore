

🚀 Quick Start

1. התקנה
`bash
git clone https://github.com/nitzan-gimmi/nitzan-gimmi.github.io
cd nitzan-gimmi.github.io
pip install -r requirements.txt
`

2. שימוש בסיסי
`python
from tokenizer import HFBTTokenizer

tokenizer = HFBTTokenizer()
text = "שלום עולם"
tokens = tokenizer.encode(text)
print(tokens)
`

3. אימון מודל לדוגמה
`bash
python train.py --epochs 5 --tokenizer HFBT
`

---
מעולה 🌱  
בוא נבנה לך תיעוד מלא ומסודר שאפשר להכניס ישירות ל‑README.md. זה יהיה שילוב של טכני + פיוטי, עם חלוקה לרמות נאנו / מיקרו / מאקרו, כולל קוד, צינורות, והחזון הרחב.  

---

📖 HFBT – יומן מסע לשוני‑חישובי

🌱 פתיחה
הפרויקט HFBT נולד מתוך רצון לשלב בין שורשי השפה העברית לבין מודלים חישוביים מודרניים.  
הוא אינו רק קוד, אלא גם מסע פיוטי: מן האותיות אל האלגוריתם, מן הנשימה אל הווקטור.  

---

🔹 נאנו – אבני הבניין
יחידות הקוד והקבצים הבסיסיים המרכיבים את המערכת:

- קבצי תשתית
  - README.md – תיעוד הפרויקט.  
  - requirements.txt – ספריות נדרשות (כגון torch, transformers, numpy).  

- מודולים עיקריים
  - tokenizer.py – מימוש טוקנייזר HFBT.  
  - dataset.py – הכנת דאטה ללמידה.  
  - train.py – אימון מודל.  
  - evaluate.py – הערכת ביצועים.  

- דוגמת קוד בסיסית
  `python
  from tokenizer import HFBTTokenizer

  tokenizer = HFBTTokenizer()
  text = "שלום עולם"
  tokens = tokenizer.encode(text)
  print(tokens)
  `

---

🔹 מיקרו – הצינורות (Pipelines)
כאן מתחברים הבלוקים הקטנים לתהליכים שלמים:

1. Pipeline להכנת דאטה
`python
from dataset import prepare_dataset

train, test = prepare_dataset("corpus.txt")
`
שלבים: טעינת טקסטים → ניקוי → חלוקה לסט אימון/בדיקה.

---

2. Pipeline לאימון
`python
from train import train_model

train_model(train, tokenizer="HFBT", epochs=10)
`
שלבים: דאטה → טוקניזציה (HFBT) → אימון מודל → שמירת checkpoints.

---

3. Pipeline להערכה
`python
from evaluate import evaluate_model

results = evaluate_model("checkpoints/model.pt", test)
print(results)
`
שלבים: טעינת מודל → חישוב Precision / Recall / F1 → השוואה מול BPE.

---

🔹 מאקרו – החזון הרחב
כאן נפרשת התמונה הגדולה:

- GitHub Repository – מאגר ציבורי, פתוח לכולם.  
- תיעוד יומנאי – כל יום מתועד כפרק במסע (פיוטי + טכני).  
- תרשימי מושג – חיבור בין בנייני הפועל (פָּעַל, נִפְעַל, הִפְעִיל) לבין מושגים של Agency, Causality, Reflexivity.  
- Vector of Will – מושג מרכזי: הרצון כווקטור מתמטי, המחבר בין עבר לעתיד.  
- Roadmap  
  1. Tokenizer (HFBT)  
  2. Dataset  
  3. Training  
  4. Evaluation  
  5. Integration עם LLMs  

---

📊 דוגמת טבלת תוצאות
| Tokenizer | Precision | Recall | F1 Score | Tokens Efficiency |
|-----------|-----------|--------|----------|-------------------|
| BPE       | 0.82      | 0.79   | 0.80     | 1.0x              |
| HFBT      | 0.88      | 0.86   | 0.87     | 1.3x              |

---

✨ סיכום
HFBT הוא לא רק כלי טכני, אלא שפה חדשה:  
שפה שמחברת בין שורש ל‑וקטור, בין פיוט ל‑אלגוריתם, בין עבר ל‑עתיד.  

---

נִצן, זה שלד מוכן ל‑README.md שלך.  
רוצה שאבנה לך גם גרסת Quick Start קצרה (3 צעדים בלבד להתקנה והרצה) שתעמוד בראש המסמך, כדי שמפתחים חדשים יתחברו מהר?