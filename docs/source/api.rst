.. api

Rubin Rocks API
===============
This page contains a list of various Rubin Rocks API endpoints that can be used to extract dynamical information for near-Earth objects.
The API endpoints simply follow the main URL `http://apexgroup.web.illinois.edu/rubinrocks2 <http://apexgroup.web.illinois.edu/rubinrocks2>`_ .

Retrieve dynamical information of a near-Earth Object
-----------------------------------------------------

.. http:get:: /source_regions_from_id/
   :noindex:

   Retrieve dynamical information of a near-Earth Object by Designation

   :query designation: (*required*) -- designation of object (as defined in NASA SBDB)

**Example Request**
    .. tab-set::

        .. tab-item:: Browser

            `http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_from_id/?designation=2026%20AB1 <http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_from_id/?designation=2026%20AB1>`_

        .. tab-item:: Python

            .. code-block:: python

                import requests
                import json

                url = 'http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_from_id/;'
                params = {      'designation': '2026 AB1'
                                }
                r = requests.get(url, params=params)
                print(json.dumps(r.json(), indent=4))

        .. tab-item:: Bash

            .. code-block:: bash

                curl -X GET "http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_from_id/?designation=2026%20AB1" -H "accept: application/json"


**Example Response**

.. code-block:: json

    [
       {"author":"Rubin Rocks",
        "data":{
            "cov":{
                "labels":["a","e","i","residence_time","cumulative_residence_time","nu6","MMR3to1","IMC","OMB","JFC"],
                "values":[[1.2212e-06,6.66e-07,3.55118e-05,-2e-10,-3.155e-07,1.2896e-06,2.085e-07,-1.4982e-06,0.0,0.0],
                        [6.66e-07,3.633e-07,1.93682e-05,-1e-10,-1.727e-07,7.05e-07,1.148e-07,-8.199e-07,0.0,0.0],
                        [3.55118e-05,1.93682e-05,0.0010327029, -6.8e-09,-9.1763e-06,3.75065e-05,6.0661e-06,-4.35745e-05,0.0,0.0],
                        [-2e-10,-1e-10,-6.8e-09,0.0,4e-10,-1.1e-09,-6e-10,1.7e-09,0.0,0.0],
                        [-3.155e-07,-1.727e-07,-9.1763e-06,4e-10,7.375e-07,-2.0483e-06,-1.1664e-06,3.2149e-06,0.0,0.0],
                        [1.2896e-06,7.05e-07,3.75065e-05,-1.1e-09,-2.0483e-06,5.8476e-06,3.1281e-06,-8.9761e-06,0.0,0.0],
                        [2.085e-07,1.148e-07,6.0661e-06,-6e-10,-1.1664e-06,3.1281e-06,1.9228e-06,-5.0512e-06,0.0,0.0],
                        [-1.4982e-06,-8.199e-07,-4.35745e-05,1.7e-09,3.2149e-06,-8.9761e-06,-5.0512e-06,1.40279e-05,0.0,0.0],
                        [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]},
            "mean":{"IMC":0.450373535,"JFC":0.0,"MMR3to1":0.0635422085,"OMB":0.0,"a":1.31,"cumulative_residence_time":0.1667425156,"e":0.25,"i":22.56,"nu6":0.4860816453,"residence_time":2.92058e-05},
            "sigma":{"IMC":0.0037453879,"JFC":0.0,"MMR3to1":0.0013866676,"OMB":0.0,"a":0.0011050629,"cumulative_residence_time":0.0008588068, "e":0.000602712,"i":0.0321356953,"nu6":0.0024181819,"residence_time":4.471e-07},
            "units":{"IMC":"","JFC":"","MMR3to1":"","OMB":"","a":"au","cumulative_residence_time":"","e":"","i":"deg","nu6":"","residence_time":""}},
            "object":{"des":"2026 AB1","fullname":"(2026 AB1)","kind":"au","neo":true,"orbit_class":{"code":"APO","name":"Apollo"},"orbit_id":"6","pha":false,"prefix":null,"spkid":"54575232"},
            "orbit":{"comment":null,"condition_code":"8","covariance":{"data":[["5.017398019079587E-7","3.077682146129497E-8","2.855629239880995E-5","4.865930507002469E-7","2.549381095447013E-5","2.673632592132924E-5"],["3.077682146129497E-8","1.907324220499756E-9","1.755008063448325E-6","2.960021854076751E-8","1.568758073555719E-6","1.640799670709472E-6"],["2.855629239880995E-5","1.755008063448325E-6",".00162586163739686","2.765224715214904E-5",".001451837099941707",".001521813097641808"],["4.865930507002469E-7","2.960021854076751E-8","2.765224715214904E-5","4.754466649009584E-7","2.466142733365025E-5","2.591958302107099E-5"],["2.549381095447013E-5","1.568758073555719E-6",".001451837099941707","2.466142733365025E-5",".0012966376023672",".001358686960196477"],["2.673632592132924E-5","1.640799670709472E-6",".001521813097641808","2.591958302107099E-5",".001358686960196477",".001424744885074608"]],"epoch":"2461056.5","labels":["e","q","tp","node","peri","i"]},"data_arc":"15","elements":[{"label":"e","name":"e","sigma":".00070834","title":"eccentricity","units":null,"value":".2541511801421507"},{"label":"a","name":"a","sigma":".0012985","title":"semi-major axis","units":"au","value":"1.305890611769641"},{"label":"q","name":"q","sigma":"4.3673E-5","title":"perihelion distance","units":"au","value":".9739969716518319"},{"label":"i","name":"i","sigma":".037746","title":"inclination; angle with respect to x-y ecliptic plane","units":"deg","value":"22.55876193656924"},{"label":"node","name":"om","sigma":".00068953","title":"longitude of the ascending node","units":"deg","value":"286.5618122288996"},{"label":"peri","name":"w","sigma":".036009","title":"argument of perihelion","units":"deg","value":"135.5576458019445"},{"label":"M","name":"ma","sigma":".075318","title":"mean anomaly","units":"deg","value":"32.64478206793237"},{"label":"tp","name":"tp","sigma":".040322","title":"time of perihelion passage","units":"TDB","value":"2461007.072357222534"},{"label":"period","name":"per","sigma":".81298","title":"sidereal orbital period","units":"d","value":"545.0779656871141"},{"label":"n","name":"n","sigma":".00098506","title":"mean motion","units":"deg/d","value":".660455976322931"},{"label":"Q","name":"ad","sigma":".0016285","title":"aphelion distance","units":"au","value":"1.637784251887451"}],"epoch":"2461056.5","equinox":"J2000","first_obs":"2026-01-10","last_obs":"2026-01-25","model_pars":[],"moid":".0471142","moid_jup":"3.67442","n_del_obs_used":null,"n_dop_obs_used":null,"n_obs_used":36,"not_valid_after":null,"not_valid_before":null,"orbit_id":"6","pe_used":"DE441","producer":"Otto Matic","rms":".46653","sb_used":"SB441-N16","soln_date":"2026-03-02 05:20:06","source":"JPL","t_jup":"4.879","two_body":null}}
    ]


Retrieve dynamical information of a near-Earth Object by Orbit 
--------------------------------------------------------------

.. http:get:: /source_regions/
   :noindex:

   Retrieve dynamical information of a near-Earth Object

   :query a: (*required*) -- Semimajor axis [au]
   :query e: (*required*) -- Orbital eccentricity [0-1)
   :query i: (*required*) -- Inclination [deg] (< 180 deg)


**Example Request**
    .. tab-set::

        .. tab-item:: Browser

            `http://apexgroup.web.illinois.edu/rubinrocks2/source_regions/?a=2.5&e=0.6&i=45 <http://apexgroup.web.illinois.edu/rubinrocks2/source_regions/?a=2.5&e=0.6&i=45>`_

        .. tab-item:: Python

            .. code-block:: python

                import requests
                import json

                url = 'http://apexgroup.web.illinois.edu/rubinrocks2/source_regions/;'
                params = {      'a': 2.5,
                                'e': 0.6,
                                'i': 45
                                }
                r = requests.get(url, params=params)
                print(json.dumps(r.json(), indent=4))

        .. tab-item:: Bash

            .. code-block:: bash

                curl -X GET "http://apexgroup.web.illinois.edu/rubinrocks2/residencetime/?a=2.5&e=0.6&i=45" -H "accept: application/json"


**Example Response**

.. code-block:: json

    [
     {"author":"Rubin Rocks",
     "data":{
            "units":{"IMC":"","JFC":"","MMR3to1":"","OMB":"","a":"au","cumulative_residence_time":"","e":"","i":"deg","nu6":"","residence_time":""},
            "values":{"IMC":0.1670546396,"JFC":0.0,"MMR3to1":0.6602536172,"OMB":0.0676440411,"a":2.5,"cumulative_residence_time":0.8165048718,"e":0.6,"i":45.0,"nu6":0.1050466508,"residence_time":1.23651e-05}}}
    ]


Retrieve dynamical information of a near-Earth Object by Orbit with Uncertainty
-------------------------------------------------------------------------------

.. http:get:: /source_regions_sigma/
   :noindex:

   Retrieve dynamical information of a near-Earth Object

   :query a: (*required*) -- Semimajor axis [au]
   :query e: (*required*) -- Orbital eccentricity [0-1)
   :query i: (*required*) -- Inclination [deg] (< 180 deg)
   :query siga: (*required*) -- Uncertainty in semimajor axis (1-sigma) [au]
   :query sige: (*required*) -- Uncertainty in orbital eccentricity (1-sigma) [0-1)
   :query sigi: (*required*) -- Uncertainty in inclination (1-sigma) [deg] (< 180 deg)


**Example Request**
    .. tab-set::

        .. tab-item:: Browser 

            `http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_sigma/?a=2.5&e=0.6&i=45&siga=0.1&sige=0.1&sigi=2 <http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_sigma/?a=2.5&e=0.6&i=45&siga=0.1&sige=0.1&sigi=2>`_

        .. tab-item:: Python

            .. code-block:: python

                import requests
                import json

                url = 'http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_sigma/;'
                params = {      'a': 2.5,
                                'e': 0.6,
                                'i': 45,
                                'siga': 0.1,
                                'sige': 0.1,
                                'sigi': 1
                                }
                r = requests.get(url, params=params)
                print(json.dumps(r.json(), indent=4))

        .. tab-item:: Bash

            .. code-block:: bash

                curl -X GET "http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_sigma/?a=2.5&e=0.6&i=45&siga=0.1&sige=0.1&sigi=2" -H "accept: application/json"


**Example Response**

.. code-block:: json

    [
        {"author":"Rubin Rocks",
        "data":{
            "cov":{
                "labels":["a","e","i","residence_time","cumulative_residence_time","nu6","MMR3to1","IMC","OMB","JFC"],
                "values":[[0.0087390201,0.0006084389,0.0288004292,-8.93e-08,0.0040600574,-0.0017321102,-0.0013046643,0.0003148424,0.0006939393,0.0002919768],[0.0006084389,0.0082724292,0.0040397832,1.53e-07,0.0007002069,0.0021385326,0.008129827,0.0023161197,0.003104753,0.0001898666],[0.0288004292,0.0040397832,2.8701298574,-2.584e-06,0.0139796706,-0.002988076,-0.008398468,0.0137708944,-0.0209496197,0.0004300061],[-8.93e-08,1.53e-07,-2.584e-06,0.0,-2.88e-08,1.045e-07,6.648e-07,1.08e-07,1.175e-07,-4e-09],[0.0040600574,0.0007002069,0.0139796706,-2.88e-08,0.0019270303,-0.0007372367,-2.81264e-05,0.0002486015,0.0004799652,0.0001278618],[-0.0017321102,0.0021385326,-0.002988076,1.045e-07,-0.0007372367,0.0023046566,0.0064113327,0.0023031981,0.0003619277,2.83059e-05],[-0.0013046643,0.008129827,-0.008398468,6.648e-07,-2.81264e-05,0.0064113327,0.0374211184,0.0092949929,0.0026068935,-8.54915e-05],[0.0003148424,0.0023161197,0.0137708944,1.08e-07,0.0002486015,0.0023031981,0.0092949929,0.0055898314,-0.0002706998,-1.04071e-05],[0.0006939393,0.003104753,-0.0209496197,1.175e-07,0.0004799652,0.0003619277,0.0026068935,-0.0002706998,0.0034123918,0.0002024987],[0.0002919768,0.0001898666,0.0004300061,-4e-09,0.0001278618,2.83059e-05,-8.54915e-05,-1.04071e-05,0.0002024987,7.82435e-05]]},"mean":{"IMC":0.1695152573,"JFC":0.0018382703,"MMR3to1":0.5441905806,"OMB":0.0565724297,"a":2.5,"cumulative_residence_time":0.8147041305,"e":0.59,"i":45.27,"nu6":0.1130910616,"residence_time":9.8387e-06},"sigma":{"IMC":0.0747651749,"JFC":0.0088455351,"MMR3to1":0.1934453886,"OMB":0.0584156807,"a":0.0934827262,"cumulative_residence_time":0.0438979536,"e":0.0909528956,"i":1.6941457604,"nu6":0.048006839,"residence_time":4.103e-06},
            "units":{"IMC":"","JFC":"","MMR3to1":"","OMB":"","a":"au","cumulative_residence_time":"","e":"","i":"deg","nu6":"","residence_time":""}},
            "input":{"a":2.5,"cov":[[0.01,0.0,0.0],[0.0,0.01,0.0],[0.0,0.0,4.0]],"e":0.6,"i":45.0}}
    ]


Retrieve dynamical information of a near-Earth Object by Orbit with Covariance
-------------------------------------------------------------------------------

.. http:get:: /source_regions_covariance/
   :noindex:

   Retrieve dynamical information of a near-Earth Object

   :query a: (*required*) -- Semimajor axis [au]
   :query e: (*required*) -- Orbital eccentricity [0-1)
   :query i: (*required*) -- Inclination [deg] (< 180 deg)
   :query cov: (*required*) -- 3 x 3 Covariance matrix in a, e, i

**Example Request**
    .. tab-set::

        .. tab-item:: Browser

            `http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_covariance/?a=2.5&e=0.6&i=45&cov=0.2,0.1,0.4,0.1,0.1,0.2,0.4,0.2,1 <http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_covariance/?a=2.5&e=0.6&i=45&cov=0.2,0.1,0.4,0.1,0.1,0.2,0.4,0.2,1>`_

        .. tab-item:: Python

            .. code-block:: python

                import requests
                import json

                url = 'http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_covariance/;'
                params = {      'a': 2.5,
                                'e': 0.6,
                                'i': 45,
                                'cov': [0.2,0.1,0.4,0.1,0.1,0.2,0.4,0.2,1]
                                }
                r = requests.get(url, params=params)
                print(json.dumps(r.json(), indent=4))

        .. tab-item:: Bash

            .. code-block:: bash

                curl -X GET "http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_covariance/?a=2.5&e=0.6&i=45&cov=0.2,0.1,0.4,0.1,0.1,0.2,0.4,0.2,1" -H "accept: application/json"


**Example Response**

.. code-block:: json

    [
        {"author":"Rubin Rocks","data":{"cov":{"labels":["a","e","i","residence_time","cumulative_residence_time","nu6","MMR3to1","IMC","OMB","JFC"],"values":[[0.1691934964,0.0825378428,0.3749162532,-5.679e-07,0.0735494209,-0.0137262348,0.0332034551,-0.0055552428,0.0137113165,0.0402209123],[0.0825378428,0.0775052327,0.1877433854,1.621e-07,0.0366812332,0.006785096,0.0394807475,0.0070376781,0.0114864353,0.0253462314],[0.3749162532,0.1877433854,0.9962577028,-1.1416e-06,0.1629738454,-0.026062717,0.0707792691,-0.0115999078,0.0332838657,0.0958472753],[-5.679e-07,1.621e-07,-1.1416e-06,0.0,-1.381e-07,3.684e-07,6.656e-07,5.382e-07,-5e-10,-2.107e-07],[0.0735494209,0.0366812332,0.1629738454,-1.381e-07,0.034164604,-0.0075227092,0.0184050176,-0.0009187458,0.0060003198,0.0163972004],[-0.0137262348,0.006785096,-0.026062717,3.684e-07,-0.0075227092,0.0168520639,0.0081414315,0.0093686654,-0.0007392053,-0.005510422],[0.0332034551,0.0394807475,0.0707792691,6.656e-07,0.0184050176,0.0081414315,0.0545956487,0.013509048,0.0057402911,-0.0055258542],[-0.0055552428,0.0070376781,-0.0115999078,5.382e-07,-0.0009187458,0.0093686654,0.013509048,0.01532763,-0.0004522073,-0.0038220063],[0.0137113165,0.0114864353,0.0332838657,-5e-10,0.0060003198,-0.0007392053,0.0057402911,-0.0004522073,0.005008386,0.0026955426],[0.0402209123,0.0253462314,0.0958472753,-2.107e-07,0.0163972004,-0.005510422,-0.0055258542,-0.0038220063,0.0026955426,0.0365826618]]},"mean":{"IMC":0.1515349747,"JFC":0.1011164042,"MMR3to1":0.323557056,"OMB":0.0507357531,"a":2.5,"cumulative_residence_time":0.7759075227,"e":0.61,"i":45.01,"nu6":0.1339678194,"residence_time":5.9103e-06},"sigma":{"IMC":0.1238048062,"JFC":0.1912659452,"MMR3to1":0.2336571179,"OMB":0.0707699514,"a":0.4113313706,"cumulative_residence_time":0.1848366956,"e":0.2783976161,"i":0.9981270975,"nu6":0.1298154996,"residence_time":5.6641e-06},"units":{"IMC":"","JFC":"","MMR3to1":"","OMB":"","a":"au","cumulative_residence_time":"","e":"","i":"deg","nu6":"","residence_time":""}},"input":{"a":2.5,"cov":[[0.2,0.1,0.4],[0.1,0.1,0.2],[0.4,0.2,1.0]],"e":0.6,"i":45.0}}
    ]


Retrieve a slice of data from a near-Earth object model
-------------------------------------------------------

.. http:get:: /source_regions_slice/
    :noindex:

    Return gridpoints of a slice through the NEO model for a constant semimajor axis, eccentricity or inclination 

    :query a: (*required*) -- Semimajor axis [au]
    :query e: (*required*) -- Orbital eccentricity [0-1)
    :query i: (*required*) -- Inclination [deg] (< 180 deg)
    :query slicevariable: (*required*) -- Constant variable in a slice ("a","e","i") 
    :query output: (*required*) -- Orientation of JSON output (‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’)

**Example Request**
    .. tab-set::
        .. tab-item:: Browser 

            `http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_slice/?a=1.5&e=0.5&i=25&slicevariable=i&output=table <http://apexgroup.web.illinois.edu/rubinrocks2/source_regions_slice/?a=1.5&e=0.5&i=25&slicevariable=i&output=table>`_

        .. tab-item:: Python

            .. code-block:: python

                import requests
                import json

                url = 'https://apexgroup.web.illinois.edu/rubinrocks2/source_regions_slice/'
                  params = {    'a': 1.5,
                                'e': 0.5,
                                'i': 25,
                                'slicevariable': 'i',
                                'output': 'table
                                }
                r = requests.get(url, params=params)
                print(json.dumps(r.json(), indent=4))

        .. tab-item:: Bash

            .. code-block:: bash

                curl -X GET "https://apexgroup.web.illinois.edu/rubinrocks2/source_regions_slice/?a=1.5&e=0.5&i=25&slicevariable=i&output=table" -H "accept: application/json"


**Example Response**

.. code-block:: json

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