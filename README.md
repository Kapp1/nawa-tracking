# 🕋 nawa-tracking

> **Python SDK & PoC** for the NAWA Smart Pilgrim Management Platform  
> AI-powered facial-matching, behaviour analysis, and PDF reporting.

---

## ⚡ Quick install

```bash
pip install git+https://github.com/Kapp1/nawa-tracking.git
```

---

## 📺 Try the live dashboard

```bash
git clone https://github.com/Kapp1/nawa-tracking
cd nawa-tracking && pip install -e .[dashboard]   # or install streamlit, plotly manually
streamlit run app.py
```

---

## 🧩 5 – (Optional) Extras

| Feature                      | Quick hint                                                                  |
|-----------------------------|------------------------------------------------------------------------------|
| **Docker image**            | `FROM python:3.11-slim` → `CMD ["streamlit","run","app.py"]`                |
| **Auth on Streamlit Cloud** | Add `~/.streamlit/config.toml` with `[server] enableXsrfProtection = false` |
| **Deploy on AWS**           | Use Dockerfile above, push via EB CLI or any containerized workflow         |

---

## ✅ What’s next?

- [ ] Support Arabic/English dual-language reports.
- [ ] Add face thumbnails inside the PDF.
- [ ] Save match logs to SQLite or Firebase.
- [ ] Add interactive heatmaps for pilgrim movement.
