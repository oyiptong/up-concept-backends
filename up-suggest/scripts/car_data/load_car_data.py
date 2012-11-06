#!/usr/bin/env python
import time
import re
import json

import pymongo

path_pattern = re.compile(r'[^A-Za-z0-9\./_-]+')

def get_model_types(car_rules_filename):
    model_types = {}
    with open(car_rules_filename, 'r') as car_rules:
        data = json.load(car_rules)

        for category,meta in data.iteritems():
            keywords = meta['keywords'].split(',')
            for keyword in keywords:
                keyword = path_pattern.sub('_', keyword)
                if model_types.has_key(keyword):
                    model_types[keyword].add(category)
                else:
                    model_types[keyword] = set([category])
    return model_types

def get_car_models(car_image_filename, model_types):
    car_objs = {}
    with open(car_image_filename, 'r') as car_data:
        for line in car_data:
            path = line[2:].strip()
            path = path_pattern.sub('_', path)

            make, model, image_filename = path.split('/')
            model_name = model[len(make)+1:]
            car_objs[model] = {"tags": set([make, model_name, 'automobile']), "image_path": path}
            
            if model_types.has_key(make):
                for tag in model_types[make]:
                    car_objs[model]['tags'].add(tag)

            if model_types.has_key(model):
                for tag in model_types[model]:
                    car_objs[model]['tags'].add(tag)

            if model_types.has_key(model_name):
                for tag in model_types[model_name]:
                    car_objs[model]['tags'].add(tag)
    return car_objs

def main():
    start = time.time()

    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-U", "--username", dest="username", help="mongodb username", type="string")
    parser.add_option("-P", "--password", dest="password", help="mongodb password", type="string")
    parser.add_option("-H", "--hostname", dest="hostname", help="mongodb hostname", type="string", default="localhost")
    parser.add_option("-D", "--database", dest="database", help="mongodb database", type="string", default="up_suggest")
    parser.add_option("-p", "--port", dest="port", help="mongodb port", type="int", default=27017)
    parser.add_option("-c", "--clean", dest="clean", help="purge collection before saving", action="store_true", default=False)
    (options, args) = parser.parse_args()

    model_types = get_model_types('car_rules_english.json')
    car_objects = get_car_models('carimagefiles.txt', model_types)

    if options.username and options.password:
        credentials = "{0}:{1}@".format(options.username, options.password)
    else:
        credentials = ""

    mongo_url = "mongodb://{0}{1}:{2}/{3}".format(credentials, options.hostname, options.port, options.database)

    conn = pymongo.Connection(mongo_url)
    db = conn[options.database]

    cars = db['car']

    if options.clean:
        print "purging collection"
        cars.remove({}, safe=True)

    cars.ensure_index('model', unique=True)
    cars.ensure_index('tags')

    objs_saved = 0
    for model, meta in car_objects.iteritems():
        car = {
                'model': model,
                'tags': list(meta['tags']),
                'image_path': meta['image_path']
        }
        cars.update({'model': model}, car, True, safe=True)
        objs_saved += 1

    finish = time.time()
    print "Persisted {0} objects in {1:0.2f} secs".format(objs_saved, finish-start)

if __name__ == '__main__':
    main()
