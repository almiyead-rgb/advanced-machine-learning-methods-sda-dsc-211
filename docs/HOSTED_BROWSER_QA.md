# Hosted browser and accessibility QA | اختبار المتصفح والوصول

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## Required environments | البيئات المطلوبة

| Environment | Widths | Required checks |
|---|---|---|
| Chrome on Windows | 1366, 1024, 390 px | layout, links, keyboard, zoom |
| Edge on Windows | 1366, 1024, 390 px | layout, links, keyboard, zoom |
| Screen reader | Desktop width | headings, landmarks, link names |
| Print preview | A4 portrait | readable ordering and no clipped text |

## Acceptance checks | فحوص القبول

- English is visually on the left and Arabic on the right at desktop widths.
- At narrow widths, the two languages stack without mandatory horizontal scrolling.
- Every navigation link reaches the intended section.
- All Colab and support links open the correct learner-template resource.
- Focus is visible for every interactive element.
- The skip link appears on keyboard focus and moves to main content.
- Text remains readable at 200% zoom.
- Information is not conveyed by colour alone.
- Reduced-motion preferences remove non-essential transitions.
- The non-official SDAIA statement and instructor attribution are visible.

- تظهر الإنجليزية يسارًا والعربية يمينًا في العرض المكتبي.
- تتكدس اللغتان في العرض الضيق دون تمرير أفقي إلزامي.
- تصل روابط التنقل إلى أقسامها الصحيحة.
- تفتح روابط Colab والدعم الموارد الصحيحة في قالب المتدرب.
- يظهر مؤشر التركيز لكل عنصر تفاعلي.
- يظهر رابط التجاوز عند استخدام لوحة المفاتيح وينتقل إلى المحتوى الرئيس.
- يبقى النص مقروءًا عند تكبير 200%.
- لا تعتمد المعلومة على اللون وحده.
- تلغي إعدادات تقليل الحركة الانتقالات غير الضرورية.
- يظهر بيان عدم الرسمية واسم المدربة بوضوح.

## Evidence record | سجل الأدلة

Create a dated result file only after the hosted review. Record browser versions, widths, screenshots, defects, corrective commits and final status: `PASS`, `PASS WITH LIMITATIONS`, or `FAIL`.

لا تُسجّل حالة نجاح قبل تنفيذ المراجعة الفعلية في المتصفح.
