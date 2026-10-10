# 🧾 FairBill: Your Automated Consumer Advocate

An AI-powered multi-category bill auditing and legal compliance dashboard designed to expose predatory hidden fees, duplicate entries, and illegal tax line items instantly.

## 🚀 The Core Problem
Corporations, medical institutions, and utility providers intentionally write billing statements using confusing jargon and complex formats because they know **99% of consumers will just pay without reviewing them**. This asymmetry costs individuals thousands of rupees annually in unnecessary charges.

## 💡 Our Solution
**FairBill** serves as an intelligent financial guardian right in your pocket. Users simply snap a photo or upload an invoice. Leveraging cutting-edge multimodal vision models, the system dynamically:
1. **Parses & Extracts** raw structured billing metrics from images.
2. **Audits Rules** against hyper-local regional consumer laws (such as Indian GST thresholds or service charge mandates).
3. **Exposes Frauds** by flagging inflated prices, duplicate service rounds, or junk administration fees.
4. **Drafts Legal Remedies** by autogenerating ready-to-send official consumer dispute forms.

---

## 🛠️ Multi-Category Matrix Supported
*   🏥 **Hospital Invoices:** Catches duplicate round check-ups and room-rent GST compliance errors (e.g., illegal 18% GST application on standard non-ICU rooms under ₹5,000/day).
*   🍔 **Restaurant Receipts:** Targets hidden "Service Charge" traps (reminding users it is strictly voluntary) and incorrect 18% GST inflation instead of the standard 5% restaurant markup.
*   ⚡ **Electricity Bills:** Decodes confusing tier/slab distributions and highlights invalid fixed-tariff penalties or sudden fuel adjustments.
*   🛒 **Grocery Receipts:** cross-checks item values directly against regional printed Maximum Retail Prices (MRP) to catch retail vendor markup pricing fraud.

---

## 🏗️ Tech Stack
*   **Frontend UI:** Streamlit (Python-native reactive dashboard engine)
*   **AI Orchestration Layer:** Google Gemini API 
*   **Vision/OCR Subsystem:** Multimodal Input Vision Tokens
*   **Data Models:** Pillow (Image preprocessing) & Pandas (Tabular evaluations)

---

## 💻 Local Installation & Setup

Follow these steps to run the interactive system deployment pipeline locally on your machine:

### 1. Clone & Navigate
```bash
git clone https://github.com
cd Fairbill
```

### 2. Configure Virtual Environment
```bash
python -m venv venv
# On Windows Command Prompt:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Dependency Onboarding
```bash
pip install streamlit google-genai pillow
```

### 4. Setup Local Secrets Environment
Create a file named `.env` in the root directory and securely reference your token parameter:
```text
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Start Application Portal
```bash
streamlit run app.py
```

---

## 🔮 Future Scalability Map
*   **Automated Background Ingestion:** Deep integration linking directly into user email platforms to automatically ingest and screen utility invoices as they arrive.
*   **Crowdsourced Pricing Aggregators:** Compiling anonymous pricing databases to alert localized consumers when they are paying significantly higher averages than neighbors for identical services.
*   **Direct Court Filings:** Linking finalized legal draft layouts directly into digital national consumer portal pipelines for instantaneous dispute submission.
*