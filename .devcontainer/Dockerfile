FROM python3.12-bookworm

WORKDIR /usr/src/app

COPY pyproject.toml && poetry.lock ./
RUN poetry install

COPY . .

CMD [ "python", "manage.py", "runserver" ]
