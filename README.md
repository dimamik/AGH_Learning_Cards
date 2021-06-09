<!-- PROJECT LOGO -->
<br />
<p align="center">

<h3 align="center">AGH Learning Cards</h3>

  <p align="center">
    Web Application to Learn words  and its definitions represented in card front-back form
    <br />
    <br />
    <br />
    <a href="https://github.com/dimamik/learning-cards-front">Front</a>
    ·    
    <a href="http://95.111.249.217">View Demo</a>
    ·
    <a href="https://github.com/dimamik/AGH_Learning_Cards/issues">Report Bug</a>
    ·
    <a href="https://github.com/dimamik/AGH_Learning_Cards/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#project-presentation">Project Presentation</a></li>
    <li><a href="#technology-stack">Technology Stack</a></li>
    <li><a href="#database-diagram">Database Diagram</a></li>
    <li><a href="#api-endpoints">API Endpoints</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Authors

Dzmitry Mikialevich

Konrad Kowalczyk

## About The Project

This is a project of a web application (backend + frontend) which allows users to learn various topics by so-called
“learning cards”.    
Front page of such a reversible card contains a word to learn and the back contains description or definition.    
Database stores users’ accounts data, their collections of cards and the collections “liked” by them.

## Project Presentation

[![Product Name Screen Shot][product-screenshot]]()

## Technology Stack

- Database:
    - [Postgresql 13](https://www.postgresql.org/)
- Backend:
    - [Python 3.6 or newer](https://www.python.org)
    - [Flask 2.0](https://flask.palletsprojects.com/en/2.0.x/)
    - [SQLAlchemy 1.4](https://www.sqlalchemy.org/)
- Frontend:
    - [Vue.js 2](https://vuejs.org/)
    - [Vuetify 2.5](https://vuetifyjs.com/en/)

## Database Diagram

[![Database][database-scheme]]()

## API Endpoints

Can be found at: [router.py](app/http/router.py)

| ADDRESS:://{ }                             | METHOD | NOTES                                                                                | REQUEST                                                           | RESPONSE                                                                                                                                                                                              |
| ------------------------------------------ | ------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api/auth/sign-in                           | post   | Client browser receives a session\_id as a cookie                                    | {<br>email: string,<br>password: string<br>}                      | HTTP: 200 OK<br>{<br>userName: string<br>userID: int<br>}                                                                                                                                             |
| api/auth/sign-up                           | post   | Client browser receives a session\_id as a cookie                                    | {<br>username: string,<br>email: string,<br>password: string<br>} | HTTP: 201 CREATED<br>{<br>userName: string<br>userID: int<br>}                                                                                                                                        |
| api/auth/sign-out                          | post   |                                                                                      |                                                                   | HTTP: 204 NO\_CONTENT                                                                                                                                                                                 |
| api/auth/current-user                      | get    | Returns logged in user                                                               |                                                                   | HTTP: 200 OK<br>{<br>userID: int,<br>userName: string,<br>userEmail: string,<br>userInfo: json<br>}                                                                                                   |
| api/collections                            | get    | Returns all collections, {page, size} query params                                   |                                                                   | HTTP: 200 OK<br>\{<br>total: int,<br>data: [{<br>is\_liked: boolean,<br>collectionID: int,<br>collectionName: string,<br>collectionDescription: json,<br>holderID: int,<br>cardInfo: json<br>}\]<br>} |
| api/collections/user/{user\_id}            | get    | Returns collections created by user {page, size} query params                        |                                                                   | HTTP: 200 OK<br>\{<br>total: int,<br>data: [{<br>is\_liked: boolean,<br>collectionID: int,<br>collectionName: string,<br>collectionDescription: json,<br>holderID: int,<br>cardInfo: json<br>}\]<br>} |
| api/collections/{collection\_id}           | get    | Returns single collection                                                            |                                                                   | HTTP: 200 OK<br>\[<br>{<br>cardID: int,<br>collectionID: int,<br>cardInside: json,<br>is\_watched: boolean<br>}<br>\]                                                                                 |
| api/current-user/collections               | post   | Creates a new collection, login required                                             | {<br>collectionDescription: string<br>collectionName: string<br>} | HTTP: CREATED                                                                                                                                                                                         |
| api/current-user/collections               | delete | Removes a collection, login required, ownership required                             | {<br>collection\_id: int<br>}                                     | HTTP: NO\_CONTENT                                                                                                                                                                                     |
| api/current-user/favourite                 | get    | Returns favourite collections of the user, login required, {page, size} query params |                                                                   | HTTP: 200 OK<br>\[<br>total: int,<br>data: [{<br>is\_liked: boolean,<br>collectionID: int,<br>collectionName: string,<br>collectionDescription: json,<br>holderID: int,<br>cardInfo: json<br>}\]<br>} |
| api/current-user/favourite/{collection-id} | post   | Adds the collection to favourites, login required                                    |                                                                   | HTTP: OK                                                                                                                                                                                              |
| api/current-user/favourite/{collection-id} | delete | Removes the collection from favourites, login required                               |                                                                   | HTTP: OK                                                                                                                                                                                              |
| api/collections/{collection\_id}           | post   | Adds a card to the collection, ownership required                                    |                                                                   | HTTP: OK                                                                                                                                                                                              |
| api/collections/{collection\_id}           | delete | Removes a card from the collection, ownership required                               |                                                                   | HTTP: OK                                                                                                                                                                                              |

<!-- GETTING STARTED -->

## Getting Started

To run locally:

- Install and Configure PostgreSQL
- Create POSTGRES variable in config.py file with your database credentials
- Create SECRET_KEY in config.py with securely generated hash:
    - bash: `python -c 'import os; print(os.urandom(16))'`
- Create database by running:
    - `python setup.py`
- Run `flask run` from the root folder

Contents of config.py:

```python
POSTGRES = {
    'user': 'UserName',
    'pw': 'Password',
    'db': 'DatabaseName',
    'host': 'hostName',
    'port': '5432',
}

SECRET_KEY = "Generated in previous step secret key"
```

## Fill with data from csv:
```python
def fill_with_data(csv_path,collection_id,column_front,column_back):
    import csv
    with open("out.txt", "w") as file:
        with open(csv_path,newline='') as csv_file:
            list_of_rows = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in list_of_rows:
                row[column_front] = row[column_front].replace("\"","")  
                row[column_back] = row[column_back].replace("\"","")           
                print(row)
                json_to_write = {
                    'front' : row[column_front],
                    'back' : row[column_back]
                }
                json_to_write = str(json_to_write).replace("'", "\"")
                file.write(f"{collection_id}\t{json_to_write}\n")
```

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->


<!-- ACKNOWLEDGEMENTS -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge

[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge

[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members

[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge

[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge

[issues-url]: https://github.com/othneildrew/Best-README-Template/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/othneildrew

[product-screenshot]: img/app_screen.png

[database-scheme]: img/database_diagram.png
