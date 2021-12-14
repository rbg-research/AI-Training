
# Speech Processing (20DS705)  

### Team-7
* Aakash Jignesh Modi (CB.EN.P2CEN20001)
* Mredulraj S. Pandianchery (CB.EN.P2CEN20019)
* Vinay R. (CB.EN.P2CEN20028)  
  
  
  
Librispeech (test-clean data) dataset: https://huggingface.co/datasets/librispeech_asr  
Processed Librispeech (test-clean data) dataset created for ease of use and avoiding out of memory problem in colab. Link for processed data https://drive.google.com/drive/folders/1kN-pGEy8P8gOBXn_ilwGKsdJxPx1ZvRz?usp=sharing contains two files:  
* 'file.zip' contains audio files;
* 'test_clean.json' contains the path, length and transcription of audiofiles as a dictionary.  

Models worked on:
* Conformer
* HuBERT

Word Error Rate(WER) with Language Model (LM):
* Conformer: 0.0258
* HuBERT: 0.0201
