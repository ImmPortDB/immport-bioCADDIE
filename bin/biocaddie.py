import sys
import os
import logging
import re
import json
sys.path.append("../model")
log = logging.getLogger(__name__)

from study import Study
from study_categorization import StudyCategorization
from study_personnel import StudyPersonnel
from study_pubmed import StudyPubmed
from study_glossary import StudyGlossary
from arm_or_cohort import ArmOrCohort
from arm_2_subject import Arm2Subject
from assessment_panel import AssessmentPanel
from contract_grant import ContractGrant
from inclusion_exclusion import InclusionExclusion
from lab_test_panel import LabTestPanel
from experiment import Experiment
from program import Program
from subject import Subject
from workspace import Workspace

# Global Regular Expression
cleanStringRegEx = re.compile("\n|\r")

def cleanString(s):
    """Remove carriage return and line feeds from a string.
       Also replace single " with '

    :param str s: string
    :returns str s: string
    """

    try:
        if s is None:
            return ''
        elif type(s) is str:
            s = cleanStringRegEx.sub(" ",s)
            return s.replace('"',"'")
        else:
            return s
    except:
        return ""

def createDirectory(directory):
    '''Create a new directory if it does not already exist.

    :param str directory: Name of directory
    :returns: True or False
    '''
    try:
        os.makedirs(directory)
    except OSError as e:
        if os.path.exists(directory):
            pass
        else:
            return False

    return True


def getStudyByAccession(session, study_accession):
    '''Query for a Study using the study_accession.
       Return Study

    :param session: SQLAlchemy session
    :param string: study_accession
    :returns study: Study
    '''

    study = session.query(Study) \
                   .filter_by(study_accession=study_accession) \
                   .first()

    return study

def getStudyPersonnelByAccession(session, study_accession):
    '''Query for a StudyPersonnel using the study_accession.
       Return array of StudyPersonnel

    :param session: SQLAlchemy session
    :param string: study_accession
    :returns personnel: StudyPersonnel
    '''

    personnel = session.query(StudyPersonnel) \
                   .filter_by(study_accession=study_accession) \
                   .all()

    return personnel

def getDatasetTypes(study):
    '''Merge information from categories and if study is clinical trial
       into DataSet types

    :param Study: study
    '''

    types = []
    if study.clinical_trial == 'Y':
        types.append("Clinical Trial")
    types.append(study.type)
    categories = study.categorizations
    for category in categories:
        types.append(category.research_focus)
    return types

def getDatasetCreators(study):
    '''Process the study personnel into creators

    :param Study: study
    '''

    creators = []
    persons = study.personnel
    for person in persons:
        obj = {}
        obj['lastName'] = person.last_name
        obj['firstName'] = person.first_name
        obj['email'] = person.email
        obj['affiliation'] = person.organization
        obj['role'] = person.role_in_study
        creators.append(obj)
    return creators

def getPrimaryPublications(study):
    '''Process the pubmed information into publications

    :param Study: study
    '''

    publications = []
    for publication in study.publications:
        obj = {}
        obj['authorsList'] = publication.authors
        obj['title'] = publication.title
        obj['pubmed'] = publication.pubmed_id
        obj['publicationVenue'] = publication.journal
        obj['publicationDate'] = publication.year
        publications.append(obj)

    return publications

def getExperiments(study):
    '''Process the study experiments into experiments

    :param Study: study
    '''

    experiments = []
    for experiment in study.experiments:
        obj = {}
        obj['name'] = experiment.measurement_technique
        obj['description'] = experiment.description
        obj['type'] = experiment.measurement_technique
        obj['obj_type'] = "experiment"
        experiments.append(obj)

    return experiments

def getSelectionCriteria(study):
    '''Process the inclusion/exclusion information into selectionCriteria

    :param Study: study
    '''

    selectionCriteria = []
    for criteria in study.inclusion_exclusions:
        obj = {}
        obj['criterion'] = criteria.criterion
        obj['category'] = criteria.criterion_category
        selectionCriteria.append(obj)

    return selectionCriteria

def getKeywords(study):
    '''Process the glossary into keywords

    :param Study: study
    '''

    keywords = []
    for keyword in study.glossaries:
        obj = {}
        obj['term'] = keyword.term
        # The replace is temporary until the data is fixed.
        obj['defintion'] = keyword.definition.replace("\r","")
        keywords.append(obj)

    return keywords

def getStudyGroups(study):
    '''Process the arm_or_cohort information into studyGroups

    :param Study: study
    '''

    studyGroups = []
    for group in study.arms:
        obj = {}
        obj['name'] = group.name
        obj['description'] = group.description
        obj['size'] = len(group.subjects)
        studyGroups.append(obj)

    return studyGroups

def getDatasetOrganization(study):
    '''Process the contract and program information into organization

    :param Study: study
    '''

    contracts = []
    for contract in study.contracts:
        obj = {}
        obj['name'] = contract.name.replace("\t","")
        obj['category'] = contract.category
        obj['description'] = contract.description.replace("\r","").replace("\n"," ").replace('"',"'")
        obj['external_id'] = contract.external_id
        obj['link'] = contract.link
        program = contract.program
        obj['program'] = {}
        obj['program']['category'] = program.category
        obj['program']['descripition'] = program.description.replace("\r"," ").replace("\n"," ").replace('"',"'")
        obj['program']['name'] = program.name
        contracts.append(obj)

    return contracts

def getAssessmentPanels(study):
    '''Process the assessement_panel

    :param Study: study
    '''

    assessment_panels = []
    panel_names = {}
    for panel in study.assessment_panels:
        if panel.name_reported not in panel_names:
            obj = {}
            obj['name'] = panel.name_reported
            obj['type'] = panel.assessment_type
            obj['obj_type'] = "assessmentPanel"
            panel_names[panel.name_reported] = 1
            assessment_panels.append(obj)

    return assessment_panels

def getLabTestPanels(study):
    '''Process the lab_test_panel

    :param Study: study
    '''

    lab_test_panels = []
    panel_names = {}
    for panel in study.lab_test_panels:
        if panel.name_reported not in panel_names:
            obj = {}
            obj['name'] = panel.name_reported
            obj['obj_type'] = "labTestPanel"
            panel_names[panel.name_reported] = 1
            lab_test_panels.append(obj)

    return lab_test_panels

def getReagents(session,study_accession):
    '''Retrieve reagent information from database

    :param session: SQLAlchemy session
    :param string: study_accession
    :returns reagents
    '''

    reagents = []
    sql = """
          SELECT distinct r1.name, r1.reporter_name
          FROM   reagent r1,
                 expsample_2_reagent e1,
                 expsample e2,
                 experiment e3
          WHERE  r1.reagent_accession = e1.reagent_accession
            AND  e1.expsample_accession = e2.expsample_accession
            AND  e2.experiment_accession = e3.experiment_accession
            AND  e3.study_accession = :study_accession
          """
    result = session.execute(sql,{'study_accession':study_accession})
    for row in result.fetchall():
        obj = {}
        obj['name'] = row[0]
        obj['reporter_name'] = row[0]
        reagents.append(obj)

    return reagents

def getTreatments(session,study_accession):
    '''Retrieve treatment information from database

    :param session: SQLAlchemy session
    :param string: study_accession
    :returns treatments
    '''

    treatments = []
    sql = """
          SELECT distinct t1.name
          FROM   treatment t1,
                 expsample_2_treatment e1,
                 expsample e2,
                 experiment e3
          WHERE  t1.treatment_accession = e1.treatment_accession
            AND  e1.expsample_accession = e2.expsample_accession
            AND  e2.experiment_accession = e3.experiment_accession
            AND  e3.study_accession = :study_accession
          """
    result = session.execute(sql,{'study_accession':study_accession})
    for row in result.fetchall():
        obj = {}
        obj['name'] = row[0]
        treatments.append(obj)

    return treatments
