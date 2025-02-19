import os
import yaml

def read_config_file(filepath):
    try:
        with open(filepath, "r") as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {filepath}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

# config_path = "../config/configs.yaml"
# config = read_config_file(config_path)
#
# if config:
#     print("Configuration loaded successfully.")