import random
import json
countris = {}
def load_countris_json():
  with open('countris.json', 'r') as file:
    countris = json.load(file)
    file.close()


def test(countris: dict):
  score = 0
  while countris:
    country = (lambda k: (k, countris.pop(k)))(random.choice(list(countris.keys())))
    if input(f"Столиця {country[0]}?: ").lower() == country[1].lower():
      print("Правильно!")
      score += 1
    else:
      print(f"Ні, столиця {country[0]} це {country[1]}")
  print(f"Ти набрав {score}/{len(countris)}")
if __name__ == "__main__":
  load_countris_json()
  while True:
    if input("Введіть 'q' щоб вийти з програми або Ентер щоб продовжити: ") == "q":
      break
    else:
      test(countris)
  

  