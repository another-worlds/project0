import csv
from cats.models import Cat, Breed

# Function of script
def run():
    fhand = open('meow.csv')
    reader = csv.reader(fhand)
    reader.__next__()
    
    
    Breed.objects.all().delete()
    Cat.objects.all().delete()
    
    for row in reader:
        b, created = Breed.objects.get_or_create(name=row[1])
        c = Cat(nickname=row[0], breed=b, weight=row[2])
        c.save()
        print(c)