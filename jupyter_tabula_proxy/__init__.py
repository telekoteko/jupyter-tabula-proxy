import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def setup_tabula():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """

    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "icons", "tabula.svg"
        )

    # Make sure executable is in $PATH
    def _get_tabula_command(port):
        # java -Dfile.encoding=utf-8 -Xms256M -Xmx1024M -Dwarbler.port=9999 -jar tabula.jar
        return ["java", "-Dfile.encoding=utf-8", " -Xms256M" + "-Xmx1024M" + "-Dwarbler.port=" + str(port) + "-jar tabula.jar"]

    return {
        "command": _get_tabula_command,
        "timeout": 20,
        "new_browser_tab": True,
        "launcher_entry": {"title": "tabula", "icon_path": _get_icon_path()},
    }