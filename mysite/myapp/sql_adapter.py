import psycopg2


class SqlAdapter:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="123456")

    def __enter__(self):
        self.conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="123456")
        return self

    def __exit__(self, type, value, traceback):
        self.conn.close()

    def getAllDocuments(self):
        query = """SELECT
        "Name", Count("Url")
        FROM
        urls
        GROUP
        BY
        "Name";"""

        cur = self.conn.cursor()
        cur.execute(query)

        return cur.fetchall()

    def getUrlsForName(self, name):
        query = """SELECT Distinct
        "Url"
        From
        urls
        WHERE
        "Name" = '{name}';""".format(name=name)

        cur = self.conn.cursor()
        cur.execute(query)

        return cur.fetchall()

    def getNumUrlsForName(self):
        query = """SELECT
                "Url", Count("Name")
                FROM
                urls
                GROUP
                BY
                "Url";"""

        cur = self.conn.cursor()
        cur.execute(query)

        return cur.fetchall()

    def saveUrls(self, urls, name):
        for url in urls:
            self.saveUrl(url, name)

        self.commitUrls()

    def saveUrl(self, url, name):
        query = """INSERT
                INTO
                urls("Url", "Name")
                VALUES
                ('{url}','{name}');""".format(url=url, name=name)

        cur = self.conn.cursor()
        cur.execute(query)

    def commitUrls(self):
        self.conn.commit()


