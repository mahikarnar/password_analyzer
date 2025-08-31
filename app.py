import gradio as gr

def analyze_password(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    
    strength = ["❌ Weak", "⚠️ Medium", "✅ Strong"][min(score, 2)]
    return {
        "Strength": strength,
        "Length": len(password),
        "Has Numbers": "Yes" if any(c.isdigit() for c in password) else "No"
    }

iface = gr.Interface(
    fn=analyze_password,
    inputs="text",
    outputs="json",
    title="Password Checker",
    examples=[["password"], ["Password1"], ["P@ssw0rd"]]
)


iface.launch(server_port=7860)
