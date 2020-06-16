#!/usr/bin/python
from jinja2 import Template
import yaml
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog='j2generator', 
                                  description='Build output file using jinja2 template', 
                                  usage='%(prog)s config_file j2_template_file output_file')

  parser.add_argument('config_file', help='File with paraneters for j2 template')
  parser.add_argument('j2_template_file', help='Jinja2 template file')
  parser.add_argument('output_file', help='Templated file')
  args = parser.parse_args()

  with open(args.config_file) as cfg_file:
    config =  yaml.load(cfg_file, Loader=yaml.FullLoader)

  with open(args.j2_template_file) as file_:
    template = Template(file_.read())
  
  with open(args.output_file, 'w') as file_:
    file_.write(template.render(config))