"""Data models for Zendesk Knowledge Base entities."""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Category(BaseModel):
    """Zendesk Knowledge Base Category."""

    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    locale: str = "en-us"
    source_locale: Optional[str] = None
    outdated: bool = False
    position: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Section(BaseModel):
    """Zendesk Knowledge Base Section."""

    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    locale: str = "en-us"
    category_id: int
    position: int = 0
    sorting: str = "manual"
    outdated: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Article(BaseModel):
    """Zendesk Knowledge Base Article."""

    id: Optional[int] = None
    title: str
    body: str
    locale: str = "en-us"
    section_id: int
    author_id: Optional[int] = None
    draft: bool = False
    promoted: bool = False
    position: int = 0
    label_names: list[str] = Field(default_factory=list)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
