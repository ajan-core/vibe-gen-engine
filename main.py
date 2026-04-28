from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# --- CONFIGURATION ---
# Aapka Space Link: https://janixiaofficial-vibe-gen-engine.hf.space
VALID_KEYS = ["ALI-JAAN-VIP-786", "VIBE-GEN-PRO-2026"]

@app.get("/")
def home():
    return {
        "status": "Online",
        "owner": "Ali Jaan",
        "engine": "Vibe-Gen-Engine-v1",
        "base_url": "https://janixiaofficial-vibe-gen-engine.hf.space"
    }

@app.post("/generate")
def create_movie(prompt: str, api_key: str = Header(None)):
    # Security Check
    if api_key not in VALID_KEYS:
        raise HTTPException(status_code=401, detail="Galat VIP Key! Access Denied.")

    # Response mein aapka link fit kar diya hai
    return {
        "status": "Success",
        "engine": "Animation-Movie-Edit-v1",
        "prompt_received": prompt,
        "result": "Movie is being processed in 4K...",
        "api_link": "https://janixiaofficial-vibe-gen-engine.hf.space/generate",
        "download_link": "https://your-server-link.com/output.mp4"
    }
    
