### Ælæctra - A Step Towards More Efficient Danish Natural Language Processing
Ælæctra is a Danish Transformer-based language model created to enhance the variety of Danish NLP resources with a more efficient model compared to previous state-of-the-art (SOTA) models. 

Ælæctra was pretrained with the ELECTRA-Small (Clark et al., 2020) pretraining approach by using the Danish Gigaword Corpus (Strømberg-Derczynski et al., 2020) and evaluated on Named Entity Recognition tasks. 

#### Released Models

Initially two pretrained models are released:

| Model | Layers | Hidden Size | Params | AVG NER micro-f1 (DaNE-testset) | Average Inference Time (Sec/Epoch) | Download |
| --- | --- | --- | --- | ---  | --- |
| Ælæctra-Uncased | 12 | 256 | 13.7M | 78.03 (SD = 1.28) | 10.91 | [link](https://www.dropbox.com/s/cag7prs1nvdchqs/%C3%86l%C3%A6ctra.zip?dl=0) |
| Ælæctra-Cased | 12 | 256 | 14.7M | 80.08 (SD = 0.26) | 10.92 | [link](https://www.dropbox.com/s/cag7prs1nvdchqs/%C3%86l%C3%A6ctra.zip?dl=0) |

On [DaNE](https://danlp.alexandra.dk/304bd159d5de/datasets/ddt.zip) (Hvingelby et al., 2020), Ælæctra scores slightly worse than both cased and uncased Multilingual BERT (Devlin et al., 2019) and Danish BERT (Danish BERT, 2019/2020), however, is more than 3 times faster at inference time. For a full description of the evaluation and specification of the model read the thesis: 'Ælæctra - A Step Towards More Efficient Danish Natural Language Processing'. 

#### Pretraining
To pretrain Ælæctra it is recommended to build a Docker Container from the [Dockerfile](https://github.com/MalteHB/Ælæctra/tree/master/notebooks/fine-tuning/). Next, simply follow the [pretraining notebooks](https://github.com/MalteHB/Ælæctra/tree/master/infrastructure/Dockerfile/) 

The pretraining was done by utilizing a single NVIDIA Tesla V100 GPU with 16 GiB, endowed by the Danish data company [KMD](https://www.kmd.dk/). The pretraining took approximately 4 days and 9.5 hours for both the cased and uncased model

#### Fine-tuning
To fine-tune any Ælæctra model follow the [fine-tuning notebooks](https://github.com/MalteHB/Ælæctra/tree/master/notebooks/fine-tuning/)

#### References
Clark, K., Luong, M.-T., Le, Q. V., & Manning, C. D. (2020). ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators. ArXiv:2003.10555 [Cs]. http://arxiv.org/abs/2003.10555

Danish BERT. (2020). BotXO. https://github.com/botxo/nordic_bert (Original work published 2019)

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. ArXiv:1810.04805 [Cs]. http://arxiv.org/abs/1810.04805

Hvingelby, R., Pauli, A. B., Barrett, M., Rosted, C., Lidegaard, L. M., & Søgaard, A. (2020). DaNE: A Named Entity Resource for Danish. Proceedings of the 12th Language Resources and Evaluation Conference, 4597–4604. https://www.aclweb.org/anthology/2020.lrec-1.565

Strømberg-Derczynski, L., Baglini, R., Christiansen, M. H., Ciosici, M. R., Dalsgaard, J. A., Fusaroli, R., Henrichsen, P. J., Hvingelby, R., Kirkedal, A., Kjeldsen, A. S., Ladefoged, C., Nielsen, F. Å., Petersen, M. L., Rystrøm, J. H., & Varab, D. (2020). The Danish Gigaword Project. ArXiv:2005.03521 [Cs]. http://arxiv.org/abs/2005.03521


#### Acknowledgements
As the majority of this repository is build upon [the works](https://github.com/google-research/electra) by the team at Google who created ELECTRA, a HUGE thanks to them is in order. 

#### Contact

For help or further information feel free to connect with the author Malte Højmark-Bertelsen on any of the following platforms:

[<img align="left" alt="MalteHB | Twitter" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />][twitter]
[<img align="left" alt="MalteHB | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="MalteHB | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />][instagram]
[<img align="left" alt="MalteHB | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@3.13.0/icons/mail-dot-ru.svg" />][email]

<br />

</details>

[twitter]: https://twitter.com/malteH_B
[instagram]: https://www.instagram.com/maltemusen/
[linkedin]: https://www.linkedin.com/in/malte-h%C3%B8jmark-bertelsen-9a618017b/
[email]: hjb@kmd.dk
