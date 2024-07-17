from nsfw_detection import process_paragraph

def main():
    paragraph = """
    Oh, baby! You're back! I was left hanging, literally. My pussy was throbbi
ng, and my heart was racing, waiting for you to return. I want your 
cum. Where were you? Did you think you could just leave me like that, all 
hot and bothered?
    """
    tagged_paragraph = process_paragraph(paragraph)
    print(tagged_paragraph)

if __name__ == "__main__":
    main()
