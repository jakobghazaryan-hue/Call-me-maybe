import json
from llm_sdk import Small_LLM_Model

model = Small_LLM_Model()
path = model.get_path_to_vocab_file()
print("Ֆայլ:", path)

with open(path, "r", encoding="utf-8") as f:
    vocab = json.load(f)

print("Տիպը:", type(vocab), "Չափը:", len(vocab))
print(list(vocab.items())[:10])

for token in ["{", '"', "2", "Ġsum", "Ġ"]:
    print(repr(token), "→", vocab.get(token))

id_to_token = {v: k for k, v in vocab.items()}
print(id_to_token[2629], id_to_token[17], id_to_token[220])
