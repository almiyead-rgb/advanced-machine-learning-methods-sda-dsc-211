# Phase 7 — Unified Student Gateway | المرحلة 7 — بوابة المتدرب الموحدة

## Decision | القرار

The public course portal is now the single student-facing gateway for `SDA-DSC-211`. Learners no longer need to discover course resources by browsing multiple repository folders. The portal links readiness, all five labs, project templates, requirements, assessment, final verification, submission guidance and learner support from one bilingual page.

أصبحت بوابة الدورة العامة نقطة الدخول الموحدة للمتدرب في `SDA-DSC-211`. لم يعد المتدرب بحاجة إلى البحث داخل مجلدات متعددة؛ إذ تجمع الصفحة الثنائية الاستعداد واللابات الخمسة وقوالب المشروع والمتطلبات والتقييم والفحص النهائي وإرشادات التسليم والدعم.

## Single public entry | نقطة الدخول العامة

```text
https://almiyead-rgb.github.io/advanced-machine-learning-methods-sda-dsc-211/
```

Legacy routes remain valid and redirect to the unified page:

```text
/ar.html → /
/en.html → /
```

## Student-facing resources | الموارد المتاحة للمتدرب

### Start and readiness | البداية والاستعداد

- Start guide
- Create-from-template link
- Notebook 00 in Colab
- Readiness guide

### Five-day journey | رحلة الأيام الخمسة

Each day exposes both the Colab notebook and the corresponding learner guide:

- Day 1 — baseline and boosting
- Day 2 — honest validation and leakage control
- Day 3 — imbalance, threshold and simulated decision cost
- Day 4 — interpretation, calibration and stability
- Day 5 — ensembles, Model Card and delivery

### Project workspace | مساحة المشروع

- Student repository template
- Data guide
- Decision Card template
- Interpretability report template
- Model Card template
- Final presentation template and guide
- Course-alignment matrix

### Requirements and assessment | المتطلبات والتقييم

- Technical requirements
- Administrative requirements
- Full rubric: 90 project points + 10 presentation points
- Pass and distinction thresholds
- Integrity-gate notice

### Final submission | التسليم النهائي

- Notebook 99
- Final-check guide
- Submission guide
- Final Project Check workflow
- Exact tag and commit-SHA instructions
- Private cohort submission route

### Support library | مكتبة الدعم

- Colab guide
- GitHub guide
- Troubleshooting
- FAQ
- Optional videos and references
- Bilingual glossary

## Privacy boundary | حد الخصوصية

The portal exposes all materials a student needs, but it does not expose instructor-only controls. The following remain private:

- hidden evaluation features and labels,
- private evaluator implementation and reports,
- student identities and grades,
- submission-registry records and receipts,
- access credentials and tokens.

تعرض البوابة كل ما يحتاجه المتدرب، لكنها لا تكشف بيانات التقييم المخفية أو تقارير المقيم أو هويات المتدربين ودرجاتهم أو سجلات الإيصالات أو بيانات الدخول.

## Accessibility and responsive behaviour | الوصول والاستجابة

- English appears on the left and Arabic on the right on desktop.
- Narrow screens stack content vertically.
- Keyboard skip link and visible focus remain available.
- Reduced-motion and print rules remain active.
- The old Arabic-only and English-only URLs redirect to the same unified experience.

## Automated evidence | الأدلة الآلية

At candidate commit `60007f0916ace30262b41c61964a3cf2f7547732`:

| Gate | Run | Result |
|---|---:|---|
| Portal Quality Check | `37109616284` | PASS |
| Portal Release Candidate | `37109616264` | PASS |
| Coordinated v1.1.0 Candidate Check | `37109616263` | PASS |

The release candidate remains a draft. Public deployment still requires hosted-browser review, hosted-Colab acceptance, private-control testing, final content freeze and coordinated merge approval.

## Release status | حالة الإصدار

```text
UNIFIED_STUDENT_GATEWAY: IMPLEMENTED
PORTAL_AUTOMATED_QUALITY: PASS
CROSS_REPOSITORY_COORDINATION: PASS
PRIVATE_CONTROLS_EXPOSED: NO
MERGE_AUTHORISED: NO
PUBLICATION_AUTHORISED: NO
```
