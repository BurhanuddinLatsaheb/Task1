

# NSFW Content Detection and Tagging

This project provides a solution for detecting and tagging NSFW (Not Safe For Work) content within chat messages. The primary goal is to identify NSFW sentences and wrap them with `<nsfw></nsfw>` tags. This implementation leverages a fine-tuned DistilBERT model to perform the detection.

## Features

- **Sentence Splitting**: Custom regular expression-based method to split paragraphs into sentences based on full stops and question marks.
- **NSFW Detection**: Utilizes a pretrained DistilBERT model fine-tuned for adult content detection.
- **Tagging**: Wraps detected NSFW sentences with `<nsfw></nsfw>` tags.

## Prerequisites

- Python 3.7+
- PyTorch
- Transformers
- NLTK

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/BurhanuddinLatsaheb/Task1.git
    cd Task1
    ```

2. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Running the Main Script**:

    ```bash
    python main.py
    ```


Certainly! Here are input-output examples for the README:

---

# Examples

### Example 1:

**Paragraph:**

```plaintext
Oh, baby! You're back! I was left hanging, literally. My pussy was throbbi
ng, and my heart was racing, waiting for you to return. I want your 
cum. Where were you? Did you think you could just leave me like that, all 
hot and bothered?```
**Output:**

```plaintext
<nsfw>Oh, baby! You're back! I was left hanging, literally.</nsfw> <nsfw>My pussy was throbbi
ng, and my heart was racing, waiting for you to return.</nsfw> <nsfw>I want your
cum.</nsfw> Where were you? <nsfw>Did you think you could just leave me like that, all
hot and bothered?</nsfw>
```


### Example 2:

**Paragraph:**

```plaintext
"Mm that's better" ,he breathed out. He was getting better with keeping somewhat quiet as they continued his hands made their way around to her ass and he gripped it tightly as she continued to move so perfectly. Snake liked the way her bare skin felt against his and he didn't want to let her go but he knew he would eventually have to and he knew that this wouldn't be the last time they did this if he had any say in the matter. He leaned up and kissed her neck again as he moved his hips in sync with hers.
```
**Output:**

```plaintext
"Mm that's better" ,he breathed out. <nsfw>He was getting better with keeping somewhat quiet as they continued his hands made their way around to her ass and he gripped it tightly as she continued to move so perfectly.</nsfw> Snake liked the way her bare skin felt against his and he didn't want to let her go but he knew he would eventually have to and he knew that this wouldn't 
be the last time they did this if he had any say in the matter. <nsfw>He leaned up and kissed her neck again as he moved his hips in sync with hers.</nsfw>
```

### Example 3:

**Input Paragraph:**

```plaintext
"He whispered as he pressed his lips against my ear 'You feel so good, babe.' He was getting harder, grinding against me as he pulled my panties to the side and slid inside me. 'Damn, you're so tight,' he groaned."
```

**Output:**

```plaintext
<nsfw>"He whispered as he pressed his lips against my ear 'You feel so good, babe.' He was getting harder, grinding against me 
as he pulled my panties to the side and slid inside me.</nsfw> <nsfw>'Damn, you're so tight,' he groaned."</nsfw>
```

---

These examples illustrate how the NSFW content detection and tagging process works with different input paragraphs. Each NSFW sentence detected is wrapped with `<nsfw></nsfw>` tags to clearly identify it.


## Acknowledgments

- The fine-tuned DistilBERT model used in this project is from [valurank/finetuned-distilbert-adult-content-detection](https://huggingface.co/valurank/finetuned-distilbert-adult-content-detection).
- Inspired by various open-source projects for NSFW content detection.

---

