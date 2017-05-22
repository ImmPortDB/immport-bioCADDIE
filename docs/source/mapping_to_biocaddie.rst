*************************
Mapping to bioCADDIE
*************************

As mentioned in the overview, we debated whether to map a Study or Experiment
to the DATS DataSet. In ImmPort a Study represents the central focus of
a research project. When studies are added to the ImmPort repository they are
first marked a "private" and not available for sharing. Studies remain private
until the researcher or NIH approves their release as a public study. When studies
are in the private stage, the ImmPort data curation teams works closely with the
study provider to insure the data in ImmPort reflects the intent of the
research. A Study can have multiple experiments, but contains information that
is shared across the experiments. The types of data include arms, subjects,
biosamples, organization information, etc. For these reasons we decided to
map a Study to a DATS DataSet. An overview of the ImmPort Study model is
here :doc:`study_erd` and online at
`ER Diagrams <http://www.immport.org/immport-open/public/schema/schemaDiagram/AllTables>`_

Based on what we heard at the recent bioCADDIE meeting, we will probably
rethink how we mapped information to the DATS Dimension. Currently we
mapped 3 different types of information to the DATS Dimension. The information
mapped is the experiment.purpose, lab_test_panel.name and
assessment_panel.name. experiment.purpose was recently removed from the model
so we will use the experiment.measurement_technique in the future. Both
lab_test_panel and and assessment_panel are containers for more detailed
information contained in lab_test and assessment_component, so in the future
we may want to include information from the more detailed tables. If we do
this for many studies this would greatly increase the number of Dimensions
in a DataSet. A small example of the data from the ImmPort tables are below.

Experiment - measurement_technique
----------------------------------
+------------------------------+
| ELISA                        |
+------------------------------+
| ELISPOT                      |
+------------------------------+
| Flow Cytometry               |
+------------------------------+
| Mass Spectrometry            |
+------------------------------+
| PCR                          |
+------------------------------+

Lab_test_panel - name
----------------------
+------------------------------+
| Chemistry Test               |
+------------------------------+
| Blood Cell Count             |
+------------------------------+
| Urinalysis                   |
+------------------------------+

Assessment_panel - name
-----------------------
+------------------------------+
| Medical History              |
+------------------------------+
| Family History               |
+------------------------------+
| Atopic Dermatitis Assessment |
+------------------------------+

Lab_test - name
---------------------------
+------------------------------+
| WBC                          |
+------------------------------+
| PLATELET COUNT               |
+------------------------------+
| IgG Total                    |
+------------------------------+

Assessment_component - name
---------------------------
+------------------------------+
| Sneezing Severity Score      |
+------------------------------+
| Body Mass Index              |
+------------------------------+
| Systolic Blood Pressure      |
+------------------------------+

Field By Field Mapping
------------------------------
For detailed information on how the DATS properties were extracted and written
to the Jinja2 templates representing the DATS schema, you need review the
code and the Jinja2 templates.

A simple example will be used to illustrate the process. For this example
the DataSet.creators portion of the schema will be used. In our case, we
decided in the DataSet.creators we would be filling in the Person_schema
with information from the study_personnel table and the Organization_schema
with information from the contract and program tables. We used these steps
to fill in the person_schema

1. Create a Jinja2 template representing the Person_schema instance.
2. Extract the information from the study_personnel table
3. The extracted information was transformed into a Python object
   representing the properties in the Person_schema. The Python methods used
   are below.
4. The extracted information representing the person_schema objects are used as
   input to the Jinja2 templating system, generating a DATS Person_schema
   instance for each DataSet.creators.

A similar process was used to fill out the organization_schema, but the
contract and program tables were used as the sources for the instances.

DataSet creators
----------------

::

  "creators" : {
      "description": "The person(s) or organization(s) which contributed to the creation of the dataset.",
      "type" : "array",
      "items" : {
          "oneOf": [
              {"$ref" : "person_schema.json#"},
              {"$ref" : "organization_schema.json#"}
          ]
      },
      "minItems" : 1
  },

Person_schema
----------------

::

  {
    "$schema": "http://json-schema.org/draft-04/schema",
    "title": "DATS person schema",
    "description": "A human being",
    "type": "object",
    "properties": {
      "@context": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "object"
          }
        ]
      },
      "@type": { "type": "string", "enum": [ "Person" ]},
      "identifier": {
        "$ref": "identifier_info_schema.json#"
      },
      "alternateIdentifiers": {
        "description": "Alternate identifiers for the person.",
        "type": "array",
        "items": {
          "$ref": "alternate_identifier_info_schema.json#"
        }
      },
      "relatedIdentifiers": {
        "description": "Related identifiers for the person.",
        "type": "array",
        "items": {
          "$ref": "related_identifier_info_schema.json#"
        }
      },
      "fullName": {
        "description": "The first name, any middle names, and surname of a person.",
        "type" :  "string"
      },
      "firstName": {
        "description": "The given name of the person.",
        "type" :  "string"
      },
      "middleInitial": {
        "description": "The first letter of the person's middle name.",
        "type" :  "string"
      },
      "lastName": {
        "description": "The person's family name.",
        "type" :  "string"
      },
      "email": {
        "description": "An electronic mail address for the person.",
        "type" :  "string",
        "format": "email"
      },
      "affiliations" : {
        "description": "The organizations to which the person is associated with.",
        "type" : "array",
        "items" : {
          "$ref" : "organization_schema.json#"
        }
      },
      "roles" : {
        "description": "The roles assumed by a person, ideally from a controlled vocabulary/ontology.",
        "type" : "array",
        "items" : {
          "$ref" : "annotation_schema.json#"
        }
      },
      "extraProperties": {
        "description": "Extra properties that do not fit in the previous specified attributes. ",
        "type": "array",
        "items": {
          "$ref" : "category_values_pair_schema.json#"
        }
      }
    },
    "additionalProperties": false
  }

Jinja2 Template - Person Instance
---------------------------------

::

  {%- for creator in dataset.creators %}
  {
    "firstName": "{{ creator.firstName }}",
    "lastName": "{{ creator.lastName }}",
    "email": "{{ creator.email }}",
    "affiliations": [
        {
           "name": "{{ creator.affiliation }}"
        }
    ],
    "roles": [
        {
           "value": "{{ creator.role }}"
        }
    ]
  {% if loop.last -%}
  }
  {%- else -%}
  },
  {%- endif -%}
  {%- endfor -%}

Method to retrieve Study personnel
----------------------------------

::

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


Method to create Person object
----------------------------------

::

  def getDatasetCreators(study):
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


Sample Output
----------------------------------

::

  "creators": [
    {
      "firstName": "Thomas",
      "lastName": "Casale",
      "email": "tbcasale@creighton.edu",
      "affiliations": [
          {
             "name": "Creighton University School of Medicine"
          }
      ],
      "roles": [
        {
           "value": "Principal Investigator"
        }
      ]
    },
    {
      "name": "Immune Tolerance Network - Casale",
      "extraProperties": [
        {
          "category": "Catgory",
          "values": [
            {
              "value": "NIH"
            }
          ]
        },
        {
          "category": "External Id",
          "values": [
            {
              "value": "N01-AI-95380 - Casale"
            }
          ]
        },
        {
          "category": "Description",
          "values": [
            {
              "value": "The Collaborative Network for Clinical Research on Immune Tolerance is a consortium of scientific and clinical investigators to: (1) develop a long-term scientific agenda for clinical trials and mechanistic studies; (2) design and conduct clinical trials at all phases to determine the safety, toxicity and efficacy of tolerogenic treatment strategies for multiple immune system diseases; and (3) design and conduct research to delineate the underlying mechanisms of immune tolerance as an integral part of the clinical trials undertaken by the Collaborative Network, as well as clinical trials sponsored by other Federal and private sector organizations and companies.  http://projectreporter.nih.gov/project_info_details.cfm?aid=6358320&icde=23811074&ddparam=&ddvalue=&ddsub=&cr=1&csb=default&cs=ASC"
            }
          ]
        }
      ]
    }
  ],
