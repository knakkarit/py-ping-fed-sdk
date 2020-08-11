import os
import logging
from requests import Session
from requests.exceptions import HTTPError


class _oauth_tokenExchange_generator():
    def __init__(self, endpoint:str, session:Session) -> None:
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL._oauth_tokenExchange_generator')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.endpoint = endpoint
        self.session = session

    def _build_uri(self, path: str):
        return f"{self.endpoint}{path}"

    def getSettings(self):
        """ Get general OAuth 2.0 Token Exchange Generator settings.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/tokenExchange/generator/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
        finally:
            return response

    def updateSettings(self, body, bypassExternalValidation):
        """ Update general OAuth 2.0 Token Exchange Generator settings.
        """

        payload = {
            "body": body,
            "bypassExternalValidation": bypassExternalValidation

        }

        try:
            response = self.session.put(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/generator/settings"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Settings updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getGroups(self):
        """ Get list of OAuth 2.0 Token Exchange Generator groups.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/tokenExchange/generator/groups"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
        finally:
            return response

    def createGroup(self, body, bypassExternalValidation):
        """ Create a new OAuth 2.0 Token Exchange Generator group.
        """

        payload = {
            "body": body,
            "bypassExternalValidation": bypassExternalValidation

        }

        try:
            response = self.session.post(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/generator/groups"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 201:
                self.logger.info('Token Exchange Processor Policy created.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def getGroup(self, var_id):
        """ Find an OAuth 2.0 Token Exchange Generator group by ID.
        """

        try:
            response = self.session.get(

                url=self._build_uri("/oauth/tokenExchange/generator/groups/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Success.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
        finally:
            return response

    def updateGroup(self, var_id, body, bypassExternalValidation):
        """ Update an OAuth 2.0 Token Exchange Generator group.
        """

        payload = {
            "var_id": var_id,
            "body": body,
            "bypassExternalValidation": bypassExternalValidation

        }

        try:
            response = self.session.put(
                data=payload,
                url=self._build_uri("/oauth/tokenExchange/generator/groups/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 200:
                self.logger.info('Token Exchange Processor Policy updated.')
            if response.status_code == 400:
                self.logger.info('The request was improperly formatted or contained invalid fields.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

    def deleteGroup(self, var_id):
        """ Delete an OAuth 2.0 Token Exchange Generator group.
        """

        try:
            response = self.session.delete(

                url=self._build_uri("/oauth/tokenExchange/generator/groups/{id}"),
                headers={'Accept': 'application/json'}
            )
        except HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            self.logger.error(f'Error occurred: {err}')
        else:
            if response.status_code == 204:
                self.logger.info('Token Exchange Processor Policy deleted.')
            if response.status_code == 403:
                self.logger.info('PingFederate does not have the IdP, SP and OAuth roles enabled. Operation not available.')
            if response.status_code == 404:
                self.logger.info('Resource not found.')
            if response.status_code == 422:
                self.logger.info('Validation error(s) occurred.')
        finally:
            return response

