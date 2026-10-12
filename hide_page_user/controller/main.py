import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class UserPageConfiguration(http.Controller):

    @http.route('/get_user_page_configurations', auth='user', type='json', csrf=False)
    def get_user_page_configurations(self):
        user = request.env.user
        _logger.info("API called by user: %s (ID: %s)", user.name, user.id)

        try:
            if hasattr(user, 'get_user_page_configurations'):
                result = user.get_user_page_configurations()
                _logger.info("Page configurations result: %s", result)
                return result or []
            else:
                _logger.warning("Method get_user_page_configurations not found on user model")
                return []
        except Exception as e:
            _logger.error("Error in get_user_page_configurations: %s", str(e))
            return []