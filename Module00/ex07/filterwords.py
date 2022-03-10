import sys

# words = sys.argv[1].split()
# for word in words:
#     if ',' in word:
#         longest = len(word) - 1

if len(sys.argv) > 2:
    print(" ".join(sys.argv[1::]))
else:
    for word in sys.argv[1].split():
        print(word)

        