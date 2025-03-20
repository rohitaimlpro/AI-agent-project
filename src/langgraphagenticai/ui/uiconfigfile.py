from configparser import ConfigParser
class Config:
    def __init__(self,config_file = 'src/langgraphagenticai/ui/streamlitui/uiconfigfile.ini'):
        self.config=ConfigParser()
        self.config.read(config_file)
    def get__llm_option(self):
        return self.config.get('LLM_OPTIONS').split(", ")
    def get_usecase_options(self):
        return self.config['DEFAULT'].get('USECASE_OPTIONS').split(", ")
    def get_usecase_options(self):
        return self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS').split(", ")
    def get_usecase_options(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')