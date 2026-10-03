# Bilingual Learning Design Standard | معيار التصميم التعليمي الثنائي

Version: 1.1.0-draft  
Owner: Meaad Al-Marri | ميعاد المري

## Purpose | الغرض

This standard governs every learner-facing page, guide, notebook, report template, and assessment artifact in SDA-DSC-211. The objective is not literal translation. The objective is equivalent learning value in both languages.

يحكم هذا المعيار كل صفحة ودليل ودفتر وقالب تقرير وأداة تقييم تظهر للمتدرب في SDA-DSC-211. الهدف ليس الترجمة الحرفية، بل تقديم قيمة تعليمية متكافئة باللغتين.

## Desktop layout | تخطيط الحاسب

| English — left column | العربية — العمود الأيمن |
|---|---|
| Independent LTR explanation | شرح عربي مستقل باتجاه RTL |
| Official technical terminology | المقابل العربي المهني للمصطلح |
| Same objective, evidence, and limitations | الهدف والدليل والقيود نفسها |
| Shared executable code appears once | يظهر الكود التنفيذي المشترك مرة واحدة |

## Mobile layout | تخطيط الجوال

At widths below 760 px, paired columns must stack vertically. Arabic appears first on the Arabic-first portal and English appears first on the English-first portal. The content must remain understandable without horizontal scrolling.

عند عرض أقل من 760 بكسل تتحول الأعمدة إلى تسلسل رأسي. تظهر العربية أولًا في الواجهة العربية، وتظهر الإنجليزية أولًا في الواجهة الإنجليزية. يجب أن يبقى المحتوى مفهومًا دون تمرير أفقي.

## Content equivalence rules | قواعد تكافؤ المحتوى

1. Every learner-facing heading must have an Arabic and English equivalent.
2. Objectives, instructions, warnings, deliverables, and acceptance criteria must match semantically.
3. Neither language may contain a requirement absent from the other.
4. Code, file names, variable names, commands, library names, and metric symbols remain in English.
5. Numbers, thresholds, durations, and formulas must be identical in both languages.
6. Translation must preserve the strength of claims and uncertainty qualifiers.
7. Recovery outputs, illustrative results, and non-submittable examples must carry the same warning in both languages.
8. Arabic typography must include spaces around Latin terms and numbers, for example: `اليوم 1`, `دفتر 99`, `على CPU`, `تجارب Optuna`.

## Notebook structure | بنية دفاتر Colab

Each instructional section follows this order:

1. Paired concept cell: English left, Arabic right.
2. One shared code cell.
3. Bilingual output heading.
4. Paired interpretation prompts.
5. A checkpoint with evidence and completion criteria.

كل قسم تعليمي يتبع الترتيب نفسه:

1. خلية مفهوم ثنائية: الإنجليزية يسارًا والعربية يمينًا.
2. خلية كود مشتركة واحدة.
3. عنوان ثنائي للمخرجات.
4. أسئلة تفسير باللغتين.
5. نقطة تحقق توضح الدليل ومعيار الاكتمال.

### Required notebook metadata | بيانات وصفية إلزامية للدفتر

Every paired Markdown cell created for v1.1.0 should include:

```json
{
  "bilingual_pair_id": "day01-section03",
  "bilingual_order": "en-left-ar-right",
  "learner_facing": true
}
```

## Terminology governance | حوكمة المصطلحات

The canonical terminology source is `content/terminology.yml`. Authors must not invent alternative Arabic translations inside individual files. A proposed change to a term must update the terminology file first, then all dependent content.

المصدر المرجعي للمصطلحات هو `content/terminology.yml`. لا يجوز إنشاء ترجمات عربية بديلة داخل الملفات منفردة. يبدأ أي تعديل للمصطلح من ملف المصطلحات ثم ينعكس على جميع المواد المرتبطة.

## Accessibility | الوصول الرقمي

- Use semantic headings in order.
- Include visible keyboard focus.
- Do not communicate meaning by colour alone.
- Support 200% zoom.
- Respect `prefers-reduced-motion`.
- Provide meaningful link text in both languages.
- Use explicit `dir="ltr"` and `dir="rtl"` at the content-block level.
- Avoid merged table cells that confuse screen readers.

## Visual hierarchy | التسلسل البصري

Each learner-facing block should answer four questions in order:

1. What are we building? | ماذا سنبني؟
2. Why does it matter? | لماذا يهم؟
3. What evidence will be produced? | ما الدليل الناتج؟
4. How do I know I am done? | كيف أعرف أنني أنجزت المطلوب؟

## Quality gate | بوابة الجودة

A file is not bilingual-complete unless all of the following are true:

- Both languages are present.
- Directions are correct.
- Requirements and numbers match.
- Links resolve.
- Terminology matches the canonical glossary.
- The page is readable on desktop and mobile.
- The learner can identify the deliverable and completion test without instructor explanation.
