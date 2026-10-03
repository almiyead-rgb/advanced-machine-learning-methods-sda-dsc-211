# Phase 3 — Production Bilingual Course Portal

## Scope

This phase promotes the bilingual portal design from a prototype into the production `index.html` candidate for `v1.1.0`. The published `main` portal remains unchanged until the controlled pull request is approved and merged.

## Production files

- `index.html`
- `bilingual-v1.1.css`
- `scripts/check_portal.py`
- `.github/workflows/portal_quality.yml`

## User experience

Desktop layout uses two equal columns:

- English on the left with explicit LTR direction.
- Arabic on the right with explicit RTL direction.

Narrow screens stack the language panels and remove the requirement for horizontal scrolling. The portal supports keyboard navigation, skip-to-content, visible focus states and reduced-motion preferences.

## Portal sections

- Course promise and project outcome.
- Tamweel Lite educational scenario and responsible-use boundary.
- Prerequisites and beginner readiness route.
- Five-day progressive learning journey.
- 90-point project and 10-point presentation assessment model.
- Final delivery journey: complete, verify, freeze and submit.
- Beginner support links for Colab, GitHub, troubleshooting, FAQ and learning resources.
- Instructor attribution and non-official SDAIA-account disclaimer.

## Technical and governance alignment

The portal is synchronised with the learner-template policies:

- free Colab CPU;
- no GPU, API key, paid subscription or Drive mount;
- one connected five-day project;
- one complete final submission;
- Notebook 99 plus GitHub Actions verification;
- exact tag and commit SHA;
- private cohort submission channel;
- technical readiness is not a grade or receipt;
- integrity gates remain mandatory.

## Discoverability and accessibility

The production candidate includes:

- canonical URL;
- Arabic and English `hreflang` links;
- Open Graph metadata;
- Course JSON-LD;
- responsive CSS;
- `prefers-reduced-motion` support;
- print rules;
- semantic landmarks and section anchors.

## Automated quality gate

`Portal Quality Check` validates:

- required production files;
- required section IDs;
- explicit LTR and RTL content;
- canonical URL and language alternates;
- Course JSON-LD;
- bilingual non-official SDAIA disclaimer;
- reduced-motion support;
- local link targets.

Validated run:

- Workflow: `Portal Quality Check`
- Run ID: `37106217755`
- Result: `PASS`

## Release boundary

This phase does not publish `v1.1.0`. Remaining release controls include hosted-browser visual review, hosted-Colab acceptance, final learner-template hashes, private evaluator, private submission registry and coordinated portal/template merge.