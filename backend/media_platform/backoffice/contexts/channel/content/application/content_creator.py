import os

from dotenv import load_dotenv
from media_platform.backoffice.contexts.channel.content.domain import (
    Content,
    ContentRepository,
)
from media_platform.backoffice.contexts.shared.infrastructure.file_manager import (
    FileManager,
)

load_dotenv()


CONTENT_STORAGE_PATH = os.getenv("CONTENT_STORAGE_PATH")


class ContentCreator:

    def __init__(self, repository: ContentRepository) -> None:
        self._repository = repository
        self._file_manager = FileManager("var/storage/content/")

    def run(
        self, files: dict, rating: float, metadata_: dict, channel_id: str
    ) -> None:
        content_files = []
        for file in files:
            path = self._file_manager.save_file(
                CONTENT_STORAGE_PATH, file.get("name"), file.get("data")
            )
            content_files.append(
                {
                    "name": file.get("name"),
                    "path": path,
                    "media_type": file.get("media_type"),
                }
            )
        content = Content.create(content_files, rating, metadata_, channel_id)
        self._repository.save(content)
