import subprocess
import os
import sys
from groq import Groq
from dotenv import load_dotenv

# Setup API
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("⚠️ API Key missing! Skipping AI Review.")
    sys.exit(0) # Let the commit pass if no key

client = Groq(api_key=api_key)

def get_staged_changes():
    """Git se sirf wo code nikalna jo abhi commit hone wala hai"""
    result = subprocess.run(['git', 'diff', '--cached'], capture_output=True, text=True)
    return result.stdout

def review_code(diff_text):
    """Llama 3.1 ko strict senior dev banakar code check karwana"""
    if not diff_text.strip():
        return "PASS"

    system_prompt = """
    You are an elite, extremely strict Senior Software Engineer. 
    Review the provided git diff. Look for:
    1. Hardcoded secrets/passwords.
    2. Print statements left by mistake.
    3. Syntax errors or obvious bugs.
    
    If the code is clean and safe, respond ONLY with the word "PASS".
    If there are issues, respond with "FAIL" followed by a short explanation of the problem.
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Review this code diff:\n\n{diff_text}"}
            ],
            temperature=0.1 # Kam temperature yani strict aur to-the-point
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error calling AI: {e}")
        return "PASS" # Error aane par commit block na ho

if __name__ == "__main__":
    print("🤖 AI Gatekeeper: Scanning your code...")
    changes = get_staged_changes()
    
    review_result = review_code(changes)
    
    if review_result.strip() == "PASS":
        print("✅ Code looks solid! Commit allowed.")
        sys.exit(0) # 0 means Success for Git
    else:
        print("\n❌ AI GATEKEEPER BLOCKED YOUR COMMIT!")
        print("="*40)
        print(review_result)
        print("="*40)
        print("\nPlease fix the issues and try committing again.")
        sys.exit(1) # 1 means Fail/Block for Git
