from huggingface_hub import hf_hub_download

# Download the model checkpoint
hf_hub_download(repo_id="youmebangbang/vits_tts_models", filename="neil_degrasse_tyson_checkpoint_1910000.pth", local_dir="/home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits")

# Download the config.json file
hf_hub_download(repo_id="youmebangbang/vits_tts_models", filename="config.json", local_dir="/home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits")
