# 🕋 nawa-tracking

[![PyPI version](https://img.shields.io/pypi/v/nawa-tracking.svg?color=blue&logo=python&label=PyPI&style=flat-square)](https://pypi.org/project/nawa-tracking/)
[![PyPI version](https://img.shields.io/pypi/v/nawa-tracking)](https://pypi.org/project/nawa-tracking/)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg?style=flat-square)](https://opensource.org/licenses/Apache-2.0)

> **Python SDK & PoC** for the NAWA Smart Pilgrim Management Platform  
> AI-powered facial-matching, behaviour analysis, and PDF reporting.

---

## ⚡ Quick install

```bash
- pip install git+https://github.com/Kapp1/nawa-tracking.git
+ pip install nawa-tracking
```

---

## 📺 Try the live dashboard

```bash
git clone https://github.com/Kapp1/nawa-tracking
cd nawa-tracking && pip install -e .[dashboard]   # or install streamlit, plotly manually
streamlit run app.py
```

---

## 🧩 (Optional) Extras

| Feature                      | Quick hint                                                                  |
|-----------------------------|------------------------------------------------------------------------------|
| **Docker image**            | `FROM python:3.11-slim` → `CMD ["streamlit","run","app.py"]`                |
| **Auth on Streamlit Cloud** | Add `~/.streamlit/config.toml` with `[server] enableXsrfProtection = false` |
| **Deploy on AWS**           | Use Dockerfile above, push via EB CLI or any containerized workflow         |

---

## ✅ What’s next?

- [ ] Add QR & face thumbnail to PDF
- [ ] Auto-logging into SQLite
- [ ] CI/CD auto-publish via GitHub Actions
- [ ] Arabic/English dual-mode UI
