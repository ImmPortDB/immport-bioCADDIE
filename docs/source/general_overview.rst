*************************
General Overview
*************************

1. Reviewed the DATS Specification

   * Used the bioCADDIE GitHub `repository <https://github.com/biocaddie/WG3-MetadataSpecifications>`_.

     - json_schemas: for building templates in Python Jinja2
     - json-instances: helpful to see how other repositories were mapped to DATS
     - tests: code to illustrate schema validation was very helpful

   * DATS Specification v2.2

     - Diagrams
     - Appendix I and II

   * Preprint Overview Paper

     - `Preprint <http://biorxiv.org/content/early/2017/01/25/103143>`_

   * Videos - Presentations

     - bioCADDIE special webinar 06-01-16 `YouTube <https://www.youtube.com/watch?v=mMDELhHuQMs&feature=youtu.b>`_
     - bioCADDIE Workshop: Data Indexing for Data Providers - June 23, 2016 `YouTube <https://www.youtube.com/watch?v=RNmGXEkFlPc>`_

       - Sound quality is poor. Philippe's sections were the most helpful.

2. Compared ImmPort data model to the DATS specification.
   In the ImmPort data model the study is the primary object in the model and
   experiments are linked to a study. A study may have multiple experiments, the
   number of experiments linked to a study ranges between 1 and 192.
   For an overview see :doc:`immport_model_overview` or to view online
   `Open ImmPort <http://www.immport.org/immport-open/public/schema/schemaTree>`_
   We decided for now to map an ImmPort Study to a DATS DataSet, an other option
   would be to map an ImmPort Experiment to a DATS DataSet. Most of the metadata
   in Immport, like arms, publications, personel, subjects, clinical data, etc.
   is linked to the study, so if we had chosen to use Experiment as a DATS
   DataSet, we would have too much redundancy of information being exported
   to DATS.

3. Based on the decision to map an ImmPort Study to a DATS DataSet, we went
   through the exercise of mapping the ImmPort model to the DATS model.

4. Developed an ORM model using Python SQLAlchemy over the MySQL relational
   database. Using an ORM model was not really necessary, but we have done this
   in the past for other projects, we could have accomplished the same thing
   using SQL queries directly. The ORM does not reflect all the relationships
   in the relational model, we only included what was necessary to satisfy the
   mapping to DATS. A biocaddie.py package was created as a service layer over
   the ORM.
   For example model class see :doc:`study_pubmed`
   The ImmPort shared data models is available online in multiple formats:
   `ER Diagrams <http://www.immport.org/immport-open/public/schema/schemaDiagram/AllTables>`_
   and
   `Tabular Format <http://www.immport.org/immport-open/public/schema/schemaDefinition/study>`_

5. Jinja2 templates were created that map to the DATS JSON schemas. In the other
   projects we have found it useful to develop these boiler plate templates,
   rather than using print statements, etc. in the Python code. By separating
   the concerns of extraction from ImmPort model from generating DATS, it
   reduces software complexity when either the ImmPort model or the DATS
   specification changes in the future.
   For example Jinja2 template see :doc:`publication_schema`

6. Wrote a program (genStudy.py) that uses the ORM layer, biocaddie.py package
   and the Jinja2 templates to extract one study at a time to generate a DATS
   instance for that study. There is a BASH shell script to run the genStudy.py
   program for a list of studies. Example code :doc:`genDataSet`

7. Based on code available in the bioCADDIE GitHub repository, wrote a program
   to validate the JSON generated for each study against the DATS schema
   specification. Example code :doc:`validateDatasetJSON`
