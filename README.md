## NOTE  
This is FarziDon's repo. Made for running this code in SageMaker.  
Procedure:-  

- Make a fork of this repo. Clone it, and then add the dataset inside recipe/vits_tts. Then push it back to ur repo (+ PR with main repo also)
- Git clone the final repo and pip install it (Use sudo yum install espeak)  
- You need to do everything in terminal, use vim to open .py files (can work in local and push here also)
- Run the main.py once.
- The model will be stored at /home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits (equivalent of AppData/Local in SageMaker terminal)
- Put the OG pretrained model on HF. Run download.py in vits_tts/model2. It will retrieve the pretrained model config.json and put it in the above mentioned folder
- You would have to then change the model name to model_file.pth
- Once model is fine-tuned, use s3.py in vits_tts/model to save the model in S3 bucket. Download it from there to use.
- When running tensorboard, use the sagemaker notebook url and then add /proxy/8001 at the end of it. https://coquitrainshadan.notebook.ap-south-1.sagemaker.aws/proxy/8001
- Trainer.py is kept here:- /home/ec2-user/anaconda3/envs/pytorch_p310/lib/python3.10/site-packages
- The vits_tts address is this:- /home/ec2-user/TTS/recipes/ljspeech/vits_tts
- Fine-tuning and inference is tested
- Fine-tuning (python train_vits.py —restore_path /home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits/model_file.pth - -coqpit.lr_gen 0.00001 --coqpit.lr_disc 0.00001)

29th Aug:-  
- datasetmaker.py has been added:- It will create datasets of concat_001.wav and a metadata.csv. Add the concat ones NOT the split ones. This will say Surprise at the start of each sentence, and add in the transciption of each split as well
- cleaners.py:- [] brackets won't be removed now  
- Note that the start_audio created by datasetmaker needs to be in the metadata and folder.

6th Sept:-
- git clone into /home/ec2-user/SageMaker for using additional space
- first python main.py -> train the base model downloaded for 1-2 epochs -> Once trained, take the latest checkpt and continue path finetune on it.
- Commands:- CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python -m trainer.distribute --script /home/ec2-user/SageMaker/tts-sage/recipes/ljspeech/vits_tts/train_vits.py --restore_path /home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits/model_file.pth --config_file /home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits/config.json
- CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python -m trainer.distribute --script /home/ec2-user/tts-sage/recipes/ljspeech/vits_tts/train_vits.py --restore_path /home/ec2-user/tts-sage/recipes/ljspeech/vits_tts/vits_ljspeech-September-04-2023_12+45PM-edeb850/checkpoint_1000022.pth --config_path /home/ec2-user/tts-sage/recipes/ljspeech/vits_tts/vits_ljspeech-September-04-2023_12+45PM-edeb850/config.json

23rd October:-  
- For fine-tuning, put the model.pth and config.json (anywhere) in vits_tts. Run the python train_vits.py command, then stop after 1 checkpoint. Take the checkpt.pth and run the same cmd on it again
- CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python -m trainer.distribute --script /home/ec2-user/SageMaker/tts-sage/recipes/ljspeech/vits_tts/train_vits.py --restore_path /home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits/model_file.pth --config_file /home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits/config.json
- CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7" python -m trainer.distribute --script /home/ec2-user/SageMaker/TTS/recipes/ljspeech/vits_tts/train_vits.py --restore_path /home/ec2-user/SageMaker/TTS/recipes/ljspeech/vits_tts/pralok-September-30-2023_12+52PM-af62613c/checkpoint_1970307.pth --config_path/home/ec2-user/SageMaker/TTS/recipes/ljspeech/vits_tts/pralok-September-30-2023_12+52PM-af62613c/config.json
- For running basic inference, first run main.py once. It will create a new folder in /home/ec2-user/.local/share/tts/tts_models--en--ljspeech--vits And store the default model there. Put your model/config.json in that folder to run inference again. If you want to make API. Use the script shadan_flask.py

- Do mixed_precis
## 🐸Coqui.ai News
- 📣 [🐶Bark](https://github.com/suno-ai/bark) is now available for inference with uncontrained voice cloning. [Docs](https://tts.readthedocs.io/en/dev/models/bark.html)
- 📣 You can use [~1100 Fairseq models](https://github.com/facebookresearch/fairseq/tree/main/examples/mms) with 🐸TTS.
- 📣 🐸TTS now supports 🐢Tortoise with faster inference. [Docs](https://tts.readthedocs.io/en/dev/models/tortoise.html)
- 📣 **Coqui Studio API** is landed on 🐸TTS. - [Example](https://github.com/coqui-ai/TTS/blob/dev/README.md#-python-api)
- 📣 [**Coqui Studio API**](https://docs.coqui.ai/docs) is live.
- 📣 Voice generation with prompts - **Prompt to Voice** - is live on [**Coqui Studio**](https://app.coqui.ai/auth/signin)!! - [Blog Post](https://coqui.ai/blog/tts/prompt-to-voice)
- 📣 Voice generation with fusion - **Voice fusion** - is live on [**Coqui Studio**](https://app.coqui.ai/auth/signin).
- 📣 Voice cloning is live on [**Coqui Studio**](https://app.coqui.ai/auth/signin).

<div align="center">
<img src="https://static.scarf.sh/a.png?x-pxid=cf317fe7-2188-4721-bc01-124bb5d5dbb2" />

## <img src="https://raw.githubusercontent.com/coqui-ai/TTS/main/images/coqui-log-green-TTS.png" height="56"/>


**🐸TTS is a library for advanced Text-to-Speech generation.**

🚀 Pretrained models in +1100 languages.

🛠️ Tools for training new models and fine-tuning existing models in any language.

📚 Utilities for dataset analysis and curation.
______________________________________________________________________

[![Dicord](https://img.shields.io/discord/1037326658807533628?color=%239B59B6&label=chat%20on%20discord)](https://discord.gg/5eXr5seRrv)
[![License](<https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg>)](https://opensource.org/licenses/MPL-2.0)
[![PyPI version](https://badge.fury.io/py/TTS.svg)](https://badge.fury.io/py/TTS)
[![Covenant](https://camo.githubusercontent.com/7d620efaa3eac1c5b060ece5d6aacfcc8b81a74a04d05cd0398689c01c4463bb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6e7472696275746f72253230436f76656e616e742d76322e3025323061646f707465642d6666363962342e737667)](https://github.com/coqui-ai/TTS/blob/master/CODE_OF_CONDUCT.md)
[![Downloads](https://pepy.tech/badge/tts)](https://pepy.tech/project/tts)
[![DOI](https://zenodo.org/badge/265612440.svg)](https://zenodo.org/badge/latestdoi/265612440)

![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/aux_tests.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/data_tests.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/docker.yaml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/inference_tests.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/style_check.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/text_tests.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/tts_tests.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/vocoder_tests.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/zoo_tests0.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/zoo_tests1.yml/badge.svg)
![GithubActions](https://github.com/coqui-ai/TTS/actions/workflows/zoo_tests2.yml/badge.svg)
[![Docs](<https://readthedocs.org/projects/tts/badge/?version=latest&style=plastic>)](https://tts.readthedocs.io/en/latest/)

</div>

______________________________________________________________________

## 💬 Where to ask questions
Please use our dedicated channels for questions and discussion. Help is much more valuable if it's shared publicly so that more people can benefit from it.

| Type                            | Platforms                               |
| ------------------------------- | --------------------------------------- |
| 🚨 **Bug Reports**              | [GitHub Issue Tracker]                  |
| 🎁 **Feature Requests & Ideas** | [GitHub Issue Tracker]                  |
| 👩‍💻 **Usage Questions**          | [GitHub Discussions]                    |
| 🗯 **General Discussion**       | [GitHub Discussions] or [Discord]   |

[github issue tracker]: https://github.com/coqui-ai/tts/issues
[github discussions]: https://github.com/coqui-ai/TTS/discussions
[discord]: https://discord.gg/5eXr5seRrv
[Tutorials and Examples]: https://github.com/coqui-ai/TTS/wiki/TTS-Notebooks-and-Tutorials


## 🔗 Links and Resources
| Type                            | Links                               |
| ------------------------------- | --------------------------------------- |
| 💼 **Documentation**              | [ReadTheDocs](https://tts.readthedocs.io/en/latest/)
| 💾 **Installation**               | [TTS/README.md](https://github.com/coqui-ai/TTS/tree/dev#install-tts)|
| 👩‍💻 **Contributing**               | [CONTRIBUTING.md](https://github.com/coqui-ai/TTS/blob/main/CONTRIBUTING.md)|
| 📌 **Road Map**                   | [Main Development Plans](https://github.com/coqui-ai/TTS/issues/378)
| 🚀 **Released Models**            | [TTS Releases](https://github.com/coqui-ai/TTS/releases) and [Experimental Models](https://github.com/coqui-ai/TTS/wiki/Experimental-Released-Models)|
| 📰 **Papers**                    | [TTS Papers](https://github.com/erogol/TTS-papers)|


## 🥇 TTS Performance
<p align="center"><img src="https://raw.githubusercontent.com/coqui-ai/TTS/main/images/TTS-performance.png" width="800" /></p>

Underlined "TTS*" and "Judy*" are **internal** 🐸TTS models that are not released open-source. They are here to show the potential. Models prefixed with a dot (.Jofish .Abe and .Janice) are real human voices.

## Features
- High-performance Deep Learning models for Text2Speech tasks.
    - Text2Spec models (Tacotron, Tacotron2, Glow-TTS, SpeedySpeech).
    - Speaker Encoder to compute speaker embeddings efficiently.
    - Vocoder models (MelGAN, Multiband-MelGAN, GAN-TTS, ParallelWaveGAN, WaveGrad, WaveRNN)
- Fast and efficient model training.
- Detailed training logs on the terminal and Tensorboard.
- Support for Multi-speaker TTS.
- Efficient, flexible, lightweight but feature complete `Trainer API`.
- Released and ready-to-use models.
- Tools to curate Text2Speech datasets under```dataset_analysis```.
- Utilities to use and test your models.
- Modular (but not too much) code base enabling easy implementation of new ideas.

## Model Implementations
### Spectrogram models
- Tacotron: [paper](https://arxiv.org/abs/1703.10135)
- Tacotron2: [paper](https://arxiv.org/abs/1712.05884)
- Glow-TTS: [paper](https://arxiv.org/abs/2005.11129)
- Speedy-Speech: [paper](https://arxiv.org/abs/2008.03802)
- Align-TTS: [paper](https://arxiv.org/abs/2003.01950)
- FastPitch: [paper](https://arxiv.org/pdf/2006.06873.pdf)
- FastSpeech: [paper](https://arxiv.org/abs/1905.09263)
- FastSpeech2: [paper](https://arxiv.org/abs/2006.04558)
- SC-GlowTTS: [paper](https://arxiv.org/abs/2104.05557)
- Capacitron: [paper](https://arxiv.org/abs/1906.03402)
- OverFlow: [paper](https://arxiv.org/abs/2211.06892)
- Neural HMM TTS: [paper](https://arxiv.org/abs/2108.13320)
- Delightful TTS: [paper](https://arxiv.org/abs/2110.12612)

### End-to-End Models
- VITS: [paper](https://arxiv.org/pdf/2106.06103)
- 🐸 YourTTS: [paper](https://arxiv.org/abs/2112.02418)
- 🐢 Tortoise: [orig. repo](https://github.com/neonbjb/tortoise-tts)
- 🐶 Bark: [orig. repo](https://github.com/suno-ai/bark)

### Attention Methods
- Guided Attention: [paper](https://arxiv.org/abs/1710.08969)
- Forward Backward Decoding: [paper](https://arxiv.org/abs/1907.09006)
- Graves Attention: [paper](https://arxiv.org/abs/1910.10288)
- Double Decoder Consistency: [blog](https://erogol.com/solving-attention-problems-of-tts-models-with-double-decoder-consistency/)
- Dynamic Convolutional Attention: [paper](https://arxiv.org/pdf/1910.10288.pdf)
- Alignment Network: [paper](https://arxiv.org/abs/2108.10447)

### Speaker Encoder
- GE2E: [paper](https://arxiv.org/abs/1710.10467)
- Angular Loss: [paper](https://arxiv.org/pdf/2003.11982.pdf)

### Vocoders
- MelGAN: [paper](https://arxiv.org/abs/1910.06711)
- MultiBandMelGAN: [paper](https://arxiv.org/abs/2005.05106)
- ParallelWaveGAN: [paper](https://arxiv.org/abs/1910.11480)
- GAN-TTS discriminators: [paper](https://arxiv.org/abs/1909.11646)
- WaveRNN: [origin](https://github.com/fatchord/WaveRNN/)
- WaveGrad: [paper](https://arxiv.org/abs/2009.00713)
- HiFiGAN: [paper](https://arxiv.org/abs/2010.05646)
- UnivNet: [paper](https://arxiv.org/abs/2106.07889)

### Voice Conversion
- FreeVC: [paper](https://arxiv.org/abs/2210.15418)

You can also help us implement more models.

## Installation
🐸TTS is tested on Ubuntu 18.04 with **python >= 3.7, < 3.11.**.

If you are only interested in [synthesizing speech](https://tts.readthedocs.io/en/latest/inference.html) with the released 🐸TTS models, installing from PyPI is the easiest option.

```bash
pip install TTS
```

If you plan to code or train models, clone 🐸TTS and install it locally.

```bash
git clone https://github.com/coqui-ai/TTS
pip install -e .[all,dev,notebooks]  # Select the relevant extras
```

If you are on Ubuntu (Debian), you can also run following commands for installation.

```bash
$ make system-deps  # intended to be used on Ubuntu (Debian). Let us know if you have a different OS.
$ make install
```

If you are on Windows, 👑@GuyPaddock wrote installation instructions [here](https://stackoverflow.com/questions/66726331/how-can-i-run-mozilla-tts-coqui-tts-training-with-cuda-on-a-windows-system).


## Docker Image
You can also try TTS without install with the docker image.
Simply run the following command and you will be able to run TTS without installing it.

```bash
docker run --rm -it -p 5002:5002 --entrypoint /bin/bash ghcr.io/coqui-ai/tts-cpu
python3 TTS/server/server.py --list_models #To get the list of available models
python3 TTS/server/server.py --model_name tts_models/en/vctk/vits # To start a server
```

You can then enjoy the TTS server [here](http://[::1]:5002/)
More details about the docker images (like GPU support) can be found [here](https://tts.readthedocs.io/en/latest/docker_images.html)


## Synthesizing speech by 🐸TTS

### 🐍 Python API

```python
from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)

# Run TTS

# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# Text to speech to a file
tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")
```

#### Running a single speaker model

```python
# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)
# Run TTS
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path=OUTPUT_PATH)

# Example voice cloning with YourTTS in English, French and Portuguese

tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=True)
tts.tts_to_file("This is voice cloning.", speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
tts.tts_to_file("C'est le clonage de la voix.", speaker_wav="my/cloning/audio.wav", language="fr-fr", file_path="output.wav")
tts.tts_to_file("Isso é clonagem de voz.", speaker_wav="my/cloning/audio.wav", language="pt-br", file_path="output.wav")
```

#### Example voice conversion

Converting the voice in `source_wav` to the voice of `target_wav`

```python
tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False, gpu=True)
tts.voice_conversion_to_file(source_wav="my/source.wav", target_wav="my/target.wav", file_path="output.wav")
```

#### Example voice cloning together with the voice conversion model.
This way, you can clone voices by using any model in 🐸TTS.

```python

tts = TTS("tts_models/de/thorsten/tacotron2-DDC")
tts.tts_with_vc_to_file(
    "Wie sage ich auf Italienisch, dass ich dich liebe?",
    speaker_wav="target/speaker.wav",
    file_path="output.wav"
)
```

#### Example using [🐸Coqui Studio](https://coqui.ai) voices.
You access all of your cloned voices and built-in speakers in [🐸Coqui Studio](https://coqui.ai). 
To do this, you'll need an API token, which you can obtain from the [account page](https://coqui.ai/account).
After obtaining the API token, you'll need to configure the COQUI_STUDIO_TOKEN environment variable.

Once you have a valid API token in place, the studio speakers will be displayed as distinct models within the list. 
These models will follow the naming convention `coqui_studio/en/<studio_speaker_name>/coqui_studio`

```python
# XTTS model
models = TTS(cs_api_model="XTTS").list_models()
# Init TTS with the target studio speaker
tts = TTS(model_name="coqui_studio/en/Torcull Diarmuid/coqui_studio", progress_bar=False, gpu=False)
# Run TTS
tts.tts_to_file(text="This is a test.", file_path=OUTPUT_PATH)

# V1 model
models = TTS(cs_api_model="V1").list_models()
# Run TTS with emotion and speed control
# Emotion control only works with V1 model
tts.tts_to_file(text="This is a test.", file_path=OUTPUT_PATH, emotion="Happy", speed=1.5)

# XTTS-multilingual
models = TTS(cs_api_model="XTTS-multilingual").list_models()
# Run TTS with emotion and speed control
# Emotion control only works with V1 model
tts.tts_to_file(text="Das ist ein Test.", file_path=OUTPUT_PATH, language="de", speed=1.0)
```

#### Example text to speech using **Fairseq models in ~1100 languages** 🤯.
For Fairseq models, use the following name format: `tts_models/<lang-iso_code>/fairseq/vits`.
You can find the language ISO codes [here](https://dl.fbaipublicfiles.com/mms/tts/all-tts-languages.html)
and learn about the Fairseq models [here](https://github.com/facebookresearch/fairseq/tree/main/examples/mms).

```python
# TTS with on the fly voice conversion
api = TTS("tts_models/deu/fairseq/vits")
api.tts_with_vc_to_file(
    "Wie sage ich auf Italienisch, dass ich dich liebe?",
    speaker_wav="target/speaker.wav",
    file_path="output.wav"
)
```

### Command-line `tts`
#### Single Speaker Models

- List provided models:

    ```
    $ tts --list_models
    ```
- Get model info (for both tts_models and vocoder_models):
    - Query by type/name:
        The model_info_by_name uses the name as it from the --list_models.
        ```
        $ tts --model_info_by_name "<model_type>/<language>/<dataset>/<model_name>"
        ```
        For example:

        ```
        $ tts --model_info_by_name tts_models/tr/common-voice/glow-tts
        ```
        ```
        $ tts --model_info_by_name vocoder_models/en/ljspeech/hifigan_v2
        ```
    - Query by type/idx:
        The model_query_idx uses the corresponding idx from --list_models.
        ```
        $ tts --model_info_by_idx "<model_type>/<model_query_idx>"
        ```
        For example:

        ```
        $ tts --model_info_by_idx tts_models/3
        ```

- Run TTS with default models:

    ```
    $ tts --text "Text for TTS" --out_path output/path/speech.wav
    ```

- Run a TTS model with its default vocoder model:

    ```
    $ tts --text "Text for TTS" --model_name "<model_type>/<language>/<dataset>/<model_name>" --out_path output/path/speech.wav
    ```
  For example:

    ```
    $ tts --text "Text for TTS" --model_name "tts_models/en/ljspeech/glow-tts" --out_path output/path/speech.wav
    ```

- Run with specific TTS and vocoder models from the list:

    ```
    $ tts --text "Text for TTS" --model_name "<model_type>/<language>/<dataset>/<model_name>" --vocoder_name "<model_type>/<language>/<dataset>/<model_name>" --out_path output/path/speech.wav
    ```

  For example:

    ```
    $ tts --text "Text for TTS" --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet" --out_path output/path/speech.wav
    ```


- Run your own TTS model (Using Griffin-Lim Vocoder):

    ```
    $ tts --text "Text for TTS" --model_path path/to/model.pth --config_path path/to/config.json --out_path output/path/speech.wav
    ```

- Run your own TTS and Vocoder models:
    ```
    $ tts --text "Text for TTS" --model_path path/to/model.pth --config_path path/to/config.json --out_path output/path/speech.wav
        --vocoder_path path/to/vocoder.pth --vocoder_config_path path/to/vocoder_config.json
    ```

#### Multi-speaker Models

- List the available speakers and choose a <speaker_id> among them:

    ```
    $ tts --model_name "<language>/<dataset>/<model_name>"  --list_speaker_idxs
    ```

- Run the multi-speaker TTS model with the target speaker ID:

    ```
    $ tts --text "Text for TTS." --out_path output/path/speech.wav --model_name "<language>/<dataset>/<model_name>"  --speaker_idx <speaker_id>
    ```

- Run your own multi-speaker TTS model:

    ```
    $ tts --text "Text for TTS" --out_path output/path/speech.wav --model_path path/to/model.pth --config_path path/to/config.json --speakers_file_path path/to/speaker.json --speaker_idx <speaker_id>
    ```

## Directory Structure
```
|- notebooks/       (Jupyter Notebooks for model evaluation, parameter selection and data analysis.)
|- utils/           (common utilities.)
|- TTS
    |- bin/             (folder for all the executables.)
      |- train*.py                  (train your target model.)
      |- ...
    |- tts/             (text to speech models)
        |- layers/          (model layer definitions)
        |- models/          (model definitions)
        |- utils/           (model specific utilities.)
    |- speaker_encoder/ (Speaker Encoder models.)
        |- (same)
    |- vocoder/         (Vocoder models.)
        |- (same)
```
