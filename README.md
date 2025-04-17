```markdown
# 🕋 NAWA‑tracking · Realtime Face‑Match SDK

[![PyPI](https://img.shields.io/pypi/v/nawa-tracking.svg?logo=pypi&color=blue&style=flat-square)](https://pypi.org/project/nawa-tracking)
[![Streamlit demo](https://img.shields.io/badge/Live‑Demo-streamlit.app-brightgreen?logo=streamlit&style=flat-square)](https://nawa-tracking.streamlit.app)
[![License: Apache‑2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg?style=flat-square)](LICENSE)

> **Python SDK + PoC dashboard** for the **NAWA** Smart Pilgrim Platform —  
> Edge‑AI face matching, behavioural analytics, and on‑the‑fly PDF reporting.

---

## ⚡ Install

```bash
pip install nawa-tracking
```

> Latest dev snapshot:
> `pip install git+https://github.com/Kapp1/nawa-tracking.git`

---

## ▶️ Try the live dashboard

```bash
git clone https://github.com/Kapp1/nawa-tracking
cd nawa-tracking
pip install -e .[dashboard]          # streamlit + plotly + pandas
streamlit run app.py                 # open http://localhost:8501
```

To enable AWS Rekognition, add secrets to 
`.streamlit/secrets.toml`:

```toml
AWS_ACCESS_KEY_ID     = "XXX"
AWS_SECRET_ACCESS_KEY = "YYY"
AWS_DEFAULT_REGION    = "me-central-1"
NAWA_COLLECTION       = "NAWA_PILGRIMS"
```

---

## 🔑 Main features

| 🧩 Module         | Purpose                                                         |
|-------------------|-----------------------------------------------------------------|
| `nawa.matcher`    | Rekognition call wrapper / local simulator for latency testing |
| `nawa.behavior`   | Detect forbidden‑zone movement & abnormal patterns             |
| `nawa.report`     | Generate PDF report via **fpdf2**                              |
| `app.py`          | Live Streamlit dashboard (file upload / webcam)                |

---

## 🚀 Deploy recipes

| Scenario              | Quick command                                                                   |
|-----------------------|---------------------------------------------------------------------------------|
| **Docker**            | `docker build -t nawa . && docker run -p8501:8501 nawa`                         |
| **Streamlit Cloud**   | Push repo ▸ Settings ▸ Secrets ▸ add AWS keys                                   |
| **AWS Elastic Beanstalk** | Use Dockerfile above then `eb deploy`                                       |

---

## 🤝 Contributing

Pull requests & issues are welcome.  
See `CONTRIBUTING.md` for style guide and CI rules.

---

## 📄 License

Released under the **Apache 2.0** License. See [LICENSE](LICENSE) for details.
```
