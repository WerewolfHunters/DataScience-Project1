import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from src.datascience import logger
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): input filepath

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type value
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of dictionaries

    Args:
        path_to_directories (list): creates a list of directories
        ignore_log (bool, optional): ignore if multiple directories is created. Default is set to True 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data

    Args:
        path (str): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"Json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data

    Args:
        path (str): path to json file
    
    Returns:
        ConfigBox: data as class attributes not as dict 
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully at: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary files

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """loads binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data