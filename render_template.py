from jinja2 import Template
import yaml

with open("ios-bgp.j2") as temp_file:
    t = Template(temp_file.read())

vars = open('bgp_neighbors.yaml')

yaml_vars = yaml.safe_load(vars)

output = t.render(yaml_vars)

with open('bgp_netconf.xml','w+') as bgp_netconf:
    bgp_netconf.write(output)