Publication Schema
======================

::

  {%- for publication in dataset.primaryPublications %}
  {
    "identifier":
      {
        "identifier": "{{ publication.pubmed }}",
        "identifierSource": "pubmed"
      },
    "authorsList": "{{ publication.authorsList }}",
    "title": "{{ publication.title }}",
    "publicationVenue": "{{ publication.publicationVenue }}",
    "dates": [
      {
        "date": "{{ publication.publicationDate }}",
        "type": { "value": "publication year" }
      }
    ]
  {% if loop.last -%}
  }
  {%- else -%}
  },
  {%- endif -%}
  {%- endfor -%}
