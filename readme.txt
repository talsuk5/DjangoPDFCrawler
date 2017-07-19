Environment details:
Sql - PostgreSQL 9.6
Python version - 3.6.1
Django version - 1.11.3

External python libs:
PyPDF2 - 1.26.0
simplejson - 3.11.1
psycopg2 - 2.7.1

assumptions:
- local PostgreSql (host="localhost", database="postgres", user="postgres", password="123456")
- existing sql table named urls
- names for documents uploaded are unique

Api:
GET  [base_url]/documents                   get all documents uploaded with number of urls in each
GET  [base_url]/urls                        get a list of urls and number of documents they were found on
GET  [base_url]/document/?name=[name]       get all urls for document
POST [base_url]/upload_file/?name=[name]    upload a file with unique name