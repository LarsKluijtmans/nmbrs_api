import xmltodict


def parse_xml_to_dict(xml: str) -> dict | str:
    """
    Try to parse the XML string into a dictionary.
    If parsing fails, return the original XML string.

    :param xml: A string that contains an XML document.
    :return: A dictionary representation of the XML or the original XML string.
    """
    try:
        return xmltodict.parse(xml)
    except Exception:
        return xml


def get_xml(xml: str) -> dict | None:
    """
    Method to retrieve XML data as a dictionary.

    :return: A dictionary representation of the XML data, or None if parsing fails.
    """
    xml = parse_xml_to_dict(xml)
    if type(xml) is not dict:
        return None
    return xml
