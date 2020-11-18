import subprocess
import json

class Deployer:
    config_file = None ## STRING
    user = None ## STRING
    tracked_data = {} ## DICT

    def __init__(self, filename="deployer/config.json"):
        """
        ### Deployer
        
        Tested on github
        """
        self.config_file = filename

        json_data = json.load(open(filename))

        self.user = json_data["user"]
        self.tracked_data = json_data["tracked_data"]

    def sync_cloners(self):
        """Adds "cloner"(shell script)"""

        for json_obj in self.tracked_data:
            cloner_repo = json_obj["repo"]
            cloner_dir = json_obj["dir"]

            cloner_content = f"""#!/bin/bash
cd {cloner_dir}; git clone https://github.com/{self.user}/{cloner_repo}"""

            f = open(f"deployer/cloners/{cloner_repo}.sh", "w")
            f.write(cloner_content)
            f.close()