import csv
import sys

def main():
  if sys.argv[1][-4:]!=".csv":
    sys.exit("Not a csv File")
  if len(sys.argv)<3:
    sys.exit("Too few command-line argument")
  elif len(sys.argv)>3:
    sys.exit("Too many command-line argument")
  try:
    with open(sys.argv[1]) as before,open(sys.argv[2],'w') as after:
      reader=csv.DictReader(before)
      fieldname=['first','last','house']
      writer=csv.DictWriter(after,fieldnames=fieldname)
      writer.writeheader()
      for row in reader:
        last,first=row['name'].split(',')
        house=row['house']
        writer.writerow({"first":first,"last":last,"house":house})
      
  except FileNotFoundError:
    sys.exit("File doesnt exist:(")
if __name__=="__main__":
  main()