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

        i, co = Iso.objects.get_or_create(name=row[10])
        r, co = Region.objects.get_or_create(name=row[9])
        s, co = State.objects.get_or_create(name=row[8])
        c, co = Category.objects.get_or_create(name=row[7])
        
        # my_range = [0, 1, 2, 3]
        # objs = [0, 1, 2, 3,]    
        # values = [row[3], row[4], row[5], row[6]]
        # types = [int, float, float, float]
        # for j, _value, _type in zip(my_range, values, types):
        #     try: objs[j] = _type(value)
        #     except: obj = None
        #     finally: objs[j] = None

        try: year = int(row[3])
        except: row[3] = None
        
        try: longitude = float(row[4])
        except: row[4] = None
        
        try: latitude = float(row[5])
        except: row[5] = None
        
        try: area_hectares = float(row[6])
        except: row[6] = None
        
    
        site = Site(iso=i, 
                    region=r, 
                    state=s, 
                    category=c, 
                    name=row[0],
                    description=row[1], 
                    justification=row[2], 
                    year=year, 
                    longitude=longitude, 
                    latitude=latitude, 
                    area_hectares=area_hectares)
        site.save()
        print(row)
        
