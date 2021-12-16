import json
import os
from agent import Agent


class Script:

    def load_data(self, file, agent):
        """this method read json file
        :param file: json file
        :param agent: dict new agent
        :return: data file json"""

        with open(file) as json_file:
            data = json.loads(json_file.read())
            data.append(agent)
            return data

    def write_data_file(self, input_file, output_file, agent):
        """this method write a new json file
               :param input_file: json file
               :param output_file: json file
               :param agent: dict new agent
               :return: file json"""

        data = self.load_data(input_file, agent)
        with open(output_file, "w") as outfile:
            json.dump(data, outfile, indent=4)

    def print_all_agents(self, file, agent):
        """this method print all agents
        :param agent: dict new agent
        :param file: json file"""

        data = self.load_data(file, agent)

        print(json.dumps(data, indent=4))


dict_module = {
    "fim": {
        "status": "enabled",
        "frequency": 5,
        "eps": 100
    },
    "syscollector": {
        "status": "enabled",
        "frequency": 10,
        "eps": 20
    },
    "rootcheck": {
        "status": "disabled",
        "frequency": 20,
        "eps": 40
    },
    "winevt": {
        "status": "disabled",
        "frequency": 12,
        "eps": 300
    },
    "logcollector": {
        "status": "disabled",
        "frequency": 5,
        "eps": 20
    }}

agent_ = Agent(_id=6, name='agent_6', version='4.1.5', os='ubuntu 20.04', inventory=["nano", "git", "aws-cli"],
               modules=dict_module, status='active')


new_agent = agent_.show_all_attributes_agent()


def main():
    script = Script()
    data = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')
    output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output.json')

    script.load_data(file=data, agent=new_agent)

    script.write_data_file(input_file=data, output_file=output_file, agent=new_agent)

    script.print_all_agents(file=output_file, agent=new_agent)


main()
