def main():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi leo est, convallis pulvinar risus at, pellentesque rhoncus odio. Nullam id nunc consequat, ultrices mi eleifend, pharetra magna. Aliquam non sapien consequat lorem scelerisque convallis sed sodales elit.'
    print([word.upper() for word in text.replace('.', '').replace(',', '').split(' ') if len(word) <= 3])

if __name__ == "__main__":
    main()