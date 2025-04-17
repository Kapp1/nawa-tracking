# 👾 NAWA Realtime Face Matcher SDK & Dashboard

[![PyPI version](https://img.shields.io/pypi/v/nawa-tracking?color=blue)](https://pypi.org/project/nawa-tracking/)
[![Tests](https://github.com/Kapp1/nawa-tracking/actions/workflows/ci.yml/badge.svg)](https://github.com/Kapp1/nawa-tracking/actions)
[![Deploy](https://img.shields.io/badge/Live-Dashboard-brightgreen?logo=streamlit)](https://nawa-tracking.streamlit.app)
[![License](https://img.shields.io/github/license/Kapp1/nawa-tracking)](LICENSE)
[![Streamlit demo](https://img.shields.io/badge/Live-Demo--streamlit.app-brightgreen?logo=streamlit&style=flat-square)](https://nawa-tracking.streamlit.app)

**Smart pilgrim management toolkit.**  
Face recognition, behavior monitoring, real-time Streamlit dashboard, and auto-generated PDF reports.


---

## ⚙ Installation

Install from PyPI:

```bash
pip install nawa-tracking
```

Or install the development version:

```bash
pip install git+https://github.com/Kapp1/nawa-tracking.git
```

---

## 📊 Live Dashboard

Run locally with Streamlit:

```bash
git clone https://github.com/Kapp1/nawa-tracking
cd nawa-tracking
pip install -e .[dashboard]
streamlit run app.py
```

Or use the hosted version: [nawa-tracking.streamlit.app](https://nawa-tracking.streamlit.app)

---

## ✅ Run Tests

```bash
pytest -q
```

---

## 📦 Extras

| Feature              | Quick hint                                                                 |
|----------------------|----------------------------------------------------------------------------|
| **Docker image**     | `FROM python:3.11-slim` → CMD `["streamlit", "run", "app.py"]`             |
| **Streamlit Cloud**  | Add `streamlit config.toml` with `[server] enableXsrfProtection = false`   |
| **AWS Beanstalk**    | Use Dockerfile above, push via EB CLI                                      |

---

## 📄 License

Licensed under the [Apache 2.0 License](LICENSE)

---

### 🧠 What’s next?

1. `git add README.md`
2. `git commit -m "Update README with badges and full instructions"`
3. `git push origin main`

Done ✅ If you need help recording a short demo video or adding animated previews, let me know.
```

---
