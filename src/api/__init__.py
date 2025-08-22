"""
API Management Package
External API integration and management for the Living Codex system
"""

from .management.api_manager import APIManagementSystem

__all__ = [
    "APIManagementSystem"
]

# Additional components will be imported as they are implemented
# from .integration.external_api_system import RealExternalAPISystem
