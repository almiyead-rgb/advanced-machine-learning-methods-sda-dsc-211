# Phase 4 — Portal pre-release controls | المرحلة 4 — ضوابط البوابة قبل الإصدار

## Implemented | المنفذ

```text
release/portal_release_scope.json
scripts/build_portal_release_manifest.py
scripts/check_release_coordination.py
.github/workflows/portal_release_candidate.yml
RELEASE_NOTES.md
docs/HOSTED_BROWSER_QA.md
docs/PHASE_4_PRERELEASE_CONTROLS_IMPLEMENTATION_REPORT.md
```

## Controls | الضوابط

- Deterministic integrity inventory for the production portal files.
- Static coordination check for Notebook 00, Days 1–5, Notebook 99 and learner-support links.
- Assessment-signal checks for 90/10, pass 70 and distinction 95.
- Checks for instructor attribution and the bilingual non-official SDAIA statement.
- Hosted browser and accessibility acceptance protocol.
- Release notes aligned with the learner-template governance.

- جرد نزاهة حتمي لملفات البوابة الإنتاجية.
- فحص تنسيق ثابت لدفتر 00 والأيام 1–5 ودفتر 99 وروابط دعم المتدرب.
- فحص إشارات التقييم 90/10 والنجاح 70 والتميز 95.
- فحص نسبة العمل إلى المدربة وبيان عدم الرسمية الثنائي.
- بروتوكول اعتماد المتصفح والوصول.
- مواءمة ملاحظات الإصدار مع حوكمة قالب المتدرب.

## Limitations | الحدود

Automated checks do not replace hosted visual review, contrast testing, a screen-reader review or hosted-Colab acceptance. The final manifest must be regenerated after all release files are frozen.

لا تستبدل الفحوص الآلية المراجعة البصرية وفحص التباين وقارئ الشاشة واعتماد Colab. ويجب إعادة توليد Manifest النهائي بعد تجميد جميع ملفات الإصدار.
