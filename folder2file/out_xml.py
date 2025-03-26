"""
Module for formatting folder structure as XML.
"""
import xml.dom.minidom
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional


def format_xml(data: Dict[str, Any], no_newline: bool) -> str:
    """
    Format the folder structure as XML.

    Args:
        data: The folder structure data to format
        no_newline: Whether to remove unnecessary newlines from file contents

    Returns:
        The formatted XML string
    """
    root = ET.Element("folderStructure")

    # Process each top-level folder
    for folder_name, entries in data.items():
        folder_elem = ET.SubElement(root, "folder", name=folder_name)
        process_entries(folder_elem, entries, no_newline)

    # Convert to string with proper formatting
    rough_string = ET.tostring(root, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def process_entries(parent_elem: ET.Element, entries: list, no_newline: bool) -> None:
    """
    Process entries recursively and add them to the parent element.

    Args:
        parent_elem: The parent XML element
        entries: List of entries to process
        no_newline: Whether to remove unnecessary newlines
    """
    for entry in entries:
        for name, content in entry.items():
            if isinstance(content, list):  # It's a directory
                folder_elem = ET.SubElement(parent_elem, "folder", name=name)
                process_entries(folder_elem, content, no_newline)
            else:  # It's a file
                file_elem = ET.SubElement(parent_elem, "file", name=name)
                if content is not None:
                    content_elem = ET.SubElement(file_elem, "content")
                    if no_newline:
                        content = content.replace("\n", " ")
                    content_elem.text = content
                else:
                    # Add an empty content element with a skipped attribute
                    ET.SubElement(file_elem, "content", skipped="true")
