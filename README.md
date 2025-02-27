# Artist's Artwork API: 

I've worked as a visual artist for the last 20/25 years, and have a lot of artwork!
This is an API in line with something like the Met Museum of Art's artwork API, in order to have a place to archive -- and make accessible -- all my artwork.

Also, there can be many artists in here. And it can be also used as a CRM. This is all yet to come. In the end, this API should be suitable for a Museum or Gallery use. 

Can then build a portfolio, and API access tool to scan throught the artworks -- and then for the artist to process images into whatever formats needed.

-Nick

## Tech

### Backend
Python & FastAPI & PostgreSQL:
Choosing Pythonfor it's rich image processing and analyzing libraries like PILLOW and NUMPY. Therefore building the API with FastAPI and connecting to these server-side image processing powerhouses. Originally, I designed the schema and wrote the database in SQLITE, however, for the web and produciton, Postgres to make it scalable.

### Frontend: 
TK. Planning on Typescript and Next.JS. The latter for proper SEO on a largely read-heavy portfolio site + API search tool/GUI. Typescript, becuase it is time to use a more production ready iteration of JavaScript. 

# Setup & Development

## Install and setup
- Clone
- install requirements
- create postgres DB locally + one online if deploying to the world wide web.
- add .env with: 
    - End up with two Database URLS, also the online Postgres db, commenting out the one not in use.
    
    `DATABASE_URL="your postgres db info"`
    `SECRET_KEY=<YOUR KEY>`
    `ACCESS_TOKEN_EXPIRE_MINUTE=1200`
    `ADMIN_PWD=<YOUR password>`
    `ART_LOVER_PWD=<YOUR password>` 

- Run to set up your db `alembic upgrade head`
- Seed db: `python3 -m db.seed`

## Run locally
- `python -m uvicorn main:app --reload`  
- OR `uvicorn main:app --reload`

## Alembic for Database Migrations
- `alembic current`
- `alembic revision --autogenerate -m "your note here:)"`
- `alembic upgrade head`

## Update requirements when adding new libraries/packages...
- `pip freeze > requirements.txt`


---
### Start Template and Deploying to RENDER
Note: used this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.
https://github.com/render-examples/fastapi/generate

See https://render.com/docs/deploy-fastapi or follow the steps below:

### Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.