import json
import os
import sys
import requests
import logging
from helpers import json_type_convert, safe_name


class Fetch():
    def __init__(self, swagger_url, api_schema_key="apis"):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
        )
        self.project_path = os.path.dirname(os.path.realpath(__file__))
        self.logger = logging.getLogger("PingDSL.Fetch")
        self.logger.setLevel(
            int(os.environ.get("Logging", logging.INFO))
        )
        self.api_schema_key = api_schema_key
        self.swagger_url = swagger_url
        self.ping_data = {}
        self.models = {}
        self.apis = {}
        self.enums = {}

    def get_source(self, verify=False):
        """
            Pull the API JSON from the remote swagger url
        """

        try:
            response = requests.get(self.swagger_url, verify=verify)
        except Exception as err:
            err_str = f"Failed to download swagger from: {self.swagger_url} with error {err}"
            self.logger.error(err_str)
            raise ConnectionError(err_str)
        self.logger.info(f"Successfully downloaded Ping Swagger document: {self.swagger_url}")
        self.ping_data = response.json()
        self.write_json(data=self.ping_data, name="pf-admin-api", directory="./source/")
        self.logger.debug(
            json.dumps(self.ping_data, default=str, sort_keys=True, indent=4, separators=(",", ": "))
        )

    def write_json(self, data, name, directory=None):
        """
            given string data write it to file name in folder directory
        """
        if not directory:
            directory = "./templates/resources/"
        targetdirectory = os.path.join(self.project_path, directory)

        if not os.path.exists(targetdirectory):
            os.makedirs(targetdirectory)

        path = f"{targetdirectory}/{name}.json"

        with open(os.path.join(self.project_path, path), "w") as fh:
            fh.write(json.dumps(data, default=str, sort_keys=True, indent=4, separators=(",", ": ")))

    def read_json(self, file):
        """
            extract a JSON document from the project path
            and load into a dict type
        """
        try:
            with open(os.path.join(self.project_path, file), "r") as file:
                return json.loads(file.read())
        except IOError as err:
            return False

    def get_api_schema(self, api_schema_key="apis", verify=False):
        """
            Iterate over each API in the schema file pf-admin-api and pull
            down each paths content. Store in the api and model dictionaries
            and write to the repository
        """
        for api in self.ping_data.get(api_schema_key, {}):
            safe_api_path = safe_name(api.get("path"))
            api_path = api.get("path")
            abs_path = f"{self.project_path}/source/apis/{safe_api_path}.json"
            if os.path.exists(abs_path):
                response = self.read_json(file=abs_path)
                self.apis[safe_name(response.get("resourcePath", safe_api_path))] = self.get_api_imports(response.get("apis", []))
                self.models.update(response.get("models", {}))
            else:
                try:
                    self.logger.info(f"Attempting to retrieve {self.swagger_url}{api_path}")
                    response = requests.get(f"{self.swagger_url}{api.get('path')}", verify=verify)
                except Exception as err:
                    self.logger.error(f"Failed to download swagger from: {self.swagger_url}{api_path} with error {err}")
                else:
                    r_json = response.json()
                    self.apis[r_json.get("resourcePath", safe_api_path)] = self.get_api_imports(r_json.get("apis", []))
                    self.models.update(r_json.get("models", {}))
                    self.logger.debug(f"Successfully downloaded Ping Swagger document: {self.swagger_url}{api_path}")
                    self.write_json(data=r_json, name=safe_api_path, directory="./source/apis/")

        for model, details in self.models.items():
            details["imports"] = self.get_model_imports(details)
            self.models[model] = details

    def get_api_imports(self, api_data):
        """
        Pre-process the API document and determine what needs to be imported
        to dynamically generate return objects
        """
        imports = set()
        for data in api_data:
            for op in data["operations"]:
                if not json_type_convert(op["type"]) and op["type"] not in imports:
                    imports.add(op["type"])
        return {"imports": imports, "details": api_data}

    def get_model_imports(self, model_data):
        """
        For a given model, determine it's other model dependencies, enum dependencies
        and cache discovered
        """
        imports = {"models": set(), "enums": set()}
        for prop in model_data.get("properties").values():
            class_name = prop.get("$ref", "")
            # check for a model import and add it to the set
            if class_name and class_name not in imports \
               and "enum" not in prop and not class_name.startswith("Map"):
                imports["models"].add(class_name)
            # check for an enum import and add it to the set
            elif class_name and "enum" in prop:
                if class_name in self.enums and self.enums[class_name] != prop["enum"]:
                    self.logger.warn(
                        f"Found redefined enum type: {class_name} original -> {self.enums[class_name]}, new -> {prop['enum']}..."
                    )
                self.enums[class_name] = prop["enum"]
                imports["enums"].add(class_name)

        return imports

    def fetch(self):
        self.get_source()
        self.get_api_schema()

        return {
            "models": self.models,
            "apis": self.apis,
            "enums": self.enums
        }


if __name__ == "__main__":
    Fetch("https://localhost:9999/pf-admin-api/v1/api-docs").fetch()
