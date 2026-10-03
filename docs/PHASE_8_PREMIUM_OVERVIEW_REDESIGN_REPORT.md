# Phase 8 — Premium Course Overview Redesign
# المرحلة 8 — إعادة تصميم الواجهة التنفيذية للدورة

## Decision | القرار

The course portal now uses a clear information hierarchy rather than one dense block. The supplied MEAAD image is placed inside a dedicated square logo tile, followed by the Arabic course name and the English subtitle.

تعتمد البوابة الآن تسلسلاً بصريًا واضحًا بدل تجميع المحتوى في كتلة واحدة. وُضعت صورة MEAAD المرفقة داخل مربع مستقل، يليها اسم الدورة بالعربية والعنوان الإنجليزي.

## Implemented structure | الهيكل المنفذ

1. Premium hero with the supplied logo and course name.
2. Separate course overview, five-day journey, learning outcomes and assessment panels.
3. Beginner start path with readiness, template and tool-guide links.
4. Individual Day 1–5 cards with direct Colab and guide actions.
5. Separate project workspace for data, report templates and the final presentation.
6. Separate requirements, assessment, submission and support sections.
7. System Architecture section positioned at the end.

## System architecture | معمارية النظام

```text
Student
→ GitHub Student Repository
→ Google Colab Notebooks 01–05
→ Data, Models and Evidence
→ Notebook 99 Final Evaluation
→ Final Presentation and Private Submission
```

Hidden evaluator data, grades, identities and receipts remain outside the public portal.

تبقى بيانات المقيم المخفية والدرجات والهويات والإيصالات خارج البوابة العامة.

## Visual and UX system | النظام البصري وتجربة المستخدم

- Warm cream, beige, black and restrained gold palette derived from the supplied identity.
- Sections separated by learner purpose rather than decoration.
- English-left and Arabic-right content pairing.
- Responsive mobile stacking.
- Keyboard focus, skip link, reduced motion and print support.
- All learner resources remain connected to the public student template.

## Automated acceptance | القبول الآلي

The quality workflow verifies the logo, course titles, architecture section, required student sections, local assets, responsive CSS, reduced motion, canonical metadata, hreflang, JSON-LD and the SDAIA disclaimer.
