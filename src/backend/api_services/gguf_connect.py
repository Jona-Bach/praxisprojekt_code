from llama_cpp import Llama
import os, contextlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

foldername = "gemma-3-1b"
modelname = "gemma-3-1b-it-q4_0.gguf"

MODEL_PATH = BASE_DIR / "models" / foldername / modelname

if not MODEL_PATH.exists():
    MODEL_PATH = Path.cwd() / "models" / foldername / modelname

assert MODEL_PATH.exists(), f"Modelldatei nicht gefunden: {MODEL_PATH}"

with open(os.devnull, "w") as f, contextlib.redirect_stdout(f), contextlib.redirect_stderr(f):
    llm = Llama(
        model_path=str(MODEL_PATH),
        n_ctx=4096, # Kontextlänge
        n_threads=4,# CPu Kerne die genutzt werden
        verbose=False,
    )

messages = [
    {"role": "system", "content": "Be as friendly as possible"},
    {"role": "user", "content": "Can you find the Number which is used to go from x to y: x = [1,2,3] y = [10,20,30]"},
]
resp = llm.create_chat_completion(messages=messages, max_tokens=500, temperature=0.7)
print(resp["choices"][0]["message"]["content"].strip())