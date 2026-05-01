# 🛡️ AI Gatekeeper Hook

**AI Gatekeeper** is a custom Git pre-commit hook powered by the **Llama 3.1** model via the Groq API. It introduces "Shift-Left Security" directly into the developer workflow by acting as an automated, strict Senior Engineer. 

Before any code is committed locally, the AI reviews the staged diff to prevent bad practices, leaked secrets, and bugs from ever reaching the repository.

---

## 🚀 Features

*   **Shift-Left Security**: Catches issues at the commit stage, before CI pipelines even run.
*   **Secret Detection**: Automatically blocks commits containing hardcoded API keys, passwords, or tokens.
*   **Code Quality Enforcement**: Flags unnecessary debugging artifacts like rogue `print()` statements.
*   **Ultra-Fast Execution**: Leverages Groq's lightning-fast inference to ensure the pre-commit process doesn't slow down the developer workflow.
*   **Context-Aware Reviews**: Provides human-readable feedback on exactly why a commit was rejected and how to fix it.

---

## 🛠️ Tech Stack

*   **Language**: Python 3
*   **AI Engine**: Llama 3.1-8b-instant (via Groq API)
*   **Integration**: Git Hooks (`pre-commit`)

---

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/nileshdash25/ai-gatekeeper-hook.git](https://github.com/nileshdash25/ai-gatekeeper-hook.git)
   cd ai-gatekeeper-hook
