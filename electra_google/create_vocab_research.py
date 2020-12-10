
# coding: utf-8

# In[1]:


from tokenizers import BertWordPieceTokenizer
import os


# In[2]:


os.listdir()


# In[ ]:


tokenizer = BertWordPieceTokenizer(
    clean_text=True, 
    handle_chinese_chars=False,
    strip_accents=False,
    lowercase=False, 
)

trainer = tokenizer.train( 
    "/bachelor_project/data/sentences.txt",
    vocab_size=100000,
    min_frequency=2,
    show_progress=True,
    special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
    limit_alphabet=1000,
    wordpieces_prefix="##"
)

tokenizer.save("./", "cased-100k")


# In[ ]:


tokenizer = BertWordPieceTokenizer(
    clean_text=True,
    handle_chinese_chars=False,
    strip_accents=False,  # We need to investigate that further (stripping helps?)
    lowercase=True,
)

trainer = tokenizer.train(
    "/bachelor_project/data/sentences.txt",
    vocab_size=100000,
    min_frequency=2,
    show_progress=True,
    special_tokens=['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]'],
    limit_alphabet=1000,
    wordpieces_prefix="##"
)

tokenizer.save("./", "uncased-100k")

