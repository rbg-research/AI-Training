
## Introduction

This repo consists of files built for the term project, that was presented for the subject Speech Procesing(20DS705) as a part of our M.Tech curriculum.
## Authors

This work was equally contributed by,
- [Rahesh.R ](https://github.com/Some1OutThere)- CB.EN.P2CEN20021
- [B.Sachin Aditiya](https://github.com/sachinaditiya)- CB.EN.P2CEN20030
## Models

The models used for Speech to Text conversion are:
- [Jasper](https://arxiv.org/abs/1904.03288)
- [fairseq S2T](https://arxiv.org/abs/2010.05171)

## Dataset

The dataset used for this task is [LibriSpeech ASR corpus](https://www.openslr.org/12/).
This dataset can also be downloaded from [huggingface🤗](https://huggingface.co/datasets/librispeech_asr).

## Evaluation metrics

The performance of the models are evaluated using [Word Error Rate (WER)](https://huggingface.co/metrics/wer).

## Results

The WERs we achieved for the LibriSpeech test-clean dataset are:
- Jasper - 4.1%
- fairseq S2T - 3.74%
## References

https://catalog.ngc.nvidia.com/orgs/nvidia/resources/jasper_for_pytorch
https://huggingface.co/facebook/s2t-medium-librispeech-asr
https://nvidia.github.io/OpenSeq2Seq/html/speech-recognition.html#speech-recognition
https://github.com/NVIDIA/OpenSeq2Seq

## License

[MIT](https://choosealicense.com/licenses/mit/)

