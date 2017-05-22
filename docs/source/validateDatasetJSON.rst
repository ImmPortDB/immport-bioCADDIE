validateDataSetJSON.py
----------------------

::

  #!/usr/bin/env python
  """Validate the DataSet json output is correct.
  """


  import sys
  import os
  from os.path import isfile, join
  import logging
  from argparse import ArgumentParser
  import json
  from jsonschema import RefResolver, Draft4Validator

  if __name__ == "__main__":
      parser = ArgumentParser(
               prog="validateDatasetJSON",
               description="Validate the JSON output for a dataset is correct.")

      parser.add_argument(
          '--study_accession',
          dest="study_accession",
          required=True,
          help="Specify study_accession"
      )

      parser.add_argument(
          '--log',
          dest="loglevel",
          default="DEBUG",
          required=False,
          help="Specify the log level: DEBUG, INFO, WARNING, ERROR, CRITICAL"
      )

      args = parser.parse_args()

      #
      # Setup Logging
      #
      logging.basicConfig(format='%(levelname)s:%(module)s:%(message)s',
                          level=args.loglevel)
      log = logging.getLogger(__name__)

      DATS_schemasPath = os.path.join(os.path.dirname(__file__),"../json-schemas/")
      DATS_contextsPath = os.path.join(os.path.dirname(__file__),"../json-schemas/contexts/")

      print("Starting  Validation")
      dataset_schema_file = open(join(DATS_schemasPath,"dataset_schema.json"),"r")
      dataset_schema = json.load(dataset_schema_file)
      resolver = RefResolver('file:///Users/jcampbell/git/immport-tools/bioCADDIE/json-schemas/', dataset_schema)
      validator = Draft4Validator(dataset_schema, resolver=resolver)
      dataset_file = open("../output/Study_" + args.study_accession + ".json","r")
      instance = json.load(dataset_file)
      validator.validate(instance,dataset_schema)
      print("Finished Validation")

      sys.exit(0)
