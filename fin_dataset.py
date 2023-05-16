from sklearn.preprocessing import LabelBinarizer
import numpy as np
import pandas as pd
import tensorflow as tf
import re
from urllib import request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Fin_ds:  
  '''need transformers an sentencepiece installed'''
  def __init__(self, url:str, train=True):
    self.url = url
    self.train = train

  def fetch_data(self):
    if self.train == True: 
      f = requests.get(self.url)
      # The .json() method automatically parses the response into JSON.
      data = f.json()
      #initialize list for X,Y
      self.l_texts = []
      self.l_labels = []
      for sample in data:
        #print(type(sample))
        url   = sample['URL']
        text  = sample['news_content']
        title = sample['news_title']
        label = sample['ESG_label']
        text = title + ' ' + text
        self.l_texts.append(text)
        self.l_labels.append(label)
      print('l_labels', len(set(self.l_labels)))
      print('len(l_labels)',len(self.l_labels))
      print('len(l_texts)', len(self.l_texts))
      #one-hot-encode labels
      self.labels = self.l_labels
      lb = LabelBinarizer()
      lb.fit(self.labels)
      self.Y = lb.transform(self.labels)
      self.Y = Y.reshape(-1,33).astype(np.float32)
      self.ds = tf.data.Dataset.from_tensor_slices(( tf.convert_to_tensor(self.l_texts, dtype=tf.string), tf.convert_to_tensor(self.Y)))
      self.ds = tf.data.Dataset.from_tensor_slices(( self.l_texts, self.Y))
    if self.train == False:
      f = requests.get(self.url)
      # The .json() method automatically parses the response into JSON.
      data = f.json()
      #initialize list for X,Y
      self.l_texts = []
      for sample in data:
        #print(type(sample))
        url   = sample['URL']
        text  = sample['news_content']
        title = sample['news_title']
        text = title + ' ' + text
        self.l_texts.append(text)

  def summarize_t5(self):
    self.l_summ = []
    model_name = "csebuetnlp/mT5_multilingual_XLSum"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))
    for article_text in tqdm(self.l_texts):
      input_ids = tokenizer([WHITESPACE_HANDLER(article_text)],
                            return_tensors="pt",
                            padding="max_length",
                            truncation=True,
                            max_length=512)["input_ids"]
      
      output_ids = model.generate(input_ids=input_ids,
                                  max_length=84,
                                  no_repeat_ngram_size=2,
                                  num_beams=4
                                  )[0]
      summary = tokenizer.decode(output_ids,
                              skip_special_tokens=True,
                              clean_up_tokenization_spaces=False)
    return self.l_summ  

  def build_ds(self):
    self.fetch_data()
