from dataflows import Flow, unpivot, add_metadata, dump_to_path, load, set_type, printer, validate,PackageWrapper
import dataflows

unpivoting_fields = [
    {'name': r'^A', 'keys':{'place': r'\1'}},
    {'name': r'(\d{4})', 'keys': {'year': r'\1'}}
]


extra_keys = [ {'name': 'year', 'type': 'string'}]
extra_value = {'name': 'value', 'type': 'integer'}

f = Flow(
add_metadata(
        name="Sanzhar's data",
        title="Pivot unpivot",
        descriptor=(
            "Demo data package which makes project look great "
        ),
        sources=[
            {
                "name": "Sanzhar's Data",
                "path": "https://github.com/sanzhik22",
                "title": "Unpivoting data",
            },
        ],
        licenses=[
            {
                "name": "ODC-PDDL-1.0",
                "path": "https://github.com/sanzhik22",
                "title": "Sanzhar's data v1.0",
            }
        ],
    ),
    load('data.csv'), unpivot(unpivoting_fields, extra_keys, extra_value),
    validate(),
    printer(),
    dump_to_path('data')
)

if __name__ == "__main__":
    f.process()