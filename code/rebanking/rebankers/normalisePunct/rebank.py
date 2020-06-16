from rebanking.rebankers import normalisePunct
from rebanking.rebankers import mainWrapper

main = mainWrapper(normalisePunct.doSentence)

if __name__ == '__main__':
    main()
