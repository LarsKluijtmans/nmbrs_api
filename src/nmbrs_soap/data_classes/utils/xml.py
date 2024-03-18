"""
This module provides functions for parsing XML strings into dictionaries.

Functions:
    parse_xml_to_dict(xml: str) -> dict | str: Try to parse the XML string into a dictionary.
        If parsing fails, return the original XML string.
    get_xml(xml: str) -> dict | None: Retrieve XML data as a dictionary.

Dependencies:
    xmltodict: A library for parsing XML into Python dictionaries.
"""

import xmltodict


def parse_xml_to_dict(xml: str) -> dict | str:
    """
    Try to parse the XML string into a dictionary.
    If parsing fails, return the original XML string.

    Args:
        xml (str): A string that contains an XML document.

    Returns:
        dict | str: A dictionary representation of the XML or the original XML string.
    """
    try:
        return xmltodict.parse(xml)
    except Exception:
        return xml


def get_xml(xml: str) -> dict | None:
    """
    Method to retrieve XML data as a dictionary.

    Args:
        xml (str): A string that contains an XML document.

    Returns:
        dict | None: A dictionary representation of the XML data, or None if parsing fails.
    """
    xml = parse_xml_to_dict(xml)
    if not isinstance(xml, dict):
        return None
    return xml
