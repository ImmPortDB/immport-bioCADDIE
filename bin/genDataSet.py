#!/usr/bin/env python
"""Generate a DATS representation of a Study
"""


import sys
sys.path.append("../model")
import os
import logging
from argparse import ArgumentParser
import json
import decimal
import datetime
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from study import Study, StudySchema
import biocaddie

if __name__ == "__main__":
    parser = ArgumentParser(
             prog="genStudy",
             description="Generate a bioCADDIE DataSet.")

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


    #
    # Open connection to DB using SQLAlchemy
    #
    log.info("Connecting to the Database")
    engine = create_engine('mysql+mysqlconnector://USER:PASSWORD@HOST/DR22')
    Session = sessionmaker(bind=engine)
    session = Session()

    #
    # Retrieve study information using ORM
    #
    log.info("Retrieving study metadata")
    dataset = biocaddie.getStudyByAccession(session,args.study_accession)
    dataset.types = biocaddie.getDatasetTypes(dataset)
    dataset.creators = biocaddie.getDatasetCreators(dataset)
    dataset.primaryPublications = biocaddie.getPrimaryPublications(dataset)
    dataset.allExperiments = biocaddie.getExperiments(dataset)
    dataset.selectionCriteria = biocaddie.getSelectionCriteria(dataset)
    dataset.keywords = biocaddie.getKeywords(dataset)
    dataset.studyGroups = biocaddie.getStudyGroups(dataset)
    dataset.organizations = biocaddie.getDatasetOrganization(dataset)
    dataset.assessmentPanels = biocaddie.getAssessmentPanels(dataset)
    dataset.labTestPanels = biocaddie.getLabTestPanels(dataset)
    #
    # Construct dimensions from: experiments, labtest and assessments
    #
    dataset.dimensions = []
    for experiment in dataset.allExperiments:
        dataset.dimensions.append(experiment)
    for labTestPanel in dataset.labTestPanels:
        dataset.dimensions.append(labTestPanel)
    for assessmentPanel in dataset.assessmentPanels:
        dataset.dimensions.append(assessmentPanel)

    dataset.reagents = biocaddie.getReagents(session,args.study_accession)
    dataset.treatments = biocaddie.getTreatments(session,args.study_accession)

    #
    # Use Jinja2 templates to create a DATS instance
    #
    log.info("Generating DATS instance")
    env = Environment(loader=FileSystemLoader("../templates"))
    template = env.get_template("dataset_schema.template")
    context = {
        'dataset': dataset,
    }

    biocaddie.createDirectory("../output")
    dataset_json = template.render(**context)
    f = open("../output/Study_" + args.study_accession + ".json","w")
    f.write(dataset_json)
    f.write("\n")
    f.close()
    sys.exit(0)
