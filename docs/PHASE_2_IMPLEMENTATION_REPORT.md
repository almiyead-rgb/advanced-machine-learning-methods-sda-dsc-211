# Phase 2 Implementation Report | تقرير تنفيذ المرحلة الثانية

## Status | الحالة

**Development branch:** `develop/bilingual-v1.1.0`  
**Target release:** `v1.1.0`  
**Published portal remains:** `v1.0.0`

No production page has been replaced on `main`. The bilingual redesign remains in Draft Pull Request 1 until portal, lab and accessibility gates pass.

لم تُستبدل الصفحة المنشورة على `main`. ما زالت إعادة التصميم الثنائية داخل Pull Request رقم 1 بصيغة Draft حتى اجتياز بوابات البوابة واللابات والوصول الرقمي.

## Delivered in this phase | ما تم تنفيذه

### Production README | README الفعلي

The repository landing page now uses a side-by-side bilingual structure with English on the left and Arabic on the right. It includes:

- Course value proposition and Tamweel Lite scenario.
- Duration, lab environment and free-tool requirements.
- Knowledge prerequisites and beginner readiness route.
- Five-day learning and project journey.
- Final repository deliverables.
- Assessment and final-verification instructions.
- Instructor attribution and release-state notice.

تستخدم صفحة المستودع الآن تصميمًا ثنائيًا بعمود إنجليزي يسارًا وعمود عربي يمينًا، وتشمل:

- قيمة الدورة وسيناريو Tamweel Lite.
- المدة وبيئة اللابات ومتطلبات الأدوات المجانية.
- المتطلبات المعرفية ومسار تهيئة المبتدئ.
- رحلة التعلم والمشروع خلال خمسة أيام.
- مخرجات المستودع النهائي.
- التقييم وتعليمات الفحص النهائي.
- حقوق المدربة وحالة الإصدار.

## Content corrections | تحسينات المحتوى

- Replaced ambiguous wording around “default loss” with **simulated decision cost / تكلفة القرار التعليمية**.
- Clarified that 20 hours are contact hours and may include scheduled prayer breaks inside the session window.
- Added prerequisites explicitly instead of implying that a specialist course requires no prior knowledge.
- Preserved the statement that the portal is an instructor learning portal and not an official SDAIA account.
- Preserved Arabic-only and English-only pages as focused-access alternatives while the future `index.html` will be bilingual.

## Pending portal work | الأعمال المتبقية للبوابة

1. Replace production `index.html` only after the bilingual prototype passes review.
2. Add portal-specific CI for HTML, CSS, JavaScript, anchors, links and bilingual parity.
3. Add automated accessibility checks and manual keyboard/screen-reader review.
4. Add canonical URLs, `hreflang`, Open Graph, sitemap, robots, 404 page and Course JSON-LD.
5. Verify mobile stacking, 200% zoom and reduced-motion behavior.
6. Align every portal link and term with the converted student-template release.

## Release rule | قاعدة الإصدار

The course hub and student template must be released together. The portal must never point learners to a partially converted or untested lab set.

يجب إصدار بوابة الدورة وقالب المتدرب معًا. لا يجوز أن توجه البوابة المتدربين إلى مجموعة لابات محولة جزئيًا أو غير مختبرة.
