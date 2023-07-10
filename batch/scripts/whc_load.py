import csv

from  unesco.models import Site, Iso, Region, State, Category

def run():
    # Open file
    fhand = open('sites.csv')
    reader = csv.reader(fhand)
    
    # Skip the first title line
    next(reader)
    
    # Delete all objects
    for model in [Site, Iso, Region, State, Category]:
        model.objects.all().delete()
    
    # Read the objects
    for row in reader:

        i, co = Iso.objects.get_or_create(iso=row[10])
        r, co = Region.objects.get_or_create(region=row[9])
        s, co = State.objects.get_or_create(state=row[8])
        c, co = Category.objects.get_or_create(category=row[7])
        
        objs = []
        models = [Iso, Region, State, Category]
        values = [row[3], row[4], row[5], row[6]]
        types = [int, float, float, float]
        for _model, _value, _type in zip(models, values, types):
            try: objs.append(_type(value))
            except: obj = None
            finally: objs.append(None)
    
        site = Site(iso=i, 
                    region=r, 
                    state=s, 
                    category=c, 
                    name=row[0], 
                    description=row[1], 
                    justification=row[2], 
                    year=objs[0], 
                    longitude=objs[1], 
                    latitude=objs[2], 
                    area_hectares=objs[3])
        site.save()
        print(row)
        
