import connexion


app = connexion.App(__name__, specification_dir="./")
app.add_api("api.yml")


"""Start the python web server"""


def main():
    app.run(debug=True)
