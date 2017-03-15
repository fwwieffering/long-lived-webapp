import requests
import argparse
import atexit

parser = argparse.ArgumentParser(description="Repeatedly curl url")
parser.add_argument('url', metavar='URL', type=str, help='url to query')

args = parser.parse_args()

codes = {}

@atexit.register
def exit_handler():
  print("Response summary:")
  print("Status Codes:")
  for code, count in codes.items():
    print("Status code: {} Count: {}".format(code, count))

while True:
  res = requests.get(args.url)
  if codes.get(res.status_code):
    codes[res.status_code] += 1
  else:
    codes[res.status_code] = 1
  print(res.status_code, res.content)