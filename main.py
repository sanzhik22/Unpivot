from dataflows import Flow, unpivot, load
import dataflows
f = Flow(load('data.csv'))
data, *_ = f.results()
print(data[0])

unpivoting_fields = [
    {'name': r'^A', 'keys':{'place': r'\1'}},
    {'name': r'(\d{4})', 'keys': {'year': r'\1'}}
]

extra_keys = [ {'name': 'year', 'type': 'string'}]
extra_value = {'name': 'value', 'type': 'integer'}


x = Flow(data[0], unpivot(unpivoting_fields, extra_keys, extra_value), dataflows.dump_to_path('unpivot_data.csv')).results()[0]
print(x)

