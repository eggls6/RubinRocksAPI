.. _API

Rubin Rocks API
===============

Retrieve dynamical information of a near-Earth Object
-----------------------------------------------------

.. http:get:: /residencetime/
   :noindex:

   Retrieve dynamical information of a near-Earth Object

   :query a: (*required*) -- Semimajor axis [au]
   :query e: (*required*) -- Orbital eccentricity [0-1)
   :query i: (*required*) -- Inclination [deg] (< 180 deg)


**Example Request**
    .. tabs::

        .. tab:: Browser
            `http://apexgroup.web.illinois.edu/rubinrocks/residencetime/?a=2.5&e=0.6&i=45 <http://apexgroup.web.illinois.edu/rubinrocks/residencetime/?a=2.5&e=0.6&i=45>`_

        .. code-tab:: python

            import requests
            import json

            url = 'http://apexgroup.web.illinois.edu/rubinrocks/residencetime/;'
            params = {      'a': 2.5,
                            'e': 0.6,
                            'i': 45
                            }
            r = requests.get(url, params=params)
            print(json.dumps(r.json(), indent=4))

        .. code-tab:: bash

            curl -X GET "http://apexgroup.web.illinois.edu/rubinrocks/residencetime/?a=2.5&e=0.6&i=45" -H "accept: application/json"


**Example Response**

.. sourcecode:: json

    [
        {"author":"Rubin Rocks","data":[{"IMC":0.17557,"JFC":0.0,"MMR3to1":0.6331,"OMB":0.09221,"a":2.5,"cumulative_residence_time":0.8290172612,"e":0.6,"i":45.0,"nu6":0.09912,"residence_time":1.31163e-05}]}
    ]


Retrieve a slice of data from a near-Earth object model
-------------------------------------------------------

.. http:get:: /residencetimeslice/
    :noindex:

    Return gridpoints of a slice through the NEO model for a constant semimajor axis, eccentricity or inclination 

    :query a: (*required*) -- Semimajor axis [au]
    :query e: (*required*) -- Orbital eccentricity [0-1)
    :query i: (*required*) -- Inclination [deg] (< 180 deg)
    :query slicevariable: (*required*) -- Constant variable in a slice ("a","e","i") 
    :query output: (*required*) -- Orientation of JSON output (‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’)

**Example Request**
    .. tabs::
        .. tab:: Browser
            `https://apexgroup.web.illinois.edu/rubinrocks/residencetimeslice/?a=1.5&e=0.5&i=25&slicevariable=i&output=table <https://apexgroup.web.illinois.edu/rubinrocks/residencetimeslice/?a=1.5&e=0.5&i=25&slicevariable=i&output=table>`_

        .. code-tab:: python

            import requests
            import json

            url = 'https://apexgroup.web.illinois.edu/rubinrocks/residencetimeslice/'
              params = {    'a': 1.5,
                            'e': 0.5,
                            'i': 25,
                            'slicevariable': 'i',
                            'output': 'table
                            }
            r = requests.get(url, params=params)
            print(json.dumps(r.json(), indent=4))

        .. code-tab:: bash

            curl -X GET "https://apexgroup.web.illinois.edu/rubinrocks/residencetimeslice/?a=1.5&e=0.5&i=25&slicevariable=i&output=table" -H "accept: application/json"


**Example Response**

.. sourcecode:: json

    [{"schema":
        {"fields":
        [{"name":"index","type":"integer"},{"name":"a","type":"number"},
        {"name":"e","type":"number"},{"name":"i","type":"number"},
        {"name":"residence_time","type":"number"},
        {"name":"cumulative_residence_time","type":"number"},
        {"name":"nu6","type":"number"},
        {"name":"3:1","type":"number"},
        {"name":"IMC","type":"number"},
        {"name":"OMB","type":"number"},
        {"name":"JFC","type":"number"}],
        
        "primaryKey":["index"],"pandas_version":"1.4.0"},
        "data":[{"index":12,"a":0.025,"e":0.01,"i":25.0,"residence_time":0.0,"cumulative_residence_time":0.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0},
                {"index":102,"a":0.025,"e":0.03,"i":25.0,"residence_time":0.0,"cumulative_residence_time":0.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0},
                {"index":192,"a":0.025,"e":0.05,"i":25.0,"residence_time":0.0,"cumulative_residence_time":0.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0},
                {"index":282,"a":0.025,"e":0.07,"i":25.0,"residence_time":0.0,"cumulative_residence_time":0.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0},
                {"index":372,"a":0.025,"e":0.09,"i":25.0,"residence_time":0.0,"cumulative_residence_time":0.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0},
                {"index":462,"a":0.025,"e":0.11,"i":25.0,"residence_time":0.0,"cumulative_residence_time":0.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0}, ...
                
                {"index":367752,"a":4.075,"e":0.73,"i":25.0,"residence_time":0.0000052646,"cumulative_residence_time":0.9991299416,"nu6":0.00018,"3:1":0.00217,"IMC":0.00118,"OMB":0.0,"JFC":0.99647},
                {"index":367842,"a":4.075,"e":0.75,"i":25.0,"residence_time":0.0000041175,"cumulative_residence_time":0.9992140524,"nu6":0.00024,"3:1":0.00312,"IMC":0.00226,"OMB":0.0,"JFC":0.99438},
                {"index":367932,"a":4.075,"e":0.77,"i":25.0,"residence_time":0.0000027653,"cumulative_residence_time":0.9992802603,"nu6":0.00106,"3:1":0.00413,"IMC":0.0,"OMB":0.0,"JFC":0.99481},
                {"index":368022,"a":4.075,"e":0.79,"i":25.0,"residence_time":0.0000029515,"cumulative_residence_time":0.9993493882,"nu6":0.00033,"3:1":0.00048,"IMC":0.0021,"OMB":0.0,"JFC":0.99709},
                {"index":368112,"a":4.075,"e":0.81,"i":25.0,"residence_time":0.0000017369,"cumulative_residence_time":0.9993890165,"nu6":0.00028,"3:1":0.00164,"IMC":0.00357,"OMB":0.0,"JFC":0.99451},
                {"index":368202,"a":4.075,"e":0.83,"i":25.0,"residence_time":0.0000018089,"cumulative_residence_time":0.9994154603,"nu6":0.00485,"3:1":0.00316,"IMC":0.00171,"OMB":0.0,"JFC":0.99028},
                {"index":368292,"a":4.075,"e":0.85,"i":25.0,"residence_time":0.000000992,"cumulative_residence_time":0.9994387922,"nu6":0.00834,"3:1":0.00864,"IMC":0.01562,"OMB":0.0,"JFC":0.96739},
                {"index":368382,"a":4.075,"e":0.87,"i":25.0,"residence_time":0.0000007754,"cumulative_residence_time":0.9994527051,"nu6":0.00251,"3:1":0.00737,"IMC":0.0,"OMB":0.0,"JFC":0.99012},
                {"index":368472,"a":4.075,"e":0.89,"i":25.0,"residence_time":0.000001635,"cumulative_residence_time":0.999468282,"nu6":0.0003,"3:1":0.00437,"IMC":0.0,"OMB":0.1345,"JFC":0.86083}, ...

                {"index":377832,"a":4.175,"e":0.97,"i":25.0,"residence_time":0.0,"cumulative_residence_time":1.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0},
                {"index":377922,"a":4.175,"e":0.99,"i":25.0,"residence_time":0.0,"cumulative_residence_time":1.0,"nu6":0.0,"3:1":0.0,"IMC":0.0,"OMB":0.0,"JFC":0.0}] 
     }
    ]
